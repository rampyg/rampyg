# PAD-125: Value-Asserting Conformance Predicates — Closing Null-Evidence Conformance

**Identifier:** PAD-125  
**Title:** Method for Expressing a Regulatory Conformance Requirement as a Predicate That Asserts a Value Over Credential Evidence Rather Than Its Presence, So a Structurally Complete but Semantically Empty Credential Set Cannot Certify as Conformant  
**Publication Date:** August 10, 2026  
**Prior Art Effective Date:** August 10, 2026  
**Status:** Public Disclosure (Defensive Publication)  
**Category:** Robotics / Regulatory Conformance / Verifiable Credentials  
**Author:** Ramprasad Anandam Gaddam  
**License:** Apache 2.0  
**Related:** PAD-079 (Machine-Checkable Regulatory Conformance — **this disclosure supersedes the presence-based predicate of its §3**), PAD-064 (Hardware-Rooted Robot Identity), PAD-065 (Model and Config Provenance), PAD-066 (Physical Capability Scope), PAD-091 (Wear and Degradation Attestation)  

---

## 1. Abstract

A conformance checker that decides a regulatory requirement is satisfied when a
credential of the right type carries the required *fields* can be satisfied by evidence
that is structurally complete and semantically empty. A robot that recorded no safety
events, that reported breaching its operating envelope, and whose identity carries a
hardware-root label but no hardware attestation, satisfies such a checker on every one of
those requirements. This method replaces presence with assertion: each requirement
carries a value predicate over the named field, so the requirement is satisfied only when
the evidence says what the regulation requires it to say.

Key innovations:

- **Requirement as an assertion over evidence, not a test for its presence.** Each
  requirement names a field *and* the predicate its value must satisfy, so a zero count,
  a false conformance flag, or a null measurement no longer satisfies the requirement it
  was meant to evidence.
- **Named failure mode: null-evidence conformance.** A credential-based conformance
  system whose predicates test presence admits an evidence set that is complete in form
  and empty in substance, and certifies it. Naming the class lets any credential-based
  compliance scheme test for it.
- **Co-presence predicates for dependent fields.** A field whose evidentiary value
  depends on a companion field (a hardware-root *kind* without a hardware-root
  *attestation*) is asserted as a dependency, so a label cannot stand in for the proof it
  labels.
- **Determinism and reproducibility preserved.** The predicate is a fixed computation over
  the same inputs, so the report remains reproducible across language implementations and
  bindable by digest exactly as in PAD-079.

---

## 2. Problem Statement

### 2.1 Presence is not evidence

A requirement that asks whether a credential "carries field X" is satisfied by any value
of X, including the values that mean the requirement was *not* met. A safety-record
credential reporting `totalEvents: 0` carries the field the record-keeping requirement
names, and so satisfies it, though it evidences that nothing was recorded.

### 2.2 The failure is silent and points toward compliance

The unsound predicate does not error; it returns satisfied. A checker built this way
reports conformance most confidently in exactly the case where the least evidence exists,
because an empty or degenerate credential set is structurally simple and complete. The
error direction is toward certification, which is the dangerous direction.

### 2.3 A negative measurement satisfies the requirement it contradicts

Where a credential carries a field whose value is itself a conformance verdict — a motion
digest reporting `withinEnvelope: false`, a monitoring flag, a pass/fail result — a
presence test is satisfied by the value that reports non-conformance. The requirement is
then evidenced by its own violation.

### 2.4 A label can impersonate the proof it names

Where a credential carries both a descriptive field and the cryptographic proof that
substantiates it, a predicate over the descriptive field alone is satisfied by an
identity that names a hardware root it never proves possession of.

---

## 3. Solution (The Invention)

Each requirement in a conformance profile carries, alongside the credential type and the
field path it names, an **expectation map**: the predicate the field's value must satisfy
for the requirement to be considered evidenced. The checker evaluates the predicate
against the value, not the key against the object.

Four predicate forms cover the observed failure modes:

- **Minimum-count** — a counted quantity must exceed a floor, so a ledger that recorded
  nothing does not evidence a record-keeping requirement.
- **Required-value** — a field whose value is itself a verdict must hold the conforming
  value, so a reported envelope breach does not evidence continuous monitoring.
- **Dependency** — a named field is evidential only when its substantiating companion
  field is also present, so a hardware-root label without a hardware-root attestation does
  not evidence hardware binding.
- **Presence** — retained for fields where existence genuinely is the evidence (an
  identifier, a digest), so the stricter forms are applied where they carry meaning rather
  than uniformly.

The checker walks the profile as before and returns the same deterministic per-requirement
report, each entry citing its clause; only the satisfaction decision changes. The report
digest, the signed point-in-time attestation, and its digest binding are unchanged from
PAD-079, so the artifact format and its verification are backward compatible while the
decision beneath them becomes sound.

Because the predicate is data carried by the requirement rather than logic in the checker,
a profile author states the assertion at the point the clause is mapped, and every
language implementation evaluates it identically.

---

## 4. Prior Art Differentiation

Schema validation (JSON Schema, SHACL), constraint languages, business-rule engines, and
credential-status checking are prior art. PAD-079 — this project's own earlier
disclosure — is prior art for machine-checkable regulatory conformance over robot
credentials, and its §3 discloses the presence-based predicate this disclosure corrects.
This disclosure does **not** claim conformance checking generally, nor value constraints
generally.

What is differentiated is:

- **The identification of null-evidence conformance as a failure class of
  credential-based compliance systems**: an evidence set complete in structure and empty
  in substance certifying as conformant, with the error directed toward certification.
- **A regulatory requirement expressed as a value assertion bound to the clause it maps
  to**, so the conformance decision tests what the regulation requires the evidence to
  say, not merely that a field of that name exists.
- **A dependency predicate distinguishing a descriptive field from the cryptographic
  proof that substantiates it**, so a label cannot satisfy a requirement that exists to
  compel the proof.
- **Preservation of determinism, cross-language reproducibility, and digest-bound signed
  attestation** while strengthening the predicate, so existing conformance artifacts and
  verifiers remain valid.

Schema validation asserts that a document is well-formed; this asserts that the evidence
substantiates a regulatory clause. The distinction is the whole of the invention: a
credential set can be perfectly well-formed and evidence nothing.

---

## 5. Technical Implementation

A reference design extends each profile requirement with an expectation map naming the
predicate form and its parameter, and evaluates it in the checker before marking a
requirement satisfied. The profiles for ISO 10218-1/-2, ISO/TS 15066, the EU Machinery
Regulation 2023/1230, the EU AI Act high-risk requirements, and UL 3300 carry expectations
on their counted, verdict-valued, and proof-substantiated fields. The report shape, the
report digest, and the conformance attestation are unchanged. The open layer is the
predicate vocabulary and its evaluation.

Implementers of any credential-based compliance scheme are encouraged to test their own
profiles for this class directly: construct an evidence set in which every counted field
is zero, every verdict field reports non-conformance, and every proof field is absent
while its label is present, and confirm the checker refuses it.

---

## 6. Claims Summary

1. A method for deciding regulatory conformance over verifiable credentials in which each
   requirement carries a predicate asserting a property of a named field's value, and the
   requirement is satisfied only when the predicate holds.
2. The method of claim 1 wherein a counted-evidence requirement is satisfied only above a
   stated minimum, so a ledger recording nothing does not evidence record-keeping.
3. The method of claim 1 wherein a field whose value is itself a conformance verdict must
   hold the conforming value, so a reported violation does not evidence the requirement it
   contradicts.
4. The method of claim 1 wherein a descriptive field is evidential only when its
   substantiating cryptographic companion field is also present, so a label does not
   satisfy a requirement for a proof.
5. The method of claim 1 wherein the resulting per-requirement report remains
   deterministic, reproducible across independent implementations, referenceable by
   digest, and embeddable in a signed point-in-time conformance attestation whose
   verification is unchanged.
6. The method of claim 1 applied as a test for null-evidence conformance, wherein a
   conformance profile is validated by confirming that an evidence set that is
   structurally complete and semantically empty is refused.

---

## Prior Art Declaration

This document is published as a defensive disclosure to establish prior art as of
the date above. It supersedes the presence-based satisfaction predicate disclosed in
PAD-079 §3; PAD-079 otherwise stands as published, and its original text is unaltered.
The methods are released under Apache 2.0 and may be freely implemented, to prevent
patenting by any party and to keep them available to the open Vouch Protocol ecosystem
and to the wider verifiable-credential and regulatory-compliance communities.
