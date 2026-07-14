---
type: Concept
title: Distributed Representations
description: Represent a thing with many features that each participate in many things, rather than one dedicated symbol per thing — combinatorics beats enumeration.
book: deep-learning
chapters: [1, 15]
tags: [representation, combinatorics, generalization, neural-networks, efficiency]
created: 2026-07-12
---

# Distributed Representations

## Definition

A distributed representation describes a concept using many features that can each be set independently, and each individual feature is reused across many different concepts. This is contrasted with a symbolic or "one-hot" representation, where a dedicated unit fires for each category and shares nothing with any other category. The payoff is combinatorial: n features that can each take k values can distinguish k^n concepts, instead of the n concepts a one-symbol-per-concept scheme distinguishes.

## In the Book

The book's running example (Chapter 1, expanded in Chapter 15) is a vision system that must recognize {car, truck, bird} in {red, green, blue}. A non-distributed scheme needs nine dedicated neurons — one per combination — and each must independently relearn the idea of "redness" from scratch for every object type it appears with. A distributed scheme uses three neurons for color and three for object identity: six neurons instead of nine, and the "redness" neuron learns from every red object it sees, whether car, truck, or bird. Chapter 15 formalizes why this generalizes better: non-distributed algorithms like k-nearest-neighbors, decision trees, and Gaussian-kernel methods can only assign an output to a region near an example they've actually seen (the "smoothness prior"), so the number of distinguishable regions grows linearly with the number of examples or parameters. A distributed representation built from n binary features defined by hyperplanes can carve up d-dimensional space into O(n^d) regions — exponentially more regions than parameters — because "cat" and "dog" can now share attributes like has_fur, so what's learned about one transfers to the other even without having seen the second directly.

## Why It Matters

This is the argument for why compositional description beats a lookup table wherever the number of things to describe is combinatorially large: a vocabulary of shared, reusable attributes generalizes to combinations it has never directly observed, while a vocabulary of one dedicated label per case can only ever repeat what it's already seen. It reframes categorization systems generally — taxonomies, org charts, product catalogs, personality typologies — around a design question: are the units of description shared and independently combinable, or is each case getting its own bespoke bucket that learns nothing from its neighbors?
