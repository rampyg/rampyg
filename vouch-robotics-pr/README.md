# Robotics examples staged for a `vouch-protocol/vouch` PR

This folder holds a finished, tested contribution for **`vouch-protocol/vouch`**
that could not be pushed directly because this session is scoped to `rampyg/rampyg`.

## Contents

| File | What it is |
| --- | --- |
| `robotics_ai_act_evidence_pack.py` | Example: assemble a robot's credentials → `check_conformance` (EU AI Act + ISO 10218) → signed, verifiable `RobotConformanceAttestation`. |
| `robotics_vla_accountability_loop.py` | Example: wrap a VLA brain (Gemini Robotics ER 2) — sign model provenance on load, gate each action against the physical scope before actuation, log every decision to a tamper-evident black box. |
| `vouch-robotics-examples.patch` | `git format-patch` of the single commit (both examples + `examples/README.md` index rows), DCO-signed. |
| `PR_BODY.md` | Ready-to-paste PR title + body (fills the repo template). |

Both scripts were verified against a fresh clone of `vouch-protocol/vouch`:
they run, are `black`-formatted, and pass `ruff check`.

## To land it (from a checkout that can push to `vouch-protocol/vouch`)

```bash
# from the root of a vouch-protocol/vouch checkout on an up-to-date main
git checkout -b claude/robotics-ai-act-and-vla-accountability-examples
git am /path/to/vouch-robotics-examples.patch      # applies the exact signed commit
git push -u origin claude/robotics-ai-act-and-vla-accountability-examples
# then open the PR against main using PR_BODY.md
```

If `git am` is inconvenient, just copy the two `.py` files into `examples/` and add
the two index rows to `examples/README.md` (see `PR_BODY.md`).

## Cleaner alternative

Start a new Claude Code session with **`vouch-protocol/vouch`** as the initial
source; from there the branch push + PR can be done directly, no patch needed.
