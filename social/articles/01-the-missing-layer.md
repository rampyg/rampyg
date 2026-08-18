# The missing layer: how do you trust an AI agent?

An AI agent booked a flight for someone this morning. Another moved money between accounts. A third read a patient record. Each one made a real request to a real system, and each system did the same thing: it looked at the request, saw that it carried a valid key, and did as it was told.

Here is what none of those systems could do: prove who the agent was, prove what it meant to do, and prove who allowed it.

That gap is the reason I started Vouch.

## We solved this once, for the web

For twenty-five years we have known how to answer this question for websites. When you visit your bank, your browser checks a small proof that the site is who it claims to be, and shows you a lock. Before that lock existed, anyone could stand up a page that looked like your bank, and you had no way to tell the real one from a copy. The lock did not make the web safe. It made the web checkable. You could stop guessing.

AI agents are in the world before the lock. An agent calls a service and says, in effect, trust me. The service has no way to check. It cannot tell a real agent from one an attacker stood up in the last hour. And when something goes wrong, the logs show that a request arrived and looked fine, and nothing more.

## The whole idea in one habit

Vouch is the lock for AI agents. The protocol comes down to one habit: a machine proves things rather than claiming them.

It proves who it is. Each agent gets a public name anyone can look up and a private key it keeps to itself, so it can sign its actions and anyone can check the signature.

It proves what it meant to do. Each action is a signed record stating the action, the target, and the resource, so a changed or replayed request gives itself away.

It proves who allowed it. Authority runs in a signed chain back to a person, and it shrinks as it passes from an agent to a helper, so no helper holds more power than the one that handed it the job.

And trust is not a stamp you earn one time. It is a live signal an agent has to keep renewing, so access that is forgotten fades rather than lingering.

## From agents to robots to the edge

A robot is an agent with a body, so the stakes rise: a bad move breaks a bone, not a database row. The same signed records carry a robot's identity, its force and speed limits, and a record of what it did that no one can rewrite.

And some machines work where there is no network at all: down a mine, over the ocean, in orbit. They have to prove who they are and refuse a bad order with no one to ask. The same idea stretches to cover them.

## Where this is going

That is the whole thing. Proof in place of trust-me, for every machine that acts on our behalf, wherever it is. It is open source, and I will cover one piece at a time: the key an agent is not allowed to hold, the record a robot cannot understate, the credential that cancels itself when a machine goes dark.

If you build or deploy agents, I would like your questions. Reply to this, or find the code at github.com/vouch-protocol/vouch.
