# Vouch Short Posts for Bluesky, Threads, and Mastodon

These platforms cap posts near 300 to 500 characters, so the long-form versions do not fit. Use these short hook-plus-link posts instead, one per concept, matched to the X long-form running the same day. Each is a failure hook plus the repo link, kept under 300 characters so it fits Bluesky (the tightest). Rules: no acronyms, no jargon, no hyperbole, no adverbs.

Link used throughout: github.com/vouch-protocol/vouch

---

## AI Agents

1. An AI agent connects to your systems and says it works for a company you deal with. Should you believe it? You have no way to check. That gap is what we set out to close. github.com/vouch-protocol/vouch

2. An agent moved money. A week on, the logs cannot prove what it meant to do, or whether the request was changed or replayed. This is the fix. github.com/vouch-protocol/vouch

3. Same data, same key, and a partner's system rejects your signature, because the two wrote the data out in different ways. This is how the signature matches everywhere. github.com/vouch-protocol/vouch

4. Sign a record that must last twenty years, and a future computer could forge the method you used. How a signature stays safe for a machine's whole life. github.com/vouch-protocol/vouch

5. Your assistant spins up a helper, the helper spins up another, and an email goes out you did not approve. Who authorized it? Authority as a signed chain. github.com/vouch-protocol/vouch

6. A contractor's agent keeps its access a year after the project ended, because nobody canceled it. How trust fades unless it is renewed. github.com/vouch-protocol/vouch

7. A web page hides a line telling your agent to reply with its signing key. If the key sits where the model can see it, that can work. How to keep the key out of reach. github.com/vouch-protocol/vouch

---

## Robotics

A0. A software agent's mistake corrupts a record. A robot's mistake can hurt a person. Same software, a body attached. A series on making robots accountable. github.com/vouch-protocol/vouch

R1. Copy a robot's identity onto a cheaper machine and it passes as real. How a robot proves it is the machine it claims to be, tied to a sealed chip it cannot fake. github.com/vouch-protocol/vouch

R2. A robot hurts someone. Which software was driving it, and what limits did it have? An update could have swapped either with no trace. How to prove it. github.com/vouch-protocol/vouch

R3. A robot built this year runs for twenty. The signatures that protect it may not last that long. How its records stay safe for its whole life. github.com/vouch-protocol/vouch

R4. One software mind can move from one robot body to another. Is it the same mind you can hold to account, and not running two at once? How to prove it. github.com/vouch-protocol/vouch

R5. A robot arm can be safe by a wall and dangerous by a person. A settings file will not stop it. How force and speed limits become a signed rule it enforces on itself. github.com/vouch-protocol/vouch

R6. A robot passes its morning check, and drifts out of its safe limits by afternoon. How trust fades unless the robot keeps proving it is in bounds. github.com/vouch-protocol/vouch

R7. A five-year-old robot with worn joints runs at its factory limits. How its limits tighten as it wears, on the record. github.com/vouch-protocol/vouch

R8. One operator, or one stolen key, should not launch a dangerous robot action alone. A two-person rule, proven in signatures. github.com/vouch-protocol/vouch

R9. After a crash, was the camera feed the robot acted on real, or edited? How a robot proves what its sensors saw. github.com/vouch-protocol/vouch

R10. A robot blends camera and range sensors into one picture and acts on it. Fake one input and the picture lies. How the picture ties to its real inputs. github.com/vouch-protocol/vouch

R11. After an incident, the logs are gone or edited, and a fake stop could halt a line. A sealed recorder and a stop that cannot be forged. github.com/vouch-protocol/vouch

R12. Before an audit, incident counts are easy to trim. A safety summary that cannot report fewer events than the log holds. github.com/vouch-protocol/vouch

R13. A package passes through pickers, robots, and conveyors, and arrives crushed. Each party blames the next. How the break traces to one hop. github.com/vouch-protocol/vouch

R14. Two robots from different makers must work together. How does each know the other is not a fake? A signed handshake that bounds what they share. github.com/vouch-protocol/vouch

R15. Robots need to open doors and dock at chargers. One shared master key does not scale or stay safe. How a door checks a robot with no network. github.com/vouch-protocol/vouch

R16. A robot in a mine has no signal, and needs bounded authority it can trust. A signed lease it checks on its own, with no network. github.com/vouch-protocol/vouch

R17. A robot rolls up to a dock and the guard cannot check who owns it, with no network to ask. A passport a phone can scan and verify on the spot. github.com/vouch-protocol/vouch

R18. A robot is resold or scrapped, but its keys keep working. How ownership, key changes, and retirement become signed facts. github.com/vouch-protocol/vouch

R19. A robot is stolen or its key leaks. How to cancel one capability, or a whole robot identity, across the fleet. github.com/vouch-protocol/vouch

R20. Proving a robot meets safety and AI rules is slow paperwork. How the check becomes a signed report a regulator can re-run. github.com/vouch-protocol/vouch

R21. A robot in public records the people around it. On what basis, and can that consent be reused for another recording? How consent binds to one capture. github.com/vouch-protocol/vouch

---

## Disconnected Edge and Space

D0. Every idea so far assumed the machine can check in. Take that away: a mine, the ocean, orbit. How a machine stays trustworthy with no signal. github.com/vouch-protocol/vouch

D1. A robot goes offline, its access is pulled, and it does not see the update. How a checker treats an old cancel-list as old news, and fails safe. github.com/vouch-protocol/vouch

D2. How do you switch off a robot you cannot reach? Flip it: a credential that cancels itself when the renewals stop. A dead-man switch for authority. github.com/vouch-protocol/vouch

D3. A robot's papers say it is at the dock. An attacker replays them from another country. How presence, measured by physics, becomes part of the proof. github.com/vouch-protocol/vouch

D4. A drone spoofs its position to enter a barred zone. How several stations and the laws of motion catch a machine that lies about where it is. github.com/vouch-protocol/vouch

D5. A grant that says valid until Tuesday assumes a machine can trust its clock. How authority ties to a place or a path, not a clock. github.com/vouch-protocol/vouch

D6. A clock can drift, and in space a stray particle can corrupt a key. How a machine grades its own time and steps back when its foundations are shaky. github.com/vouch-protocol/vouch

D7. A group of machines works with no way to call home, and one goes bad. How a swarm polices itself and quarantines the bad member. github.com/vouch-protocol/vouch

D8. On a long mission, units fail and messages hop with no live link. How keys and trust survive the trip. github.com/vouch-protocol/vouch
