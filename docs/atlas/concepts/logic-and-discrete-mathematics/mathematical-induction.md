---
type: Concept
title: Mathematical Induction
description: Prove a property holds for every natural number by showing it holds for a base case and that each case forces the next.
book: logic-and-discrete-mathematics
chapters: [1, 5]
tags: [proof-technique, recursion, well-ordering, formal-methods]
created: 2026-07-12
---

# Mathematical Induction

## Definition

Mathematical induction proves a statement P(n) for every natural number n by two steps:
a base step showing P(0) (or some starting value) holds, and an induction step showing
that whenever P(k) holds for some k, P(k+1) must hold too. The book states it as: "Suppose
that some property P of natural numbers holds for 0 and whenever P holds for some natural
number k, then it also holds for k+1. Then P holds for every natural number." The two-step
structure lets a single finite argument cover an infinite set of cases: the base step anchors
the chain, and the induction step is a reusable machine that pushes truth from any one link
to the next.

## In the Book

The book introduces induction in Section 1.3 with the classic sum formula
0+1+···+n = n(n+1)/2, working through the Base step (verifying P(0)) and the Inductive
Hypothesis (assuming P(k) to derive P(k+1)) explicitly, then a second worked example
proving n² ≤ 2ⁿ for all n ≥ 4, showing induction can start from any base value, not just 0.
Section 1.3's "Paradoxes" box immediately stress-tests the technique with fake inductive
proofs — "all horses have the same colour" and the heap paradox — to expose exactly where
a base step or induction step can silently fail. The book returns to induction repeatedly as
a proof engine: it reappears to prove the Pigeonhole Principle (Ch. 6) and to prove the
five-colour theorem for planar graphs (Ch. 7), where the induction step deletes a
low-degree vertex, colours the smaller graph by the inductive hypothesis, then reinserts
the vertex.

## Why It Matters

Induction converts a claim about infinitely many cases into two finite, checkable
obligations — connecting a proof strategy to any domain where a system unfolds by a
repeatable local rule: an algorithm's loop invariant, a recursive data structure, a
recurrence-defined sequence, or a chain of dependent decisions. Recognizing the base-case/
step-case shape lets you spot where an inductive-looking argument actually breaks (as the
book's horse-colour "proof" does, in the step from n=1 to n=2) rather than accepting the
conclusion because the mechanism sounds legitimate.
