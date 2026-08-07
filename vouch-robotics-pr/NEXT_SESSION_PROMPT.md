# Cold-start prompt #2 — C/WASM ports + the four parallel adoption steps

Paste into a fresh Claude Code session whose **initial source is `vouch-protocol/vouch`**.
(No attachment needed this time — everything referenced is already on `main`.)

---

You are working in `vouch-protocol/vouch`, on top of `main` (which already contains
PRs #381–#384: the robotics evidence pack across all five conformance profiles, the
VLA accountability loop, ports to TypeScript/Go/Rust, verify-side examples for
Swift/JVM/.NET/C++, the content-surface rollout, and four `robot_*` MCP tools).

Read these first so the new work matches what already exists:
`examples/robotics_ai_act_evidence_pack.py`, `examples/robotics_vla_accountability_loop.py`,
`tests/test_examples_robotics.py`, `vouch/robotics/conformance.py`, and
`sdks/cpp/examples/robotics_verify_example.cpp`.

There are **five independent tasks below**. They do not depend on each other — run
them in parallel (separate worktrees/branches), and open **one PR per task** against
`main`. Confirm the overall plan with me before opening any PR. Use the repo's DCO
sign-off and mirror `.github/PULL_REQUEST_TEMPLATE.md`. Do not push to `main`.

---

## Task A — C and WASM robotics examples

These are the two SDK surfaces the earlier ports skipped. Both **already expose
robotics symbols**; the work is examples/tests that exercise them, mirroring existing
patterns. Note there is **no `sdks/c/`** — the C ABI lives in `sdks/cpp/`.

**C** (`sdks/cpp/include/vouch_core.h`, pattern: `sdks/cpp/examples/example.c` and
`robotics_verify_example.cpp`, built via `sdks/cpp/examples/Makefile`).
Available symbols are narrower than the reference SDKs — 18 total, notably:
`vouch_robotics_mint_identity`, `vouch_robotics_verify_identity`,
`vouch_robotics_check_action`, `vouch_robotics_check_conformance`,
`vouch_robotics_build_conformance_attestation`,
`vouch_robotics_verify_conformance_attestation`,
`vouch_robotics_verify_robot_credential`, `vouch_robotics_verify_passport`,
`vouch_robotics_sign_pq`. So write a **trimmed evidence-pack + action-gate example**:
mint a hardware-rooted identity, check a safe and an unsafe action against a physical
scope, run `check_conformance`, then sign and verify a conformance attestation.
Free every returned string with `vouch_string_free` (see `example.c`), and add the
target to the existing Makefile.

**WASM** (`core/wasm/src/lib.rs`, pattern: `core/wasm/smoke.mjs`, built by
`core/wasm/build-npm.sh`). WASM exposes the **full producer surface**
(`robotics_build_*`, `robotics_blackbox_append`, `robotics_attenuates`, …), so port
**both** examples — the evidence pack and the VLA accountability loop, including the
black-box chain check and the tamper-detection case. Follow `smoke.mjs` conventions
(the `ok(name, cond)` PASS/FAIL harness, the Node RNG polyfill, fixed seeds from
`test-vectors/` where an RNG would otherwise be needed).

Verify each builds and runs the way its CI does before opening the PR.

## Task B — ROS 2 node (highest-leverage item)

Package the accountability loop as a **ROS 2 node**, so adding Vouch to a robot is one
dependency rather than a demo someone chooses to run. Nothing ROS exists in the repo
yet — you are creating it (suggest `integrations/ros2/` unless the repo layout implies
better; check `go-sidecar/` and `vouch/integrations/` for house conventions first).

The node should sit between a planner and the actuators:
- subscribe to a proposed-action topic; gate each action with `check_physical_action`
  against a `PhysicalCapabilityScope` before it reaches the actuators;
- republish only allowed actions, and publish deny reasons on a separate topic;
- sign a `ModelProvenanceAttestation` on startup recording the planner/model in use;
- append every allow/deny decision to a `BlackBoxLog`;
- expose the scope, key material, and topic names as ROS parameters.

Target ROS 2 Humble or Jazzy (state which, and why, in the PR). Include a package
manifest, a launch file, a minimal README with `colcon build` + run instructions, and
at least one test that does not require a physical robot. If a full ROS toolchain is
not installable in this environment, still write the complete package and say plainly
in the PR what you could and could not execute — do not claim it was verified if it
was not.

## Task C — regulatory gap-map (research, not code)

`vouch/robotics/conformance.py` self-describes its profiles as "a reference crosswalk,
not legal advice." Close that gap so the profiles can withstand a notified body.

For each of the five profiles, walk **every** `_req(...)` entry against the current
published text of the regulation/standard it cites (EU AI Act Reg (EU) 2024/1689; ISO
10218-1/-2; ISO/TS 15066; EU Machinery Reg 2023/1230; UL 3300). For each requirement
record: the exact clause/article, whether the cited credential genuinely evidences it,
and any requirement of the regime that Vouch **does not** cover at all.

Deliver `docs/robotics-conformance-crosswalk.md`: a per-profile table of
clause → credential → evidence strength (full / partial / none) → notes, plus an
explicit "what Vouch does not cover" section per regime. Where a mapping is thin or
missing, propose the concrete `_req(...)` additions (or new credential types) that
would close it — propose in the doc; only change `conformance.py` where a mapping is
clearly wrong or clearly missing, and call out every such change in the PR.

Be rigorous about sources: cite the actual regulation text you consulted, and where
you cannot access a paywalled standard (ISO texts are not free), say so explicitly per
clause rather than inferring the content. Flag anything uncertain rather than
asserting it — an overstated compliance claim is worse than an acknowledged gap.

## Task D — drive the loop with a real VLA runtime

`examples/robotics_vla_accountability_loop.py` is driven by a hardcoded action list.
Replace that with a **real** vision-language-action model so the demo shows a live
model being gated, not a script. Use **OpenVLA** (open weights, easiest path).

Add `examples/robotics_openvla_gated_loop.py` (plus any `requirements` note): load the
model, take its proposed actions, map them into `PhysicalAction`, and run them through
the same provenance → scope-gate → black-box pipeline. Record the real weights hash in
the `ModelProvenanceAttestation` rather than a placeholder. Keep the existing scripted
example untouched — this is an addition, not a rewrite.

Gate heavy dependencies behind an optional extra and skip cleanly when the model is
unavailable, so CI does not try to download weights. If you cannot actually run the
model here, structure the code correctly, mark it clearly as unverified in the PR, and
say exactly what remains to be checked on a machine with the weights.

## Task E — assessor-facing one-pager

Produce the material for a first conversation with an insurer or notified body
(the conversation itself is mine to have; you are preparing what I bring to it).

Add `docs/robotics-evidence-pack-for-assessors.md`, written for a compliance/risk
reader rather than an engineer: what the evidence pack is, what each of the six
credentials attests, exactly how the recipient verifies the artifact themselves
(offline, no trust in us), what it does **not** prove, and the honest maturity
statement — open reference implementation, crosswalk not legal advice. Include the
real terminal output of the evidence-pack example as the worked artifact. Keep it to
roughly two pages, and do not overclaim: the value proposition is reproducible
evidence, not certification.

---

**A note on scope:** Tasks A, B, D are code; C and E are writing/research. If your
environment cannot build ROS 2 (B) or run OpenVLA weights (D), complete everything
else in full and report precisely what was not executed — never report unverified work
as verified.
