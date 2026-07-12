---
type: Concept
title: Small-Sample Inference
description: Tiny random samples carry far more statistical information than intuition credits — five random observations already narrow a population's median with 93.75% confidence.
book: how-to-measure-anything
chapters: [3, 9]
tags: [statistics, sampling, intuition, uncertainty]
created: 2026-07-12
---

# Small-Sample Inference

## Definition

The "Rule of Five": there is a 93.75% chance that the median of any population lies between the smallest and largest values in a random sample of just five observations. The logic is a coin-flip argument — the chance all five sampled values fall above the true median is (1/2)^5, and likewise for all falling below, so the chance the median is *outside* the sampled range is 2 × 3.125% = 6.25%, leaving 93.75% that it's inside. The related "Single Sample Majority Rule" (Hubbard's "Urn of Mystery") shows that under maximum uncertainty about a population proportion, a single random observation already has a 75% chance of matching the population's majority value.

## In the Book

Hubbard introduces the underlying intuition in Chapter 3 with a jelly-bean weighing exercise: readers give a 90% CI for the average weight of a jelly bean, then watch that range narrow sharply after just five and then eight randomly sampled weights (true average ≈1.45 grams), demonstrating that people's own calibrated ranges converge quickly on the right answer with very little data. Chapter 9 formalizes this with the Rule of Five itself, illustrated by a hypothetical 10,000-employee company estimating commute times from five random employees (30, 60, 45, 80, 60 minutes) — Hubbard reports that when he polls seminar audiences on whether this sample is "statistically significant," most say no or guess the odds the true median falls in that range at only 50%, when the correct answer is 93.75%. The chapter also covers William Sealy Gosset (the Guinness brewery statistician who published under the pseudonym "Student"), whose t-statistic gives a more precise 90% CI from small samples and, on the same jelly-bean data, nearly matches the naive calibrated estimators' own ranges. He pairs this with the "Urn of Mystery" thought experiment — an urn with an unknown, uniformly-distributed proportion of green vs. red marbles — to show that even a single random draw meaningfully shifts your best bet on the majority color, contrary to almost everyone's intuition that one sample "tells you nothing."

## Why It Matters

The Rule of Five reveals that the common excuse "the sample is too small to mean anything" is usually wrong — it conflates statistical significance thresholds (built for null-hypothesis testing) with the much lower bar of getting *some* usable uncertainty reduction. Anyone facing a decision where "we don't have enough data" is used to justify not measuring at all can use this to see that even minimal, cheap sampling is informative, as long as the goal is uncertainty reduction rather than proof beyond doubt.
