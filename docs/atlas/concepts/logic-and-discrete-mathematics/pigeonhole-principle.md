---
type: Concept
title: The Pigeonhole Principle
description: If more items are distributed into fewer categories than items, some category must hold at least two — a counting-only proof of forced collisions.
book: logic-and-discrete-mathematics
chapters: [6]
tags: [combinatorics, existence-proof, counting, constraints]
created: 2026-07-12
---

# The Pigeonhole Principle

## Definition

If a set P (pigeons) has more elements than a set H (pigeonholes), then no mapping from P
to H can be injective — some element of H must receive at least two elements of P. The
book's plain-language version: "If more than n pigeons fly into n pigeonholes then at
least two pigeons will end up in the same pigeonhole." Its generalization, the Congested
Pigeonhole Principle, states that if more than kn pigeons fill n pigeonholes, some
pigeonhole holds more than k. Nothing about the specific items or categories matters — the
whole force of the principle comes from bare arithmetic comparison of two set sizes.

## In the Book

Section 6.4 opens with the claim that at least two people in Hong Kong have exactly the
same number of hairs on their head, derived without counting anyone: human hair counts
are all below 200,000 (biology), and Hong Kong's population exceeds 7,000,000 (statistics),
so by pigeonhole two people must land in the same hair-count "hole." The book works
through further applications: 370 students in a course guarantees two share a birthday
(370 pigeons into 366 day-holes); among any n+1 integers, two must share the same
remainder mod n, so their difference is a multiple of n; a piano competition needs at
least 497 entrants before two are guaranteed to choose the same pair of 32 Beethoven
sonatas (C(32,2)=496 possible pairs); and five points in an equilateral triangle of side 1,
split into four sub-triangles of side 0.5, force two points within 0.5 of each other. The
Congested version shows 61 students guarantee 6 sharing a birth month (61 > 5×12).

## Why It Matters

Pigeonhole proves that a collision or coincidence *must* exist without constructing it or
searching for it — pure counting substitutes for exhaustive search. That is a general
existence-proof pattern: whenever you can show "more things than categories," you get a
guaranteed clash for free, whether the domain is hash collisions, resource contention,
scheduling conflicts, or compression limits (you cannot losslessly compress every input
below its own length, because there are more inputs than shorter outputs). It is a
reminder that some claims about "there must be at least one X" don't need constructive
proof — a bound and a count are enough.
