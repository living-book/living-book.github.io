---
type: Concept
title: Ensemble Metalearning
description: Combining many imperfect learners — by voting, weighting, or correcting each other's errors — reliably beats relying on any single best learner alone.
book: master-algorithm
chapters: [9]
tags: [machine-learning, aggregation, diversity, error-correction]
created: 2026-07-12
---

# Ensemble Metalearning

## Definition

Metalearning, in Domingos's account, treats a committee of trained learners' predictions as a new dataset and learns, on top of it, how to combine them into a single better prediction — "learning about the learners." He walks through three variants: **stacking**, where a metalearner (any learner, from a decision tree to a weighted vote) learns which base learners to trust in which situations, invented by David Wolpert, the same researcher behind the no-free-lunch theorem; **bagging**, invented by Leo Breiman, which trains the same learner on many resampled variants of the training set and combines the results by voting to reduce variance; and **boosting**, created by Yoav Freund and Rob Schapire, which repeatedly reapplies the same classifier while up-weighting previously misclassified examples, "boosting" a barely-better-than-random classifier into a highly accurate one.

## In the Book

Chapter 9 introduces this using a medical committee metaphor: a doctor consulting several specialists and combining their opinions is doing exactly what a metalearner does, treating the specialists' recommendations as the new input features. Domingos flags a subtlety — to avoid the committee being dominated by learners that simply memorized (overfit) the training data, each learner's prediction on a given training example must come from a version trained without that example. He cites concrete high-stakes uses: the winning entry of the Netflix Prize used stacking to combine hundreds of learners, IBM's Watson used it to pick a final answer among candidates, and Nate Silver's election forecasting combines polls the same way. He also notes that bagging applied to decision trees, with each tree further restricted to a random subset of attributes at each split, produces random forests — "some of the most accurate classifiers around," used by Microsoft's Kinect and regularly winning ML competitions.

## Why It Matters

This is the practical, working-today version of the book's "unify the five tribes" ambition: rather than requiring one paradigm to dominate, it demonstrates that diverse, individually-flawed models systematically outperform any single model when their errors are uncorrelated, because the errors average out while the signal reinforces. The same logic — aggregate diverse, independently-erring judgments rather than picking one "best" expert — underlies forecasting tournaments, wisdom-of-crowds effects, and portfolio diversification, and it comes with a specific warning transferable to those domains too: the aggregation only helps if you guard against members of the committee having secretly "seen the answer" already (the training-set leakage Domingos flags).
