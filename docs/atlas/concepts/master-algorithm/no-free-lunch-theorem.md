---
type: Concept
title: The No-Free-Lunch Theorem
description: Averaged over all possible worlds, every learning algorithm performs exactly as well as random guessing — so learning is only possible by building in assumptions about the world.
book: master-algorithm
chapters: [3]
tags: [induction, bias, machine-learning, epistemology]
created: 2026-07-12
---

# The No-Free-Lunch Theorem

## Definition

David Wolpert's "no free lunch" theorem, as Domingos presents it, proves that no learning algorithm can be better than random guessing when averaged across every possible world it might encounter: for any world where a learner outperforms chance, there is an equally likely "antiworld" (with all unseen labels flipped) where it does correspondingly worse. The practical upshot is that "there's no such thing as learning without knowledge" — a learner only beats chance in the one world we actually live in because it carries built-in assumptions, or bias, about that world.

## In the Book

Chapter 3 opens with Hume's problem of induction — the philosophical observation that no amount of past observation can logically guarantee a conclusion about the future or about unseen cases — and treats Wolpert's theorem as its "modern embodiment" in rigorous mathematical form. Domingos illustrates it with an analogy to Pascal's wager: just as no god is objectively more rational to bet on than any other once you consider the full space of possible gods, no learning algorithm is objectively better than any other once you consider the full space of possible worlds. He then reframes machine learning as an "ill-posed problem," using the toy example "which two numbers add up to 1,000?" — unsolvable without an added assumption — and cites Tom Mitchell's phrase "the futility of bias-free learning": in ML, bias isn't a pejorative, it's the indispensable preconception that makes generalization possible at all, whether hand-coded by an engineer or hardwired by evolution into the brain.

## Why It Matters

This is a rigorous, general argument that no method — statistical, algorithmic, or human — can generalize from limited evidence without smuggling in prior assumptions, and that the right response is not to eliminate those assumptions (impossible) but to make them explicit and match them to the actual domain. It's the theoretical backbone for why "the data speaks for itself" is never literally true, and it gives a principled way to interrogate any predictive claim: what assumptions about the world does this method bake in, and do they actually hold here?
