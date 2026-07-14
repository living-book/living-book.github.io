---
type: Concept
title: The Limits of Local Generalization
description: A learner that only assumes "nearby inputs get similar outputs" needs as many examples as there are regions to distinguish — depth and structure buy a way around that wall.
book: deep-learning
chapters: [5, 15]
tags: [generalization, machine-learning, structure, priors, scaling]
created: 2026-07-12
---

# The Limits of Local Generalization

## Definition

The most common way a learning algorithm generalizes to unseen inputs is the smoothness (local constancy) prior: assume the target function doesn't change much within a small neighborhood, so a nearby training example is a good guide to the answer. This works well when there are few enough regions of interest to cover with examples — but the number of regions a purely local method needs examples for grows with the complexity of the target function, and a purely local method has no way to say anything about a region it hasn't seen an example from.

## In the Book

Section 5.11.2 makes this concrete with k-nearest-neighbors and decision trees: k-NN with k=1 can distinguish no more regions than it has training examples (each example's Voronoi cell), and a decision tree needs at least n leaves — hence roughly n examples — to represent a function requiring n distinguishable regions. The book's illustration is a checkerboard: a smoothness-only learner given far fewer examples than there are black-and-white squares "would be guaranteed to correctly guess the color of a new point if it lies within the same checkerboard square as a training example," but has zero basis for extending the pattern to a square it has never seen a point from, even though the checkerboard obviously has simple, learnable structure. Chapter 15.4 generalizes the same point mathematically: non-distributed algorithms (k-NN, kernel machines with local kernels, Gaussian mixtures) assign a separate degree of freedom per region and so need examples proportional to the number of regions, while a distributed, compositional representation can distinguish O(n^d) regions from O(n) parameters by intersecting many features simultaneously — buying "nonlocal" generalization to regions with no training example nearby, provided the underlying structure (periodicity, composition, translation-invariance) actually holds.

## Why It Matters

This draws a sharp line between two very different bets a system can make about the world: "the answer near here resembles the answer here" (safe, general-purpose, but expensive — costs one observation per distinguishable case) versus "the answer follows a compositional rule" (cheap once true, but wrong and misleading if it isn't). It explains why interpolation-only reasoning — case-based precedent, nearest-comparable pricing, "we've never seen this exact situation before so we can't say" — runs into a hard wall as the space of distinct cases grows, and why finding the underlying generative structure (the rule behind the checkerboard) is what lets a system say something sensible about a case it has never encountered.
