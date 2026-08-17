# Vouch for Robotics, Foundational Concepts Social Series

Batch 1: Anchor + Cluster A (Identity and provenance of the machine).
Rules applied: no adverbs, no em-dashes, failure-first, terms glossed, plain language.
X links to github.com/vouch-protocol/vouch (tag @Vouch_Protocol). LinkedIn links to vouch-protocol.com.

---

## Anchor: A robot is an AI agent with a body

**X** (271/280)
> Vouch for Robotics. Part 0.
>
> An AI agent that makes a bad API call corrupts a row. A robot that makes a bad move breaks a bone. Same code, plus a body.
>
> Vouch gives robots the same signed identity it gives agents. 21 capabilities, cross-language.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 0: Why robots need this.
>
> An AI agent that makes a bad API call corrupts a database row. A robot that makes a bad move breaks a bone. Same software, higher stakes, because the agent has a body.
>
> A robot is an AI agent with a body, so every question from the agent world returns with more weight. Who is this machine? What is it allowed to do with its arm? Who authorized that action? What did its sensors see? And when something breaks, can anyone prove what happened?
>
> Vouch answers these for robots on the same foundation as agents: signed credentials that anyone can verify, with no central authority in the loop. The robotics layer ships 21 capabilities, from hardware-bound identity to safety records to bystander consent, on the same eddsa-jcs-2022 credentials as the rest of Vouch. A credential signed on a robot in one language verifies on a controller in another, pinned by shared test vectors.
>
> This series walks through what a robot can prove about itself, its limits, and its history.
>
> First post: how a robot proves it is the machine it claims to be.
>
> vouch-protocol.com
> #Robotics #AIAgents #Safety

---

## Concept 1: Hardware-rooted identity

**X** (278/280)
> Vouch for Robotics. 1: Hardware-rooted identity.
>
> Copy a robot's identity keys onto a cheaper chassis and it passes as real. Software sees no difference.
>
> Vouch binds the robot's identity to a hardware root (a TPM chip). A clone on other hardware fails.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 1: Hardware-rooted identity.
>
> Picture a certified warehouse robot. Someone copies its identity keys onto a cheaper chassis that skipped inspection. It reports for work, and every system treats it as the trusted original. Software credentials on their own cannot catch this, because the copy holds the same keys.
>
> A robot's identity has to be tied to the metal, not to a file.
>
> Vouch binds the robot's software identity to a hardware root of trust: a TPM or secure element, a tamper-resistant chip built into the machine that holds keys no one can extract. The chip signs a binding over the robot's DID and key, and a verifier checks both the credential and that hardware attestation. Move the credential to a different body and the hardware signature stops matching, so the clone fails.
>
> The same RobotIdentityCredential carries a lifecycle record: make, commission, transfer, decommission. The machine's whole history travels with its identity.
>
> Next post: proving which model and safety policy the robot runs.
>
> vouch-protocol.com
> #Robotics #Security #Identity

---

## Concept 2: Model and config provenance

**X** (276/280)
> Vouch for Robotics. 2: Model provenance.
>
> After an incident: which model and safety policy was running? An update could swap either, no trace.
>
> Vouch signs the model, weights hash, and safety policy, re-signed on each update as a tamper-evident chain.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 2: Model and config provenance.
>
> A robot hurts someone. The investigation asks a basic question: which model was driving, and what safety policy did it carry? The vendor pushed three over-the-air updates last month. Nobody can say which brain and which limits were in place at the moment it happened.
>
> The software running a robot changes across its life, and each change alters what the machine will do. The record of what it runs has to be as accountable as the actions themselves.
>
> Vouch has the builder sign a ModelProvenanceAttestation: the model name, a hash of the exact weights, the safety policy, and a hash of the runtime config. Each update is re-signed and points to the version it replaces (the field is called supersedes), so the updates form a tamper-evident chain you can walk. A hash is a short fingerprint of a file, so a changed weight or a changed config breaks the match.
>
> That leaves one signed, checkable answer to "which model and which limits were running," for any point in the robot's history.
>
> Next post: hard limits on force and speed before the arm moves.
>
> vouch-protocol.com
> #Robotics #AISafety #Provenance

---

## Concept 3: Built to outlast its own cryptography (post-quantum)

**X** (278/280)
> Vouch for Robotics. 3: Outlasting the crypto.
>
> A robot fielded this year runs 10 to 20 years. Ed25519 may not stay safe that span.
>
> Vouch signs credentials with two proofs: Ed25519 and post-quantum ML-DSA-44. Both must verify, so one break is not fatal.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 3: Built to outlast its own cryptography.
>
> A robot that ships this year can run for 10 to 20 years. That is a problem for its signatures. Ed25519, the signing method it uses, is strong against the computers we have. It may not survive a quantum computer (a new kind of machine that can break some of today's cryptography) that arrives inside the robot's service life. A robot whose signatures can be forged is a robot whose identity and whose logs can be faked.
>
> You cannot re-sign a fleet of robots in the field on short notice, so the protection has to sit in the credential from day one.
>
> Vouch gives robot credentials a proof set: an Ed25519 proof and an ML-DSA-44 proof (the post-quantum signing method NIST selected) over the same document. Each proof verifies on its own, and both must verify for the credential to pass. The credential is as strong as Ed25519 while Ed25519 holds, and stays safe once it does not. A fleet moves to the proof set without breaking the credentials in the field, and migrate_to_pq re-signs an older credential under a post-quantum key.
>
> Next post: one AI mind that moves from one robot body to another.
>
> vouch-protocol.com
> #Robotics #PostQuantum #Cryptography

---

## Concept 4: One mind, many bodies (cross-embodiment continuity)

**X** (278/280)
> Vouch for Robotics. 4: One mind, many bodies.
>
> An AI agent can move from one robot body to another. Is it the same accountable agent, and not driving two at once?
>
> Vouch links each body into a chain the agent signs, plus a check that blocks two at once.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 4: One mind, many bodies.
>
> Software agents are not tied to one machine. The same AI "mind," with its own Vouch identity, can drive robot body A in the morning and robot body B in the afternoon. Two questions follow. After the swap, is this the same accountable agent, or a different one wearing the same name? And is one agent driving two bodies at the same time, hidden behind a single identity, doubling its reach while it looks like one?
>
> Identity for a mind that moves needs a thread that survives the move.
>
> Vouch has the agent sign an embodiment credential each time it takes a body, binding the agent to that body and that body's hardware root for a window. verify_continuity_chain walks the sequence, confirms every link carries the same agent key, and confirms each new body continues from the one before it, returning the body in use. check_no_fork confirms no two embodiments place the agent in different bodies with overlapping windows. This is the mirror image of an ownership chain of custody: in that case, one body passes between owners; in this one, one mind passes between bodies.
>
> Next post: the safe envelope that caps force and speed before the arm moves.
>
> vouch-protocol.com
> #Robotics #AIAgents #Identity
