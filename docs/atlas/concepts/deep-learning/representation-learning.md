---
type: Concept
title: Representation Learning
description: Let the machine learn the features themselves, not just the mapping from features to output — the representation is the hard part worth automating.
book: deep-learning
chapters: [1, 15]
tags: [features, machine-learning, automation, abstraction, learning]
created: 2026-07-12
---

# Representation Learning

## Definition

Most learning algorithms only work as well as the features they're handed — a doctor's structured report of "presence of uterine scar" lets logistic regression predict delivery outcomes, but the raw pixels of an MRI scan tell it almost nothing. Representation learning is the move of using machine learning to discover not just the mapping from representation to output, but the representation itself, so the system builds its own useful features from raw data instead of depending on a human to hand-design them.

## In the Book

The book opens with this problem before introducing deep learning as its solution: designing features for a task like detecting cars in photographs is hard because something as simple-sounding as "a wheel" is nearly impossible to define in terms of raw pixel values once you account for shadows, glare, and occlusion. The book's worked example is polar versus Cartesian coordinates (Fig. 1.1) — two categories of points that are inseparable by a straight line in one representation become trivially separable by a vertical line in the other; the data didn't change, only the representation did. The quintessential representation-learning algorithm the book returns to is the autoencoder (developed fully in Chapter 14): an encoder maps input into a new representation and a decoder maps it back, trained to preserve information while giving the new representation useful properties. Chapter 15 extends this into the idea of "factors of variation" — a speech recording's factors include speaker age, sex, accent, and words spoken — and argues that a good representation is one that disentangles these factors so a downstream task becomes easy.

## Why It Matters

This concept relocates the hard part of a problem: instead of asking "what rule maps input to output," you ask "what description of the input would make that rule obvious." It explains why the same raw data can be nearly unusable in one framing and trivial in another, and it generalizes to any domain where the bottleneck isn't reasoning but framing — a spreadsheet column that's the wrong unit, a org chart that hides the real reporting relationships, a legal contract structured around the wrong obligations. Once you see representation as a variable to be optimized rather than a given, "reframe the problem" stops being a vague creativity tip and becomes a specific, learnable move.
