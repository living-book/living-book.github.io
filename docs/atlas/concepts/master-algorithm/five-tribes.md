---
type: Concept
title: The Five Tribes of Machine Learning
description: Machine learning splits into five schools — symbolists, connectionists, evolutionaries, Bayesians, analogizers — each with a different root metaphor for what learning is.
book: master-algorithm
chapters: [1, 2]
tags: [taxonomy, paradigms, machine-learning, pluralism]
created: 2026-07-12
---

# The Five Tribes of Machine Learning

## Definition

Domingos divides machine learning into five schools of thought, each answering "what is learning?" differently and drawing on a different parent discipline: symbolists (learning is the inverse of deduction; roots in logic and philosophy), connectionists (learning is how the brain does it; roots in neuroscience), evolutionaries (learning is natural selection; roots in genetics), Bayesians (learning is probabilistic inference; roots in statistics), and analogizers (learning is extrapolating from similarity; roots in psychology and optimization). Each tribe has produced its own "master algorithm" — inverse deduction, backpropagation, genetic programming, Bayesian inference, and the support vector machine.

## In the Book

The tribes structure the book's central chapters (4 through 8), each devoted to one school's worldview, historical lineage, and signature technique. Domingos uses the parable of the blind men and the elephant throughout: one tribe feels the trunk and calls it a snake, another the leg and calls it a tree. He is explicit that no tribe alone is right — symbolists are good at reasoning from prior knowledge and give interpretable rules but struggle with noisy, high-dimensional data; connectionists excel at pattern recognition but their models are opaque "black boxes"; evolutionaries search structure and parameters jointly but are slow; Bayesians handle uncertainty rigorously but their inference is often computationally intractable; analogizers generalize well from few examples but scale poorly. In the cancer-curing worked example he returns to across chapters, each tribe contributes a different necessary piece — symbolic rules for known drug interactions, neural nets for image analysis, evolutionary search for drug design, Bayesian reasoning under uncertainty, similarity-based matching to prior patients — and none of them is sufficient alone.

## Why It Matters

The five-tribes framework is a portable diagnostic: when a field has multiple competing schools that each solve part of the problem and are each blind to what the others see, progress often comes not from picking a winner but from identifying what each paradigm is actually optimized for and combining them. It also warns against treating a currently-dominant paradigm (in ML's case, connectionism/deep learning) as if it were the whole field — the tribes existed before deep learning's rise and each still solves problems the others can't.
