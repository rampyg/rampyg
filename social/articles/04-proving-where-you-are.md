# Proving where you are, when a signature is not enough

A signature is a powerful thing. It proves who signed a message and that the message was not changed. But it has a blind spot that grows the farther a machine roams: a signature does not prove where the signer is.

That gap is small in a data center and large in the field. A robot's papers say it is standing at the loading bay. An attacker copies those papers and plays them back from another city, or another country, to pass as the robot and get in. Every signature checks out. The machine is not near the door.

For machines that move, and machines in places we cannot see, being in the right place has to be part of the proof. Vouch builds that in three ways.

## Measure the distance

When two machines talk, one can measure how long the other's signal takes to arrive. That travel time shows how far away the other is. A set of papers replayed from somewhere else arrives with the wrong travel time, and the check rejects it. The distance the machine claims and the distance the physics shows have to agree.

A tight beam of light does the same job in a different form. It lines up when two units face each other and at no other time, so a connection is proof they are in the same place, pointed at each other. There is no way to fake that from across the world.

## Cross-check the position

One machine's word for its own position is easy to fake, so Vouch does not take it. Several separate stations each measure how far the machine is from them, and compare. The real position is the one point that fits every measurement. A single false claim does not survive the cross-check, the way one witness who disagrees with three others stands out.

No station has to trust the machine, and no station has to take another on faith. The geometry does the arguing. A position either fits all the measurements or it does not.

## Obey the laws of motion

Every position claim is tested against physics. If a machine says it was in one place, and in another too far to reach in the time between, the claim is impossible, and the check rejects it. A tracker cannot jump across the map. A craft cannot be in two orbits at once. Motion that could not have happened is a lie, and it is caught as one.

## Why this is my favorite part

Most of security is one piece of math checking another piece of math. This work ties the math to the physical world. A signature you can copy. A travel time, a set of distances, a path that obeys the laws of motion: those you cannot copy from the wrong place, because faking them would mean bending physics, not breaking a cipher.

For a drone, a delivery robot, or a craft in deep space, that is the difference between a credential and a claim. The machine does not tell you where it is and ask you to believe it. It proves where it is, against a world that does not lie.

It is open source. github.com/vouch-protocol/vouch.
