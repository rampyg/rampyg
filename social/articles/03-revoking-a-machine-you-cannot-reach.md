# How do you switch off a robot you cannot reach?

Canceling access is easy when everyone is online. You add the key to a cancel-list, every service reads the list, and the door closes. It works because the machine you are cutting off can hear the news.

Now take a robot down a mine, a drone over the ocean, a craft in orbit. It has no signal for hours, days, or months. You decide to pull its access. You add it to the cancel-list. And the robot does not see the list. To every machine it meets out there, its old papers say it is fine.

Two problems hide in that story, and Vouch handles both.

## Problem one: old news

The first is that offline machines carry stale information. A robot syncs its cancel-list, and goes dark for a week. During that week its access is pulled. Its list is out of date, but it does not know that.

Vouch has a checker weigh how old its cancel-list is against how risky the action in front of it is. A routine reading can run on a week-old list. A heavy physical move cannot. If the list is too old for the risk, the checker refuses, and when the picture is unclear, it fails safe. Old news is treated as old news, not waved through.

There is a matching piece on the machine's own side. It can carry a small, fresh proof that its access was good as of a recent moment, so a checker it meets can confirm that much without a live connection. The longer a machine goes with no contact, the less its old proofs are worth, and its trust fades on a slope rather than holding at full strength until it expires.

## Problem two: you cannot send the stop

The second problem is deeper. Suppose you want to cut a machine off. You cannot reach it to say so. A cancel-list helps a machine that can read it, and no other.

So Vouch flips the direction. In place of sending a stop, it arranges for the machine to stop itself. A credential is issued that expires unless the machine receives a fresh renewal by a deadline. While a keeper keeps renewing, the machine keeps working. The moment the renewals stop, because the machine drifted out of contact, or a keeper chose to hold the renewal back, the credential switches itself off. No message to the machine is needed.

It is a dead-man switch for authority. Silence ends the grant, rather than extending it. To keep a disconnected machine trusted, someone has to keep saying yes. Say nothing, and its power lapses on its own.

## Why this is the right shape

There is a habit in security of assuming you can reach the thing you need to control. It holds in a data center and breaks in the field. A drone past the horizon, a craft between contacts, a robot deep underground: for long stretches, you cannot reach any of them.

Both ideas start from that fact rather than fighting it. One makes a machine honest about how stale its own view is. The other makes a grant lapse on silence, so cutting a machine off does not depend on reaching it. Together they turn a hard question, how do you reach a machine you cannot reach, into one you do not have to answer.

This is part of a set of ideas for trust with no network, which I am writing about in this series. Code at github.com/vouch-protocol/vouch.
