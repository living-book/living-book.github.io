---
type: Concept
title: Don't Mistake a Solution Method for a Problem Definition
description: A client's proposed technique (enumerate all combinations, run a linear program) is not the problem itself, and treating it as one hides the real question being asked.
book: are-your-lights-on
chapters: [4, 5, 6]
tags: [problem-framing, solution-bias, requirements, computer-science]
created: 2026-07-12
---

# Don't Mistake a Solution Method for a Problem Definition

## Definition

Clients rarely hand a problem solver a bare problem — they hand over a
half-built solution method and expect it implemented. "DON'T TAKE THEIR SOLUTION
METHOD FOR A PROBLEM DEFINITION," the book warns, and, in a harder form,
"DON'T MISTAKE A SOLUTION METHOD FOR A PROBLEM DEFINITION — ESPECIALLY IF IT'S
YOUR OWN SOLUTION METHOD." A method presented as if it were the problem forecloses
better solutions before they're even considered, and a solver's own favorite method
is the most dangerous of all, because it never even feels like an assumption.

## In the Book

A comptroller arrives with 24 hours left before sealed government-property bids
must be finalized, carrying a "plan": have a computer generate and rank all
roughly 4,000,000 possible bid combinations so the executives can scan the list
for the best one meeting the rules. The programmer team treats this enumeration
scheme as the problem and spends effort making it run in 1 hour instead of 12.
Billy Brighteyes instead reads the actual bidding rules for a few minutes and
solves the underlying allocation problem with logic and common sense in under
five minutes — a solution so fast the executives don't believe he solved their
real problem. A year later, at a new job, Billy learns from an operations
researcher that a different company faced with the same rules used a linear
programming "package" to solve it in two days for $1,400 — yet another solution
method mistaken for the definition, and just as beside the point, since Billy
realizes the real problem was never the arithmetic at all but how each bidder
should act knowing the others might also be seeing and revising their bids.

## Why It Matters

Whoever asks for help typically arrives already anchored to a technique — a
spreadsheet, an algorithm, a familiar procedure — and describes the problem in
its terms. Recognizing that the technique is a proposed answer, not the question,
is what lets a solver notice cheaper solutions, catch a problem that was framed
wrong from the start, or discover that the requester doesn't yet know their own
real problem. It's especially dangerous when the solution method is the solver's
own specialty, since expertise makes a habitual approach invisible as a choice.
