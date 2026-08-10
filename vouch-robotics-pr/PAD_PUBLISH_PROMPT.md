# Prompt — publish PAD-125 and PAD-126 to `vouch-protocol/vouch`

Paste into a session whose initial source is **`vouch-protocol/vouch`**, with
`pad-125-126.patch` attached.

---

You are working in `vouch-protocol/vouch` on top of `main`. I have two defensive
publications ready to land, supplied as the attached `pad-125-126.patch` (one DCO-signed
commit, 4 files, +428 lines).

**STOP — clearance gate before you publish anything.**

This repo's own process (`strategy/06-build-status-and-plan.md` in the private `aign` repo,
and prior practice) requires that a PAD be checked against
`docs/patents/patent-briefs-confidential.md` — the reserved-for-patent inventions — before
publication. That path is **gitignored and local-only**.

- If `docs/patents/patent-briefs-confidential.md` is readable in your working tree: read it
  and confirm neither disclosure below collides with a reserved invention.
- If it is NOT readable (you are in a remote container): **do not publish. Ask me to run the
  check and confirm**, then proceed.

Apply this specifically to **PAD-126**, which is the novel one and therefore the likeliest
collision. PAD-125 is near-zero risk — it corrects a method already published in PAD-079.
Publication is irreversible and destroys patentability of anything it discloses.

**What the patch contains**

- `docs/disclosures/PAD-125-value-asserting-conformance-predicate.md` — supersedes the
  presence-based satisfaction predicate of PAD-079 §3, which admits *null-evidence
  conformance*: a structurally complete but semantically empty credential set (zero-event
  safety record, envelope-breach motion digest, hardware-root label with no attestation)
  satisfies the requirements it was meant to evidence. Specifies four predicate forms
  (minimum-count, required-value, dependency, presence).
- `docs/disclosures/PAD-126-convention-ambiguity-conservative-gating.md` — gating a physical
  action proposed by a learned model whose output semantics are unattested: decide against
  the conservative envelope over all candidate interpretations (may over-deny, cannot
  under-deny), bind the candidate set and assumed interpretation into the signed decision
  record, and re-adjudicate historical decisions once the convention is established.
- `docs/disclosures/PAD-079-...md` — a dated editorial note pointing to PAD-125. **The
  original text is deliberately unaltered** to preserve the integrity of its 2026-07-04
  prior-art date. Do not "tidy" it.
- `docs/disclosures/README.md` — index rows and an August 10, 2026 section.

**Steps once cleared**

1. `git checkout -b claude/pad-125-126-conformance-and-convention-gating`
2. `git am pad-125-126.patch`
3. Sanity-check: both new files render, the README table rows point at the right filenames,
   and the PAD-079 note is present with its original §3 text intact.
4. `git push -u origin claude/pad-125-126-conformance-and-convention-gating`
5. Open a PR against `main` mirroring `.github/PULL_REQUEST_TEMPLATE.md`. Type of change:
   Documentation. In the body, state plainly that PAD-125 supersedes PAD-079 §3 and that
   PAD-079's original text is intentionally preserved.

**Follow-on work (confirm with me before starting).** PAD-125 documents the corrected
predicate; verify that `vouch/robotics/conformance.py` and its TypeScript, Go, Rust, and
wrapper-SDK counterparts actually implement all four predicate forms as described,
including the **dependency** form (a `hardwareRoot.kind` present without
`hardwareRoot.attestation` must NOT satisfy a hardware-binding requirement). PR #390 fixed
three specific defects; confirm the general forms are implemented, not just those three
instances. If any gap exists, report it before changing code — a cross-language predicate
change has wide blast radius across the eight SDK test suites.
