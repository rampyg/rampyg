"""
Accountability loop for a robot driven by a VLA "brain" (e.g. Gemini Robotics
ER 2, OpenVLA, a pi-family policy).

Vouch does not perceive, plan, or move — it sits *under* whatever high-level
model is deciding what to do, and makes each of those decisions attributable:

  1. on model load, the robot signs a ModelProvenanceAttestation recording *which*
     VLA build and safety policy it is about to run (swap `MODEL_NAME` for any
     brain — the layer is model-agnostic);
  2. as the brain proposes actions, each one is gated against the robot's physical
     capability scope *before* actuation; and
  3. every decision — allowed or denied — is written to an encrypted,
     tamper-evident black box, so afterwards anyone can prove what the robot was
     asked to do and what it actually did.

The "brain" here is a fixed script standing in for the real model's output; the
point is the Vouch layer around it, not the planner.

Run it:  python examples/robotics_vla_accountability_loop.py
"""

import os

from vouch import Signer, generate_identity
from vouch.robotics import (
    BlackBoxLog,
    PhysicalAction,
    SoftwareRootOfTrust,
    build_physical_scope_credential,
    build_provenance_attestation,
    check_physical_action,
    mint_robot_identity,
    verify_blackbox_chain,
    verify_provenance_attestation,
)

# Swap this for whichever brain drives the robot; the accountability layer is
# identical either way.
MODEL_NAME = "gemini-robotics-er-2"

# What the brain proposes over one task. In a real system these come from the
# model's action stream; the labels are only for the printout.
PROPOSED_ACTIONS = [
    (
        "approach part",
        PhysicalAction(force_n=20.0, speed_mps=1.2, near_humans=False, zone="assembly-cell-3"),
    ),
    (
        "hand part to operator",
        PhysicalAction(force_n=15.0, speed_mps=0.4, near_humans=True, zone="assembly-cell-3"),
    ),
    (
        "rush the handoff",
        PhysicalAction(force_n=15.0, speed_mps=1.5, near_humans=True, zone="assembly-cell-3"),
    ),
    (
        "reach into next cell",
        PhysicalAction(force_n=20.0, speed_mps=1.0, near_humans=False, zone="assembly-cell-4"),
    ),
]


def main() -> None:
    kp = generate_identity(domain="robot.acme.example.com")
    robot = Signer(private_key=kp.private_key_jwk, did=kp.did)

    # Hardware-rooted identity: this loop is attributable to one physical robot.
    root = SoftwareRootOfTrust(kind="TPM")
    identity = mint_robot_identity(
        robot, root, make="Acme Robotics", model="AR-7", serial="SN-000123"
    )
    print(f"robot {identity['credentialSubject']['serial']} online ({kp.did})\n")

    # (1) Provenance shim: record which VLA brain and safety policy is loaded.
    config = {"planner": MODEL_NAME, "guardrails": ["slow_near_humans", "zone_lock"]}
    provenance = build_provenance_attestation(
        robot,
        robot_did=kp.did,
        model_name=MODEL_NAME,
        weights_hash="uER2-WEIGHTS-DIGEST",
        safety_policy="did:web:acme.example.com#safety-policy-v3",
        config=config,
        version="2.0.0",
    )
    ok, psub = verify_provenance_attestation(provenance, kp.public_key_jwk, config=config)
    print(f"loaded brain: {psub['vla']['modelName']}  (provenance verifies: {ok})\n")

    # The enforced physical envelope the brain must stay inside.
    scope_cred = build_physical_scope_credential(
        robot,
        subject_did=kp.did,
        max_force_n=100.0,
        max_speed_mps=2.0,
        max_speed_near_humans_mps=0.5,
        allowed_zones=["assembly-cell-3"],
    )
    scope = scope_cred["credentialSubject"]["physicalScope"]

    # (3) The encrypted flight recorder. In production the key lives in an HSM and
    # the log ships to hosted black-box storage; here it is a local 32-byte key.
    blackbox = BlackBoxLog(key=os.urandom(32))

    # (2) Gate every proposed action before it reaches the actuators.
    print("brain proposes -> Vouch gate -> actuator:")
    executed = 0
    for label, action in PROPOSED_ACTIONS:
        result = check_physical_action(scope, action)
        decision = "ALLOW" if result.ok else "DENY "
        blackbox.append(
            "actuation_decision",
            {
                "action": label,
                "allowed": result.ok,
                "reasons": result.reasons,
                "speedMps": action.speed_mps,
                "zone": action.zone,
            },
        )
        detail = "" if result.ok else f"  <- {'; '.join(result.reasons)}"
        print(f"  [{decision}] {label}{detail}")
        if result.ok:
            executed += 1

    # After the task: the black box is tamper-evident without the key, so an
    # auditor can prove the record of what the robot did was not altered.
    chain_ok, err = verify_blackbox_chain(blackbox.entries())
    print(
        f"\n{executed}/{len(PROPOSED_ACTIONS)} actions actuated; "
        f"{len(blackbox.entries())} decisions logged."
    )
    print(f"black-box chain intact (tamper-evident): {chain_ok}")


if __name__ == "__main__":
    main()
