# PAD-126: Convention-Ambiguity Conservative Gating — Safe Actuation When a Model's Output Semantics Are Unattested

**Identifier:** PAD-126  
**Title:** Method for Gating a Physical Action Proposed by a Learned Model Whose Output Semantics Are Unattested, by Deciding Against the Conservative Envelope Over All Candidate Interpretations and Binding the Assumed Interpretation Into the Signed Decision Record for Later Re-Adjudication  
**Publication Date:** August 10, 2026  
**Prior Art Effective Date:** August 10, 2026  
**Status:** Public Disclosure (Defensive Publication)  
**Category:** Robotics / Physical Safety / Machine-Learning Integration / Verifiable Credentials  
**Author:** Ramprasad Anandam Gaddam  
**Related:** PAD-065 (Model and Config Provenance), PAD-066 (Physical Capability Scope Attenuation), PAD-069 (Confidential Tamper-Evident Robot Black Box), PAD-091 (Wear and Degradation Attestation)  
**License:** Apache 2.0  

---

## 1. Abstract

A robot driven by a learned vision-language-action model receives a numeric action vector
and converts it into physical quantities — force, speed, aperture — before checking those
quantities against a signed capability scope. That conversion rests on the model's output
*convention*: which element means what, in what units, in which direction, under which
normalization. The convention is documentation. It is not attested, not signed, and not
checkable at run time, yet the safety decision depends on it entirely. Where the
convention is inverted relative to the assumption, the derived quantity inverts, and the
gate permits precisely the action it exists to prevent.

This method treats the model's output semantics as an unattested trust boundary. The gate
enumerates the candidate interpretations, evaluates the safety-relevant magnitude under
each, and decides against the **conservative envelope** — the interpretation least
favourable to permission — so the decision is sound under every candidate. It then binds
the candidate set and the interpretation actually assumed into the signed decision record,
so an auditor can re-adjudicate the decision once the convention is established.

Key innovations:

- **The semantic convention of a learned model's output treated as a trust boundary.**
  The gap between a model's output space and a safety envelope's units is identified as an
  unattested dependency of a physical safety decision, not an integration detail.
- **Decision against the conservative envelope over candidate interpretations.** The
  safety-relevant magnitude is evaluated under every candidate convention and the least
  permissive result governs, so the gate may over-deny but cannot under-deny — the error
  is forced into the safe direction.
- **The assumed interpretation bound into the signed decision record.** The decision
  carries the candidate set and the convention assumed, so the record states what it
  depended on rather than concealing it.
- **Re-adjudication of historical decisions.** Because each record names its assumption,
  establishing the true convention later allows past decisions to be re-evaluated and any
  that were unsound identified, rather than being unrecoverable.

---

## 2. Problem Statement

### 2.1 A safety gate silently inherits an unverified assumption

A capability scope bounds force, speed, and zone. A learned model emits a normalized
vector. Something must map one to the other, and that mapping is written by hand from
documentation, example code, or inference. Nothing in the credential chain attests it. The
gate's soundness therefore rests on an assumption no verifier can check.

### 2.2 The failure mode is inverted and points toward permission

Where a convention is directional — an aperture element in which one extreme means fully
open and the other fully closed — an inverted assumption does not merely perturb the
estimate; it reverses it. The configuration exerting maximum force is scored as exerting
minimum force. The gate does not fail loudly; it permits. A safety mechanism whose
characteristic failure is silent permission is worse than none, because it is trusted.

### 2.3 The assumption is invisible after the fact

A black box that records the decision, the derived quantity, and the verdict does not
record the interpretation under which the quantity was derived. An investigator reading a
permitted action that caused harm cannot determine whether the gate was correct under a
wrong assumption or incorrect under a right one, and cannot re-check the fleet's history
once the convention is settled.

### 2.4 The gap is systemic, not incidental

Every integration of a learned action model with a bounded actuator repeats this mapping,
independently, without attestation. As action models proliferate across heterogeneous
hardware, the number of hand-written, unverified semantic bridges grows with the product
of models and platforms.

---

## 3. Solution (The Invention)

The gate does not resolve the ambiguity; it survives it, and records that it did.

**Enumerate.** For each element of the action vector whose semantics are not attested, the
integration declares the finite set of candidate interpretations it cannot rule out — for
a directional element, the two polarities; for a scale ambiguity, the candidate units or
normalizations.

**Evaluate conservatively.** The safety-relevant physical magnitude is computed under each
candidate. The gate decides against the envelope of those results — for a quantity bounded
above, the pointwise maximum; for one bounded below, the minimum. Because the governing
value is the least favourable to permission, an action admitted by the gate is admissible
under *every* candidate interpretation. The gate may refuse an action that was in fact
safe; it cannot admit one that was in fact unsafe on account of the ambiguity. The
uncertainty is thereby converted from a silent hazard into a bounded, quantifiable loss of
availability.

**Bind the assumption.** The decision record — appended to the tamper-evident black box and
covered by the same signature as the rest of the decision — carries the candidate set
considered, the interpretation assumed as nominal, and the fact that the conservative
envelope governed. The model provenance attestation for the running weights (PAD-065) is
referenced, so the record ties the assumption to the exact model build it was made about.

**Re-adjudicate.** When the convention is later established — by vendor attestation,
controlled commissioning, or observed actuation — the recorded candidate set and nominal
assumption allow every historical decision to be recomputed under the settled convention.
Decisions that were conservative are confirmed; any that would have differed are
identified. A fleet's accumulated history becomes re-checkable rather than
uninterpretable.

Where the convention is subsequently attested, the gate narrows its candidate set to the
attested interpretation and the conservative envelope collapses to the true value,
recovering the availability the conservatism cost. The method therefore degrades to the
ordinary gate as attestation improves, rather than imposing a permanent penalty.

---

## 4. Prior Art Differentiation

Interval arithmetic, worst-case and robust control, conservative approximation under
parameter uncertainty, fail-safe design, runtime verification, safety envelopes, control
barrier functions, and unit-checking type systems are all prior art. This disclosure does
**not** claim conservative bounding under uncertainty generally, nor safety filters
generally, nor unit checking generally.

What is differentiated is:

- **Identifying the semantic convention of a learned model's output as an unattested trust
  boundary of a credential-bounded physical safety decision**, distinct from parameter
  uncertainty in a known model: the quantity is not imprecisely known, its *meaning* is
  unestablished.
- **Applying a conservative envelope across candidate semantic interpretations rather than
  across numeric error bounds**, so soundness is obtained over a discrete set of possible
  meanings rather than a continuous range of possible values.
- **Binding the candidate set and the assumed interpretation into the signed,
  tamper-evident decision record**, so the safety decision discloses the assumption it
  rests on and remains attributable to a specific attested model build.
- **Re-adjudication of historical decisions against a later-established convention**, so an
  unattested assumption produces a recoverable record rather than an unrecoverable one.
- **Graceful collapse to the exact gate once the convention is attested**, so the
  availability cost of conservatism is temporary and tied to the absence of attestation.

Robust control chooses a controller sound across a plant's uncertain parameters; this
chooses an admissibility decision sound across an action vector's uncertain *semantics*,
and signs which semantics it assumed so the choice can be audited and revisited.

---

## 5. Technical Implementation

A reference design declares, per model integration, the candidate interpretation set for
each ambiguous element of the action vector; derives the safety-relevant magnitudes under
each candidate; takes the direction-appropriate envelope; and submits the governing value
to the ordinary physical-capability-scope check (PAD-066). The decision, the candidate set,
the nominal assumption, and a reference to the model provenance attestation (PAD-065) are
appended to the black box (PAD-069) under one signature. A re-adjudication routine
recomputes recorded decisions against a supplied settled convention and reports any that
would have differed.

The method is model-agnostic and applies to any learned policy emitting an action vector
whose element semantics are not cryptographically attested by the model publisher. The
correct long-term remedy is for publishers to attest output semantics alongside weights;
until that exists, this method makes the gap safe and auditable rather than silent.

---

## 6. Claims Summary

1. A method for gating a physical action proposed by a learned model, in which the
   semantics of one or more elements of the model's output are unattested, comprising
   enumerating the candidate interpretations, deriving the safety-relevant magnitude under
   each, and deciding admissibility against the interpretation least favourable to
   permission.
2. The method of claim 1 wherein an action admitted by the gate is admissible under every
   enumerated candidate interpretation, so ambiguity can cause refusal of a safe action but
   cannot cause admission of an unsafe one.
3. The method of claim 1 wherein the candidate set and the interpretation assumed as
   nominal are bound into a signed, tamper-evident decision record covering the same
   decision.
4. The method of claim 3 wherein the decision record references the provenance attestation
   of the exact model build whose output was interpreted.
5. The method of claim 3 wherein historical decision records are recomputed against a
   subsequently established convention, and decisions that would have differed are
   identified.
6. The method of claim 1 wherein, upon attestation of the true convention, the candidate
   set narrows to the attested interpretation and the decision reverts to the exact
   magnitude, recovering availability lost to conservatism.
7. The method of claim 1 wherein the safety-relevant magnitude is bounded above and the
   governing value is the pointwise maximum over candidates, or is bounded below and the
   governing value is the pointwise minimum.

---

## Prior Art Declaration

This document is published as a defensive disclosure to establish prior art as of
the date above. The methods are released under Apache 2.0 and may be freely
implemented, to prevent patenting by any party and to keep them available to the
open Vouch Protocol ecosystem and to the wider robotics and machine-learning-safety
communities.
