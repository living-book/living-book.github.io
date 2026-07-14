---
type: Concept
title: A Test's Goodness Is Relational, Not Intrinsic
description: A test can't be judged good or bad in isolation — "goodness" is a property of the relationship among the test, the implementation, and the situation it's used in.
book: perfect-software
chapters: [8]
tags: [measurement, quality, relativity, testing, evaluation]
created: 2026-07-12
---

# A Test's Goodness Is Relational, Not Intrinsic

## Definition

Run against a genuinely bug-free system, a superbly designed test suite and a lousy one produce the identical result — no bugs found — so bug-finding outcomes alone can never certify which set of tests was better. "Goodness" therefore isn't a property of a test, or even of a test-plus-implementation pair; it's a property of the relationship among the test, the specific implementation, and the situation the software will be used in — a test adequate for one internal tool can be dangerously inadequate for the same code sold to a thousand customers.

## In the Book

Weinberg constructs the thought experiment directly: define a "perfect" test set (finds every bug, never flags a non-bug, gives complete confidence of both, does it cheaply) and notice you can't verify these properties in advance, only after the fact — and even "after the fact" is compromised, since he describes receiving a letter thirty years after publishing The Psychology of Computer Programming pointing out an "obvious" error no reader had ever caught in 200,000 sold copies. He offers "bebugging" (a term he says he coined) — seeding known bugs, sometimes ones developers already found naturally in review, to estimate what fraction of unknown bugs testing is likely missing — as a partial, statistical workaround, not a certainty. He closes with the smoke-alarm analogy: a dead smoke alarm looks behaviorally identical to a working one until there's a fire, which is why "no information" gets mistaken for "no value," and why managers who judge testers by bug counts perversely reward testers more when the underlying product is worse.

## Why It Matters

This is a general antidote to judging any verification activity — audits, code review, safety inspection — purely by its output counts. A clean bill of health looks identical whether it came from a rigorous process or a lazy one, so evaluating the process itself (coverage, honesty, understandability, what it was actually designed to check) matters more than the headline number it produced.
