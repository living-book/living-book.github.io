---
type: Concept
title: The Curse of Dimensionality
description: As the number of attributes describing something grows, similarity, distance, and generalization stop behaving intuitively and most learning methods degrade or break.
book: master-algorithm
chapters: [7]
tags: [machine-learning, high-dimensional-data, similarity, scaling]
created: 2026-07-12
---

# The Curse of Dimensionality

## Definition

Coined by control theorist Richard Bellman, the curse of dimensionality is the phenomenon whereby adding more attributes (dimensions) to a problem doesn't just add computational cost — it breaks the intuitions about distance and similarity that many learning methods depend on. Domingos calls it "the second worst problem in machine learning, after overfitting," and stresses that "no learner is immune" to it, even though some resist it better than others.

## In the Book

Chapter 7 (on analogy-based, or "analogizer," learning) uses nearest-neighbor algorithms as the sharpest illustration, since they rely directly on measuring similarity between examples. Domingos works through the "hyperorange" thought experiment: an orange whose pulp fills 90% of its radius has 73% of its volume as pulp in three dimensions (0.9³), but a hundred-dimensional "hyperorange" with the same 90%-of-radius pulp has only about three-thousandths of a percent of its volume as pulp — "the hyperorange is all skin." He shows the same breakdown for the normal distribution: in high dimensions a bell curve behaves like a doughnut, with samples more likely far from the mean than close to it. The consequence for nearest-neighbor is that in high dimensions "all examples look equally alike, and at the same time they're too far from each other to make useful predictions." He extends the problem to decision trees, which approximate a sphere-shaped concept with a bounding cube — in high dimensions almost the entire cube's volume lies outside the sphere, so accuracy collapses. He notes that the number of training examples needed to pin down a concept's boundary grows exponentially with the number of Boolean attributes, and that even fully relevant attributes can hurt if they're only weakly informative, since irrelevant noise in enough dimensions swamps genuine signal.

## Why It Matters

This concept generalizes past machine learning to any situation involving many simultaneous measures of similarity or many simultaneous variables — recommendation systems, forecasting with too many covariates, even human judgment about which of many features matter for a decision. Adding "more information" is not free: past some point, more dimensions dilute genuine signal, make notions of "similar" and "close" stop meaning what you think they mean, and require exponentially more data just to keep pace, which is a sharp corrective to the reflex that more variables or more granular measurement is always better.
