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

---

# Cluster B: Keeping physical actions inside safe limits

## Concept 5: Physical limits that hold before the arm moves

**X** (274/280)
> Vouch for Robotics. 5: Physical limits that hold.
>
> A robot arm can be safe by a wall and dangerous by a person. A config file cannot stop it.
>
> Vouch puts the limits (force, speed, zones, a human cap) in a signed credential, checked before each move.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 5: Physical limits that hold before the arm moves.
>
> An industrial arm runs at a speed that is fine facing a wall and harmful facing a coworker. The safe speed lives in a config file the software reads. A bad update, a bug, or a tampered value, and the arm swings at full speed with a person in reach.
>
> For a machine that can hurt someone, its limits cannot be a suggestion in software. They have to be signed, and checked at the last moment before motion.
>
> Vouch carries the limits in a PhysicalCapabilityScope credential: max force, max speed, a lower speed cap near humans, allowed zones, and shift windows. The robot checks a proposed action against this scope before actuation, the instant a motor is about to move, and refuses an action outside it. When one robot hands authority to another, a delegated scope can attenuate, meaning it can shrink the limits, not widen them.
>
> The result: the ceiling on force and speed is a signed rule the robot enforces on itself, not a line in a config that anyone can edit.
>
> Next post: making that trust decay unless the robot keeps proving it stays in bounds.
>
> vouch-protocol.com
> #Robotics #AISafety #Security

---

## Concept 6: Trust that decays unless the robot keeps earning it

**X** (277/280)
> Vouch for Robotics. 6: Trust that must be renewed.
>
> Grant a robot trust one time and it holds as it drifts out of bounds. Nobody watches between checks.
>
> The robot signs a motion summary each interval. It is trusted while a fresh, in-bounds one exists.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 6: Trust that decays unless the robot keeps earning it.
>
> A robot passes its morning safety check and gets marked trusted. By afternoon a worn joint has it exceeding its speed near people. Its status reads trusted, because trust was stamped one time and was not revisited. The gap between check-ups is a blind spot.
>
> Trust for a moving machine should reflect the last minute, not the last inspection.
>
> Vouch has the robot self-sign a RobotHeartbeatCredential each interval, carrying a motion digest: a short summary of its peak force, peak speed, peak speed near humans, and any zone breaches over that window, plus whether it stayed inside its PhysicalCapabilityScope. A verifier treats the robot as trusted while a fresh, in-envelope heartbeat exists, and drops trust the moment one is missing or out of bounds. This inverts the usual model from "trusted until someone revokes it" to "untrusted until it renews."
>
> The result: a robot proves it is behaving, minute by minute, and loses standing the moment it stops.
>
> Next post: shrinking a robot's limits as it wears out.
>
> vouch-protocol.com
> #Robotics #AISafety #ContinuousTrust

---

## Concept 7: Limits that tighten as the robot wears

**X** (280/280)
> Vouch for Robotics. 7: Limits that tighten as it ages.
>
> A five-year-old robot with worn joints runs at its factory limits. The safe envelope did not move with it.
>
> Vouch has the robot sign its wear level, and lowers its force and speed caps as wear rises.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 7: Limits that tighten as the robot wears.
>
> A robot leaves the factory rated for a certain force and speed. Five years in, its actuators are worn and its sensors drift, but it operates at the day-one limits, because those numbers were fixed at manufacture. A machine less able than it was runs with the same authority it had when new.
>
> The safe envelope should track the machine's real condition, not its spec sheet.
>
> Vouch has the robot sign a RobotWearAttestation carrying a wear level from 0 (new) to 1 (spent), with optional detail metrics, bound to its identity. Each attestation links to the one before it, so verify_wear_chain walks a tamper-evident wear history. attenuate_for_wear derives a physical scope whose numeric caps are scaled by (1 minus the wear level), and the result is a valid narrowing of the original scope, so the same limit check the rest of Vouch uses carries the derating.
>
> The result: an aging robot operates inside a tighter, signed envelope than the one it shipped with, and the tightening is on the record.
>
> Next post: a cryptographic two-person rule for high-risk actions.
>
> vouch-protocol.com
> #Robotics #AISafety #PredictiveMaintenance

---

## Concept 8: A cryptographic two-person rule

**X** (280/280)
> Vouch for Robotics. 8: A two-person rule, in crypto.
>
> One operator, or one stolen key, should not launch a high-risk robot action on their own.
>
> Vouch requires M of N approvers to each sign the same action. Duplicate signatures cannot reach the threshold.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 8: A cryptographic two-person rule.
>
> A single command sends a heavy robot into a weld, a lift, or a move that could injure someone if it is wrong. One operator issues it. One account, one key. If that account is careless or stolen, a single party can trigger a high-consequence physical action, and there is no second check.
>
> High-risk moves in the physical world call for the same discipline as a nuclear launch or a large wire transfer: more than one hand on the decision.
>
> Vouch expresses this as a physical quorum. A high-consequence action is authorized when at least M of an attested set of N approvers have each signed an approval over the same action (quorum means the minimum number of approvers required). verify_action_authorization counts the distinct valid approvers, so one approver cannot pad the count with duplicate signatures. Fall short of the threshold, and the robot does not act.
>
> The result: dangerous actions need a real quorum of people, proven in signatures, not a single click.
>
> Next post: proving what a robot's sensors saw.
>
> vouch-protocol.com
> #Robotics #AISafety #Security

---

# Cluster C: Proof of what happened

## Concept 9: Proof of what the robot saw

**X** (278/280)
> Vouch for Robotics. 9: Proof of what it saw.
>
> After a crash, was the feed the robot acted on real, or edited after the fact?
>
> Vouch has the robot sign each frame's fingerprint at capture, hash-linked in order. A swapped or edited frame breaks the chain.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 9: Proof of what the robot saw.
>
> A delivery robot runs into someone and the footage shows a clear path. Was that the feed the robot acted on, or a clip pulled from a different moment, or edited after the incident? A camera file on its own carries no proof of when it was taken or by which machine.
>
> If a robot's decisions rest on what it perceives, the perception itself has to be provable.
>
> Vouch has the robot sign the provenance of each captured sensor frame at the moment of capture: a record binding the frame's hash (a short fingerprint of the exact image or scan), the sensor id, the modality (camera, lidar, radar, depth, audio, thermal), the capture time, and the robot's DID. The records hash-link in order into a PerceptionLog, so the sequence of what the robot saw is tamper-evident, and a swapped, dropped, or edited frame breaks the chain. The store holds the fingerprints, not the raw frames, so holding the actual frame lets a verifier recompute its hash and confirm the match.
>
> The result: a robot can prove what its sensors captured and when, and a doctored feed does not hold up.
>
> Next post: proving the fused world model behind a decision used the real inputs.
>
> vouch-protocol.com
> #Robotics #Provenance #AISafety

---

## Concept 10: Proof the fused world model is honest

**X** (279/280)
> Vouch for Robotics. 10: Proof the world model is honest.
>
> A robot fuses camera, lidar, and radar into one view and acts on it. Fake an input, the view lies.
>
> Vouch binds the fused view to its input frames, and flags any input missing from the signed log.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 10: Proof the fused world model is honest.
>
> Post 9 signed each raw sensor frame. But a robot does not act on single frames. It fuses many, from cameras, lidar, and radar, into one world model, an object map, or an occupancy grid, and acts on that combined view. If one input is dropped or swapped on the way into the fusion, the robot's picture of the world is wrong, and the raw-frame signatures do not catch it.
>
> The combined view a robot acts on has to commit to the exact inputs that built it.
>
> Vouch signs a FusedPerceptionAttestation that binds the fused output's hash to an ordered list of the input frame hashes, a digest over those inputs, and a fusion method identifier. verify_fused_attestation checks the robot's signature, reproduces the input digest so the attestation commits to those inputs, and, given the raw fused output, reproduces its hash. verify_fusion_inputs checks each named input against the robot's signed perception log and returns any that were absent, so a manipulated fusion result or a dropped input is caught.
>
> The result: the world model behind a decision is tied to the real, signed sensor data that produced it.
>
> Next post: the encrypted black box and a kill switch only an authority can pull.
>
> vouch-protocol.com
> #Robotics #Provenance #AISafety

---

## Concept 11: The black box and the kill switch

**X** (276/280)
> Vouch for Robotics. 11: Black box and kill switch.
>
> After an incident, the logs are gone or edited. And a spoofed 'stop' could halt a fleet.
>
> Vouch gives robots an encrypted, tamper-evident recorder, plus a kill switch limited to attested authorities.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 11: The black box and the kill switch.
>
> Two failures live at the ends of an incident. After a crash, the log that would explain it is missing or rewritten. And in the moment of danger, an emergency stop depends on its authenticity: a forged stop command could halt a production line, and a real one could be dismissed as fake.
>
> A robot needs a record no one can rewrite, and a stop no one can forge.
>
> Vouch gives it both. The black box is an append-only, encrypted (AES-256-GCM), hash-linked flight recorder: the payloads stay confidential, the chain is tamper-evident without the key, and the head can be signed to anchor the log, so anyone can prove the record is intact, while its contents stay readable to key-holders. The kill switch is a verifiable emergency-stop credential; with an authority allowlist, an attested authority is the one party that can trigger it, and its trigger is provable after the fact.
>
> The result: the record survives the incident, and the emergency stop is a signed act, not a spoofable signal.
>
> Next post: a safety ledger a robot cannot understate.
>
> vouch-protocol.com
> #Robotics #AISafety #Security

---

## Concept 12: A safety record that cannot be shrunk

**X** (272/280)
> Vouch for Robotics. 12: A safety record that cannot shrink.
>
> Before an audit, incident and near-miss counts are easy to trim.
>
> Vouch keeps a hash-linked ledger of safety events and a signed summary. It cannot undercount without breaking the chain.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 12: A safety record that cannot be shrunk.
>
> An operator preparing for a regulator wants clean numbers. The robot's incidents, near-misses, manual overrides, and envelope breaches sit in a log that the same operator controls. Trimming a few entries before the audit is a quiet edit, and the summary handed to the regulator is no more honest than the person compiling it.
>
> A safety summary is worth trusting when it cannot understate the events beneath it.
>
> Vouch keeps safety events in an append-only, hash-linked ledger: incident, near-miss, manual override, kill-switch trigger, envelope breach, each with a severity. build_safety_record produces a portable RobotSafetyRecordCredential that summarizes the ledger into counts by type and severity, the period, and the ledger head hash that anchors it. Because the summary is bound to that head, it cannot report fewer events than the ledger holds without breaking the chain, and a broken chain is visible to any verifier.
>
> The result: the number a regulator sees is tied to a tamper-evident log, so an understated safety record gives itself away.
>
> Next post: tracing a damaged package to the exact hop that broke it.
>
> vouch-protocol.com
> #Robotics #Compliance #AISafety

---

## Concept 13: Tracing damage to the hop that caused it

**X** (276/280)
> Vouch for Robotics. 13: Who broke the package?
>
> A tote passes through pickers, robots, and conveyors, and arrives damaged. Each party blames the next.
>
> Vouch signs each custody handoff with the item's condition, so an incident traces to the exact hop.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 13: Tracing damage to the hop that caused it.
>
> A tote moves from a human picker to a mobile robot to a sorting arm to a truck. It arrives crushed. Every handler says it was fine when they passed it on. With no signed record of each transfer, the damage is a whodunit, and the cost lands on whoever has the weakest case.
>
> When custody of a physical thing passes across many hands, human and robot, each handoff needs to be on the record.
>
> Vouch records each transfer as a CustodyHandoffCredential: the receiving actor signs that it accepted custody of the task or object from the releasing actor, with an attested condition (intact, damaged). verify_handoff_chain walks the sequence, where each receiver becomes the next releaser, and returns the current holder; holder_at returns who held the item at a given time. locate_condition_change compares the attested conditions and pins a state change (intact to damaged) to the holder responsible for it.
>
> The result: a damaged-goods dispute becomes a signed chain, and the break localizes to one hop and one actor.
>
> Next post: two robots from different vendors proving trust before they cooperate.
>
> vouch-protocol.com
> #Robotics #Provenance #Logistics

---

# Cluster D: Trust between machines and the world

## Concept 14: Robots that vet each other before they cooperate

**X** (268/280)
> Vouch for Robotics. 14: Robots that vet each other.
>
> Two robots from rival vendors must cooperate. How does each know the other is not a spoof?
>
> Vouch runs a signed handshake that checks identity and bounds the shared scope to what both grant.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 14: Robots that vet each other before they cooperate.
>
> Two robots from two vendors meet on a job: one lifts, one welds. To work together they exchange commands. But neither built the other, and neither should take the other's word for who it is or what it may do. A spoofed peer, or one reaching past its remit, turns a joint task into a hazard.
>
> Machines from different owners need a way to authenticate and to bound what they will do together, with no shared master key.
>
> Vouch defines a robot-to-robot handshake: three signed messages, HELLO, ACCEPT, and CONFIRM. The responder checks the initiator's domain (its owner's identity space) against its own TrustPolicy, and intersects the scope the initiator proposes with the scope it is willing to offer, so the agreed session scope is no broader than what either side grants on its own. Each side verifies the other's signatures before the work starts.
>
> The result: two machines with no prior contact establish a bounded, mutual trust, and a rogue or over-reaching peer is turned away.
>
> Next post: giving a robot the right to open a door without handing it a key.
>
> vouch-protocol.com
> #Robotics #Security #MultiAgent

---

## Concept 15: Opening the door without handing over a key

**X** (280/280)
> Vouch for Robotics. 15: Open the door, no shared key.
>
> A robot must open doors, call elevators, dock at chargers. A shared master key cannot scale or stay safe.
>
> An operator signs a scoped grant; the door checks the robot's signed request with no network.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 15: Opening the door without handing over a key.
>
> A fleet of robots in a hospital has to open doors, call elevators, and dock at chargers. The blunt fix is a shared credential every robot carries. One leak, and every door in the building is open to whoever holds it, with no way to tell which robot did what.
>
> A robot should prove it is allowed through a specific door, without a key that opens every other door as well.
>
> Vouch splits it into a grant and a request. An infrastructure operator signs an InfrastructureAccessGrant naming the resource, the permitted operations, an optional zone, and a time window. The robot signs an InfrastructureAccessRequest for one operation on one resource. The resource runs authorize_access with no network call and allows the operation when the grant verifies under the operator key and is in its window, the request verifies under the robot key, the two name the same robot and resource, and the operation is permitted. attenuates_grant confirms a sub-grant narrows what it inherits.
>
> The result: the grant plus the request is a tamper-evident, attributable record of the access, and there is no master key to leak.
>
> Next post: bounded authority for a robot with no signal at all.
>
> vouch-protocol.com
> #Robotics #Security #Infrastructure

---

## Concept 16: Bounded authority for a robot with no signal

**X** (280/280)
> Vouch for Robotics. 16: Authority with no signal.
>
> A robot in a mine or tunnel has no signal, but needs bounded, time-limited authority.
>
> Vouch issues a signed lease that bounds its scope for a set window. The robot verifies and acts with no network call.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 16: Bounded authority for a robot with no signal.
>
> Inspection robots work where there is no connectivity: down a mine, inside a pipeline, in a field far from any tower. They cannot phone home to check what they are allowed to do. The lazy answer is to give a disconnected robot broad standing authority and hope, which is a poor candidate for a blank check.
>
> Authority that survives offline has to be bounded and short-lived.
>
> Vouch issues a DelegationLeaseCredential: an authority signs a grant that bounds the robot's physical capability scope, including allowed zones, for a fixed window. The robot verifies the signature, that the window is current, and that a proposed action fits the scope, with no network call. Leases nest, and each sub-grant narrows the one above it, which forms an open cross-vendor chain of shrinking authority.
>
> The result: a robot cut off from the network acts inside signed, time-boxed, shrink-only limits it can check on its own.
>
> Next post: a scannable passport a person can verify with no network.
>
> vouch-protocol.com
> #Robotics #Security #EdgeComputing

---

## Concept 17: A passport a person can scan and verify offline

**X** (277/280)
> Vouch for Robotics. 17: A passport you can scan.
>
> A robot shows up at a dock. The guard cannot check who owns it or what it may do, with no network.
>
> Vouch puts a signed passport in a QR or NFC tag. A scan verifies owner, actions, and standing on site.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 17: A passport a person can scan and verify offline.
>
> An unfamiliar robot rolls up to a loading dock, a lobby, or a nurse's station. A person has to make a call: is this machine authorized to be on site, who owns it, and what is it cleared to do? Most of the time there is no console and no reliable network to look it up. So the machine gets waved through on appearance.
>
> Anyone should be able to check a robot's credentials on the spot, with nothing but a phone.
>
> Vouch encodes a compact, signed passport into a QR code or NFC tag as a vouch-passport: URI carrying the credential's bytes. A reader scans it and runs verify_passport to confirm the robot's owner, authorized actions, certification, and standing, and the signature verifies with no network call, because the credential travels in the tag itself. build_passport and encode_passport produce the tag; the check is a scan.
>
> The result: a guard, a nurse, or a dockworker can verify a robot in seconds, with no network, instead of trusting how it looks.
>
> Next post: retiring and reselling a robot without leaving its trust behind.
>
> vouch-protocol.com
> #Robotics #Identity #Security

---

# Cluster E: Lifecycle, revocation, compliance, privacy

## Concept 18: Ownership, key changes, and a clean retirement

**X** (279/280)
> Vouch for Robotics. 18: Retire and resell, on the record.
>
> A robot is resold or scrapped, but its keys keep working. Ownership is unclear; a retired unit passes checks.
>
> Vouch signs ownership transfers into a custody chain; a decommission ends its trust.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 18: Ownership, key changes, and a clean retirement.
>
> A robot outlives its first owner. It gets resold, its keys get rotated after a scare, and one day it is pulled from service. Without a signed history, none of that is provable: a used robot's real owner is a guess, a rotated key is hard to tell from a hijack, and a decommissioned unit can keep presenting valid credentials past the point it should be trusted.
>
> A machine that changes hands and changes keys over a long life needs each of those transitions on the record.
>
> Vouch makes them accountable. The current owner signs an ownership transfer to the next, and linked transfers form a chain of custody that verify_custody_chain walks. The robot's current key authorizes its successor, forming a key history that verify_key_history walks, for a routine rotation or a post-compromise change. An owner or authority signs a decommission credential retiring the robot, after which a verifier refuses to trust it.
>
> The result: who owns a robot, which keys it has held, and whether it is retired are all signed facts, not paperwork.
>
> Next post: revoking a robot's authority the instant a key leaks.
>
> vouch-protocol.com
> #Robotics #Identity #Lifecycle

---

## Concept 19: Revoking a robot the instant a key leaks

**X** (272/280)
> Vouch for Robotics. 19: Pull the plug on a bad robot.
>
> A robot is stolen or its key leaks. You must cancel its authority across the fleet.
>
> Vouch offers two levels: revoke one credential, or kill a whole robot identity. Verifiers stop trusting it.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 19: Revoking a robot the instant a key leaks.
>
> A robot's signing key turns up in a leaked config, or the machine itself is stolen off a site. Every credential it holds becomes a liability, and every verifier that trusts it is exposed until you can pull that trust. If revocation is slow or all-or-nothing, you are stuck choosing between leaving a hole open and shutting down more than you need to.
>
> Cutting off a compromised robot has to be fast, and it has to be able to cut at the right size.
>
> Vouch offers two levels. Surgical, per-credential revocation attaches a status entry (a BitstringStatusList, a shared list where each credential has a slot marked valid or revoked) to a single identity, provenance, or capability credential. Whole-DID kill, for a leaked key or a captured robot, uses the standard revocation registry, and because a robot DID is an ordinary DID, the usual distribution path carries the kill with no new machinery.
>
> The result: you can revoke one capability or an entire robot, and verifiers stop trusting the revoked credential on their next check.
>
> Next post: proving a robot meets safety regulations, by machine, not paperwork.
>
> vouch-protocol.com
> #Robotics #Security #Revocation

---

## Concept 20: Compliance a machine can check

**X** (279/280)
> Vouch for Robotics. 20: Compliance a machine can check.
>
> Proving a robot meets ISO, EU Machinery, or EU AI Act rules is manual, and stale by the time it lands.
>
> Vouch maps a robot's credentials to each regulation's clauses and signs a conformance report.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 20: Compliance a machine can check, not a binder someone assembles.
>
> Proving a robot meets its safety and AI regulations is a paperwork exercise. Someone maps requirements to evidence by hand, assembles a binder, and files it, and by the time it is filed the fleet has changed. The mapping is human, slow, and hard for a regulator to re-check without repeating the whole job.
>
> If a robot's evidence is signed credentials, checking it against a regulation should be a computation, not a compilation.
>
> Vouch defines a conformance profile: a machine-checkable mapping from a robot's credentials to the clauses of a public regulation. Built-in reference profiles cover ISO 10218-1 and -2, ISO/TS 15066, the EU Machinery Regulation 2023/1230, the EU AI Act high-risk requirements, and UL 3300. check_conformance walks a profile and reports, per requirement, whether the presented credentials satisfy it, citing the clause. An assessor signs a point-in-time attestation over that report, and because the report is deterministic, every language reproduces it from the same credentials.
>
> The result: conformance becomes a signed, reproducible report a regulator can re-run, with the caveat that the profiles are a reference crosswalk, and each deployment confirms the mapping against the current law for its market.
>
> Next post: proving a robot had a basis to record the people around it.
>
> vouch-protocol.com
> #Robotics #Compliance #EUAIAct

---

## Concept 21: Consent bound to the exact capture

**X** (280/280)
> Vouch for Robotics. 21: Consent, bound to the capture.
>
> A robot in public records the people near it. On what basis, and can that consent be reused for another clip?
>
> Vouch binds a consent basis to each capture by hash, and holds fingerprints, not images.
>
> github.com/vouch-protocol/vouch

**LinkedIn**
> Vouch for Robotics. Part 21: Consent bound to the exact capture.
>
> A service robot moving through a lobby or a ward records the people around it as a side effect of doing its job. Two privacy questions follow. On what basis did it capture a given person: their consent, a posted notice, a legitimate interest? And if someone did consent, what stops that consent from being reused to justify a different recording?
>
> A robot that captures people needs to bind a lawful basis to each specific capture, and to hold as little about people as it can.
>
> Vouch does both. build_consent_evidence has the robot bind a capture's hash to a consent basis, one of explicit-consent, posted-notice, legitimate-interest, or redacted, and for explicit consent it commits to the covering tokens by their signature. A bystander can sign a consent token over the hash of one capture and the robot's DID, so verify_consent_token accepts it for that capture and that robot, and it cannot be replayed to another recording. The store holds hashes and the basis, not an image or a person's identifying data.
>
> The result: a robot can prove it had a basis to record a given moment, while holding fingerprints instead of footage.
>
> That closes the core robotics series. Next, an optional set for robots that operate with no network, in the air, or in orbit.
>
> vouch-protocol.com
> #Robotics #Privacy #AISafety
