---
type: Concept
title: Regularization as Preference, Not Constraint
description: Instead of forbidding a model certain solutions, penalize them softly — express a preference the training data can still override if the evidence is strong enough.
book: deep-learning
chapters: [5, 7]
tags: [regularization, machine-learning, bias, tradeoffs, generalization]
created: 2026-07-12
---

# Regularization as Preference, Not Constraint

## Definition

There are two different ways to control what a learning algorithm can conclude: exclude candidate solutions entirely (a hard constraint on the hypothesis space), or make some candidates cost more than others while leaving all of them technically reachable (a soft preference). The book defines regularization as any modification to a learning algorithm intended to reduce its generalization error without reducing its training error, and frames excluding a function outright as just the limiting case of a preference — "an infinitely strong preference against that function."

## In the Book

Chapter 5.2.2 builds this from the weight-decay example: instead of restricting linear regression to a smaller family of functions, add a penalty term λw^Tw to the training objective that costs the model more for using larger weights. When λ = 0 there's no preference; as λ grows, the model is pushed toward smaller weights but can still use large ones if the fit improves enough to be worth the penalty. Figure 5.5 shows this concretely on a degree-9 polynomial: with excessive λ, the model is forced flat and underfits; with λ near zero it overfits wildly; a well-chosen medium λ recovers a curve close to the true quadratic, "even though the model is capable of representing functions with much more complicated shape." This section follows directly from the no-free-lunch theorem (5.2.1) — since no algorithm is best on average across every possible task, "we must design our machine learning algorithms to perform well on a specific task... by building a set of preferences into the learning algorithm."

## Why It Matters

This distinguishes two very different ways institutions and systems limit behavior: rules that forbid an option outright versus costs/incentives that discourage it while leaving it available if circumstances justify it. A constraint is a wall; a preference is a slope — and the slope is often the better design, because it doesn't need to anticipate every legitimate exception in advance the way a rule does. This reframes regularization, policy design, pricing, and even personal habits (a soft "usually don't" versus a hard "never") as points on the same spectrum, and gives a concrete lever — how strong is the penalty — for tuning where on that spectrum you want to sit.
