"""
EU AI Act (and ISO 10218) compliance evidence pack for a robot.

A high-risk robot assembles the Vouch credentials it already holds — a
hardware-rooted identity, a model/config provenance attestation, a physical
capability scope, and a tamper-evident safety record — and turns them into a
single signed artifact a buyer, insurer, or notified body can verify:

  1. build the credential set the robot carries,
  2. run `check_conformance` against a regulatory profile to get a deterministic,
     clause-by-clause report,
  3. sign that report into a RobotConformanceAttestation, and
  4. verify the attestation the way an external assessor would.

The profiles are an open reference crosswalk, not legal advice; a deployment
confirms each mapping against the current regulation text. See
`vouch/robotics/conformance.py` for the built-in profiles.

Run it:  python examples/robotics_ai_act_evidence_pack.py
"""

from vouch import Signer, generate_identity
from vouch.robotics import (
    SafetyEventLog,
    build_conformance_attestation,
    build_physical_scope_credential,
    build_provenance_attestation,
    build_safety_record,
    check_conformance,
    mint_robot_identity,
    verify_conformance_attestation,
    SoftwareRootOfTrust,
)

# Which regulatory profiles to produce evidence for. Both ship in
# vouch/robotics/conformance.py; add "eu-machinery-2023-1230", "iso-ts-15066",
# or "ul-3300" to widen the pack.
PROFILE_IDS = ["eu-ai-act-high-risk", "iso-10218"]


def build_credential_set(robot: Signer, robot_did: str):
    """The evidence a fielded robot carries, one credential per capability."""

    # 1. Hardware-rooted identity (ISO 10218 / UL 3300 identification).
    root = SoftwareRootOfTrust(kind="TPM")  # a real deployment signs with the TPM
    identity = mint_robot_identity(
        robot, root, make="Acme Robotics", model="AR-7", serial="SN-000123"
    )

    # 2. Model + config provenance — which VLA brain and safety policy ran
    #    (EU AI Act Art. 13 transparency, Art. 15 traceable-to-a-known-build).
    provenance = build_provenance_attestation(
        robot,
        robot_did=robot_did,
        model_name="gemini-robotics-er-2",
        weights_hash="uER2-WEIGHTS-DIGEST",
        safety_policy="did:web:acme.example.com#safety-policy-v3",
        config={"max_torque": 12.5, "guardrails": ["slow_near_humans", "zone_lock"]},
        version="2.0.0",
    )

    # 3. Physical capability scope — the enforced operating limits that give a
    #    human oversight a hard envelope (EU AI Act Art. 14).
    scope = build_physical_scope_credential(
        robot,
        subject_did=robot_did,
        max_force_n=100.0,
        max_speed_mps=2.0,
        max_speed_near_humans_mps=0.5,
        allowed_zones=["assembly-cell-3"],
    )

    # 4. Tamper-evident safety record — automatic event logging that travels
    #    with the robot (EU AI Act Art. 12 record-keeping, ISO 10218-2 records).
    log = SafetyEventLog()
    log.append("maintenance", severity="info", details={"action": "calibration"})
    log.append("near_miss", severity="low", details={"zone": "assembly-cell-3"})
    log.append("manual_override", severity="medium", actor="did:web:operator.example.com")
    record = build_safety_record(robot, robot_did=robot_did, summary=log.summarize())

    return [identity, provenance, scope, record]


def main() -> None:
    kp = generate_identity(domain="robot.acme.example.com")
    robot = Signer(private_key=kp.private_key_jwk, did=kp.did)
    assessor = generate_identity(domain="notified-body.example.com")
    assessor_signer = Signer(private_key=assessor.private_key_jwk, did=assessor.did)

    credentials = build_credential_set(robot, kp.did)
    print(f"Assembled {len(credentials)} credentials for {kp.did}\n")

    for profile_id in PROFILE_IDS:
        report = check_conformance(credentials, profile_id)
        status = "CONFORMS" if report["conforms"] else "GAPS"
        print(
            f"=== {report['regime']} ({report['version']}) — {status} "
            f"[{report['satisfiedCount']}/{report['totalCount']}] ==="
        )
        for req in report["requirements"]:
            mark = "PASS" if req["satisfied"] else "MISSING"
            print(f"  [{mark:>7}] {req['clause']}  {req['title']}")

        # An assessor (or the robot itself) signs a point-in-time attestation
        # binding the report by digest, then anyone re-verifies it offline.
        attestation = build_conformance_attestation(
            assessor_signer, robot_did=kp.did, report=report
        )
        ok, subject = verify_conformance_attestation(attestation, assessor.public_key_jwk)
        print(
            f"  signed attestation verifies: {ok}  "
            f"(issuer={attestation['issuer']}, reportDigest={subject['reportDigest'][:16]}...)\n"
        )


if __name__ == "__main__":
    main()
