# PR: Add robotics examples — EU AI Act evidence pack and VLA accountability loop

**Target:** `vouch-protocol/vouch`  ←  branch `claude/robotics-ai-act-and-vla-accountability-examples`
**Base:** `main`

> These files were built and tested against a fresh clone of `vouch-protocol/vouch`
> (both examples run, `black`-formatted, `ruff`-clean). They could not be pushed
> from the session that generated them because that session was scoped to
> `rampyg/rampyg` only. Apply the patch (or copy the two files) from a session/checkout
> that can push to `vouch-protocol/vouch`, then open the PR with the body below.

---

## Suggested PR title

```
Add robotics examples: EU AI Act evidence pack and VLA accountability loop
```

## Suggested PR body (fills the repo template)

### Description

Two runnable `examples/` scripts showing how the existing `vouch.robotics`
credentials compose end to end for a robot driven by a vision-language-action
"brain" (e.g. Gemini Robotics ER 2). No core changes — examples and one docs
index row only.

### Type of Change

- [x] Documentation update
- [x] New feature (non-breaking) — new runnable examples

### Changes Made

- `examples/robotics_ai_act_evidence_pack.py` — assembles a robot's hardware-rooted
  identity, model/config provenance, physical capability scope, and tamper-evident
  safety record, runs `check_conformance` against `eu-ai-act-high-risk` and
  `iso-10218`, and signs + verifies a `RobotConformanceAttestation` over the
  deterministic report (clause-by-clause output).
- `examples/robotics_vla_accountability_loop.py` — wraps a VLA brain: signs a
  `ModelProvenanceAttestation` on model load, gates each proposed action against the
  physical capability scope *before* actuation, and records every allow/deny decision
  to an encrypted, tamper-evident black box (`verify_blackbox_chain` at the end).
- `examples/README.md` — index rows for both.

### Testing

- [x] Both examples run clean (`python examples/robotics_ai_act_evidence_pack.py`,
  `python examples/robotics_vla_accountability_loop.py`).
- [x] `black examples/…` formatted; `ruff check examples/…` passes.
- [x] Additive only — no changes under `vouch/` or `tests/`.

### Checklist

- [x] Follows project code style (black + ruff)
- [x] Docs updated (examples index)
- [x] Commits signed off (DCO)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01Jmk45Y6oAxCHwHrxRjmb35
