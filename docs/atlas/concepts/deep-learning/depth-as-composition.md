---
type: Concept
title: Depth as Composition
description: Stacking layers that each build on the last lets a network represent functions that would need exponentially more resources built any other way.
book: deep-learning
chapters: [1, 6, 15]
tags: [depth, composition, hierarchy, abstraction, efficiency]
created: 2026-07-12
---

# Depth as Composition

## Definition

Depth is not "more of the same layer" — it's the number of sequential steps of composition needed to compute a function, where each step's output becomes the next step's input and can build a more abstract concept out of simpler ones already computed. A network's depth can be measured either as the length of the computational chain or as how many levels the *concepts* it represents are related to each other (a face built from eyes built from contours built from edges). The book's core empirical claim is that some functions which require an exponential number of units to represent shallowly can be represented with a polynomial number of units once depth is allowed to grow.

## In the Book

Chapter 1's flagship illustration (Fig. 1.2) is object recognition from raw pixels: a first hidden layer detects edges by comparing neighboring pixel brightness, a second layer finds corners and contours by combining edges, a third finds object parts by combining contours, and the output layer identifies the object — each layer's job becomes tractable only because the layer below already solved a simpler version of the problem. Chapter 6.4.1 makes the exponential-advantage claim precise: functions representable by piecewise-linear networks with absolute-value or ReLU units gain regions to distinguish that grow exponentially with depth, because each layer can "fold" the space created by the layer before it (Fig. 6.5) — a fixed number of folding operations composed in sequence produces exponentially more distinguishable regions than the same number of units arranged in one wide layer. The universal approximation theorem guarantees a shallow network *can* represent any function, but the book stresses this is a different, weaker claim than *efficiently* — Barron's bound shows the required width can be exponential in the input dimension for a single hidden layer, a cost depth avoids by reusing earlier computation.

## Why It Matters

This is the general case for why hierarchy beats flatness when a target is compositional: if the thing you're trying to build is itself made of reusable sub-parts, a system that computes and reuses those sub-parts needs far fewer total components than one that must special-case every combination from scratch. It applies wherever "depth" shows up outside neural networks — an org chart of delegated authority versus one manager approving everything directly, a legal argument built from established sub-claims versus one argued from first principles each time, a codebase of composed functions versus one flat script. The claim to hold onto is specific: depth isn't valuable because it's fashionable, it's valuable exactly when the target has compositional structure to exploit — and worthless, even harmful, when it doesn't.
