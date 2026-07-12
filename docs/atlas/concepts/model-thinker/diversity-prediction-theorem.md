---
type: Concept
title: Diversity Prediction Theorem
description: A crowd's collective prediction error equals average individual error minus the diversity of individual predictions — an exact mathematical identity, not a tendency.
book: model-thinker
chapters: [3]
tags: [forecasting, aggregation, collective-intelligence, mathematics, measurement]
created: 2026-07-12
---

# Diversity Prediction Theorem

## Definition

For any set of numerical predictions of a true value, the following identity always holds exactly: Many-Model (collective) Error = Average Individual Error − Diversity of Predictions, where diversity is the average squared distance of each prediction from the group's mean prediction. Because diversity is always non-negative, the group average can never be less accurate than the average individual — and it is strictly more accurate whenever the individuals disagree.

## In the Book

Page presents this as a mathematical identity in Chapter 3, distinct from the probabilistic Condorcet jury theorem that precedes it — "we need not test it. It always holds." He walks through a worked numeric example: two models predict a film will win 2 and 8 Oscars respectively; the film actually wins 4. The individual errors are 4 and 16 (squared), averaging to 10. The average prediction, 5, has an error of only 1. The gap — 9 — exactly equals the diversity of the two predictions (each is 3 away from the mean of 5, squared and averaged). Page is explicit that this is the formal engine behind the "wisdom of crowds," and connects it to the observed value of ensemble methods in computer science and to empirical findings — such as the U.S. Federal Reserve deliberately relying on an ensemble of economic models rather than a single one. But he also flags the theorem's limit: it guarantees improvement only over the *average* individual, and if every model shares the same bias, the crowd average inherits that bias too — diversity does not fix systematic error, only idiosyncratic error.

## Why It Matters

This turns "get diverse opinions" from a vague managerial slogan into an exact accounting identity: you can measure how much of your collective error comes from individuals simply being wrong versus from everyone being wrong in the *same* direction. That distinction tells you what to fix — recruit more accurate forecasters if average error dominates, recruit more different ones if lack of diversity dominates — and it explains why three randomly-chosen forecasters can reliably outperform the single historically-best forecaster, since the "best" performer today may not stay best as conditions change.
