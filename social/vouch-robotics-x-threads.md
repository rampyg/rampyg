# Vouch Robotics, X Threads (personal account)

Voice: personal / founder. Format: one concept = one thread. Hook first, no link or tag in tweet 1. Tag @Vouch_Protocol and the repo link in the final tweet. Rules: no adverbs, no acronyms, no jargon, no hyperbole, logical flow. Every tweet verified at or under 280 characters (count shown).

Post the numbered tweets in order as a single thread. Reply to your own first tweet within the hour to help reach.

---

## Anchor thread: a robot is an AI agent with a body

**1/** (229)
When a software agent makes a mistake, it corrupts a record.
When a robot makes the same mistake, it can hurt a person.
Same kind of software, higher stakes, because it has a body.
Let me explain how you make a robot accountable.

**2/** (243)
A robot raises the same questions a software agent does, with more weight.
Who is this machine?
What is it allowed to do with its arm?
Who told it to act?
What did its cameras see?
And when something goes wrong, can anyone prove what happened?

**3/** (226)
The answer is to turn each of those into a signed record anyone can check, with no central authority in the middle.
A robot's identity, its limits, its history: each becomes a small proof the robot carries and shows on demand.

**4/** (210)
This is what Vouch does for robots. It is open source, and it builds on the same kind of checks that secure websites.
A proof made by a robot in one system can be checked by a controller from a different maker.

**5/** (225)
Over this series I will take one piece at a time: how a robot proves who it is, what it may do, and what it did.
First: proving it is the machine it claims to be.
Built at @Vouch_Protocol. Open source: github.com/vouch-protocol/vouch

---

## Concept 1 thread: hardware-rooted identity

**1/** (240)
A warehouse robot passes every safety check. It works next to people all day.
Someone copies its identity onto a cheaper machine that skipped inspection.
Your systems cannot tell the two apart.
Here is how a robot proves it is the real one.

**2/** (209)
Most robots prove who they are with a stored secret, a kind of password file.
Copy that file onto another machine, and to every system the copy is the same robot.
A password can be copied. That is the problem.

**3/** (217)
Vouch gives the robot a pair of keys.
One key stays private, sealed inside the machine. The other is public, so anyone can check the robot's signature against it.
The robot proves who it is without sharing the secret.

**4/** (208)
That private key lives inside a sealed chip built into the machine, a chip made so the key cannot be extracted.
Move the software to another body, and the sealed chip is missing. The signature stops matching.

**5/** (184)
So a clone fails the check. It has the files, but not the one thing it cannot copy: the sealed chip the real robot was built with.
Identity is tied to the machine, not to a file on it.

**6/** (148)
Next in the series: proving which brain and which safety limits the robot is running.
Built at @Vouch_Protocol. Open source: github.com/vouch-protocol/vouch

---

## Concept 2 thread: model and settings provenance

**1/** (230)
A robot hurts someone. The first question is simple: which software was driving it, and what safety limits did it have?
The maker pushed three remote updates last month.
Nobody can say which version was in charge when it happened.

**2/** (187)
The software inside a robot changes over its life. Each update can change what the machine will do.
So the record of what it is running has to be as trustworthy as the actions themselves.

**3/** (228)
Vouch has the maker sign a record of what the robot runs: the exact program, a fingerprint of its settings, and its safety limits.
A fingerprint is a short code taken from a file. Change the file, and the code no longer matches.

**4/** (166)
Every update is signed again and points to the version it replaces.
So the updates form a chain you can walk, and no version can be swapped in without leaving a mark.

**5/** (215)
That leaves one signed answer to which software and which limits were running, at any moment in the robot's past.
Next: hard limits on force and speed, before the arm moves.
@Vouch_Protocol · github.com/vouch-protocol/vouch

---

## Concept 3 thread: built to outlast its own cryptography

**1/** (192)
A robot built this year can stay in service for ten to twenty years.
That is a problem for the way it signs things.
The signatures that keep it safe today may not stay safe for its whole life.

**2/** (218)
Every robot signs its records to prove they are real. Those signatures rely on math that is strong against the computers we have.
A new kind of computer, still being built, could one day break that math and forge them.

**3/** (211)
A robot whose signatures can be forged is a robot whose identity and whose records can be faked.
And you cannot re-sign a whole fleet in the field on short notice. The protection has to be built in from day one.

**4/** (180)
Vouch signs each robot record two ways at once: with today's signature, and with a newer one designed to resist that future computer.
Both have to check out for the record to pass.

**5/** (239)
So the record stays trustworthy as long as either signature holds, which carries you through the long switch the whole industry is starting.
Next: one software mind that moves between robot bodies.
@Vouch_Protocol · github.com/vouch-protocol/vouch

---

## Concept 4 thread: one mind, many bodies

**1/** (215)
A software mind can move from one robot body to another.
Two problems follow.
After the move, is it the same mind you can hold to account?
And is one mind running two bodies at the same time, hidden behind one name?

**2/** (146)
An identity that travels needs a thread that survives the move, so a body swap cannot become a way to dodge responsibility or to double up unseen.

**3/** (178)
Each time the mind takes a body, it signs a record binding itself to that body for a set period.
Line those records up, and you can follow one mind across every body it has used.

**4/** (196)
A check walks that line and confirms two things: every record carries the same mind, and each new body continues from the one before.
A second check confirms the mind is not in two bodies at once.

**5/** (213)
So you can prove the same accountable mind carried across bodies, and catch the case where it split in two.
Next: the safe limits on force and speed, before the arm moves.
@Vouch_Protocol · github.com/vouch-protocol/vouch
