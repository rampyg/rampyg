# Cold-start prompt for the new session (scoped to `vouch-protocol/vouch`)

Paste everything below into a fresh Claude Code session whose initial source is
`vouch-protocol/vouch`, with `vouch-robotics-examples.patch` attached.

---

You are working in `vouch-protocol/vouch`. I want to land a robotics-examples
contribution and then extend it. Work on a feature branch and open PR(s) against
`main`; never push to `main` directly.

**Context.** Two runnable `examples/` scripts were already written and tested
against this repo in a previous session but could not be pushed there. They are in
the attached `vouch-robotics-examples.patch` (one DCO-signed commit adding
`examples/robotics_ai_act_evidence_pack.py`,
`examples/robotics_vla_accountability_loop.py`, and two `examples/README.md` index
rows). They compose the existing `vouch.robotics` primitives — no core changes.

**Step 0 — land the base.**
1. `pip install -e .` (or the repo's dev install), then create branch
   `claude/robotics-ai-act-and-vla-accountability-examples`.
2. Apply the patch: `git am vouch-robotics-examples.patch` (if `git am` is awkward,
   the two files + README rows can be recreated — but prefer the patch).
3. Verify: run both examples, run `black --check` and `ruff check` on them, and
   `pytest tests/` to confirm nothing regressed. Fix anything that fails.

Then do the following three tasks. Confirm the plan with me before opening PRs.

**Task 1 — widen the evidence pack.** Extend
`examples/robotics_ai_act_evidence_pack.py` to cover all five built-in profiles in
`vouch/robotics/conformance.py`: `eu-ai-act-high-risk`, `iso-10218`,
`iso-ts-15066`, `eu-machinery-2023-1230`, `ul-3300`. That means building the extra
credentials those profiles require (e.g. `iso-ts-15066` needs a
`RobotHeartbeatCredential` with a `motionDigest` via `MotionCollector`; `ul-3300`
needs a `PerceptionProvenanceCredential`). Print a per-profile CONFORMS/GAPS
summary and sign one conformance attestation per profile. Keep it runnable,
`black`-formatted, and `ruff`-clean.

**Task 2 — add lightweight tests.** Add a small `tests/` module (e.g.
`tests/test_examples_robotics.py`) that imports the two example modules' helper
functions (refactor the examples slightly if needed so logic is importable, not
only under `__main__`) and asserts: every profile reports `conforms == True`, each
signed conformance attestation verifies, the VLA loop denies the over-speed and
out-of-zone actions and allows the safe ones, and `verify_blackbox_chain` passes.
Match the existing tests' style in `tests/`.

**Task 3 — port to the other SDKs.** Reproduce the two examples in each SDK,
respecting that only the reference SDKs carry the producer-side surface:
- **Full port (producer + verify): TypeScript** (`packages/sdk-ts`, add to its
  examples/tests area), **Go** (`go-sidecar/robotics` / its examples), **Rust**
  (`core/vouch-core`, module `robotics`).
- **Verify-side example only: Swift** (`sdks/swift`), **JVM/Kotlin**
  (`sdks/jvm`, `VouchRobotics`), **.NET/C#** (`sdks/dotnet`, `VouchRobotics`),
  **C++** (`sdks/cpp`, `vouch::robotics`) — use each wrapper's curated surface
  (`verify_robot_credential`, `check_conformance` +
  `verify_conformance_attestation`, `check_action`, `verify_passport`, etc.).
- Before writing each port, READ that SDK's actual robotics API and its existing
  example/test conventions — do not assume signatures. Use the shared interop
  vector in `test-vectors/robotics/` where relevant so credentials produced in one
  language verify in another. Build/lint/test each language the way its CI does.

**Task 4 — surface the two capabilities across every content/distribution channel.**
Weave a consistent description of the two new capabilities — (a) the EU AI Act /
ISO conformance **evidence pack**, and (b) the **VLA (Gemini Robotics ER 2)
accountability loop** (provenance-on-load → pre-actuation scope gate → tamper-evident
black box) — into each surface below. Reuse one consistent framing everywhere; keep
each file in its existing format/voice. READ each file first and match its structure.

| Surface | Path(s) to update |
| --- | --- |
| FAQs | `agents-and-skills/FAQ-DRAFT.md` and `website/src/app/faq/faq-data.ts` |
| Help Guides | `agents-and-skills/HELP-GUIDE-DRAFT.md` and `website/src/app/help/help-data.ts` |
| Knowledge base (website AI assistant) | `website-agent/backend/knowledge/robotics.md` (+ `conformance.md`) |
| Claude Skill | `claude-skill/skills/vouch-protocol/SKILL.md` and `reference/robotics.md` |
| OpenAI custom GPT | `openai-gpt/knowledge/vouch-knowledge.md`, `instructions.md`, `conversation-starters.md` |
| Gemini gem | `gemini-gem/knowledge/vouch-knowledge.md`, `instructions.md`, `examples.md` |
| Website demos | `website/src/app/demos/robotics/RoboticsDemos.tsx` (+ module CSS) |
| MCP server | `packages/vouch-mcp` — it exposes **no** robotics tools today; either add robotics verbs (e.g. `check_action`, `verify_conformance`, `verify_robot_credential`) with tests, or, if that's out of scope, document the gap. Confirm with me which. |
| Website | `website/src/app/robotics` (robotics page section) |

Keep the `.md` knowledge/skill/gpt/gem edits in lockstep (they are near-duplicates by
design — the same robotics story is mirrored across them). For the website TSX/TS
changes, build the site (`npm run build` or the repo's command) to confirm they compile.

**PR packaging (confirm with me):** default plan —
- PR #1 = Task 1 + Task 2 (Python evidence pack widening + tests; small, reviewable).
- PR #2 = Task 3 reference-SDK ports (TypeScript / Go / Rust).
- PR #3 = Task 3 wrapper verify-side examples (Swift / JVM / .NET / C++).
- PR #4 = Task 4 content/distribution surfaces (docs-heavy; split website vs.
  knowledge-file vs. MCP-code if it gets large).

Adjust if I say otherwise. Use the DCO sign-off the repo requires and mirror
`.github/PULL_REQUEST_TEMPLATE.md`. Confirm the overall plan before opening any PR.
