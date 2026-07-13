---
type: Concept
title: Power-Law Distributions
description: Distributions produced by positive feedback (more begets more) have long tails where extreme events are far more common and far more extreme than a normal distribution would predict.
book: model-thinker
chapters: [6]
tags: [distributions, extreme-events, feedback, measurement, forecasting]
created: 2026-07-12
---

# Power-Law Distributions

## Definition

A power-law (long-tailed) distribution is one where the probability of an event is proportional to its size raised to a negative exponent, so probability falls off much more slowly than in a normal distribution — producing far more extreme outliers than intuition calibrated on bell curves expects. Page's illustration: if human height followed a power law calibrated to the same mean as city population size does, the U.S. would contain one person as tall as the Empire State Building and 180 million people under 7 inches tall.

## In the Book

Chapter 6 argues that long tails arise from non-independence, typically positive feedback — what sociologist Robert Merton called the Matthew effect ("unto every one that hath shall be given"). Page walks through two generative mechanisms in detail: the preferential attachment model, where new arrivals join existing entities in proportion to those entities' current size (explaining city population sizes, book sales, and web-link counts), and self-organized criticality (explaining traffic jams, forest fires, earthquakes, and war deaths). He shows the practical stakes with a concrete comparison: if terrorist-attack deaths followed a power law with exponent 2, a one-in-a-million event involves nearly 800 deaths; if the same mean and a normal distribution were assumed instead, a one-in-a-million event would involve fewer than 50 — a roughly sixteen-fold underestimate of tail risk from picking the wrong distributional family. He also introduces Zipf's Law as the special case where exponent equals 2, verified against real 2016 U.S. city-population data (each city's rank times its population lands near a constant, ~8 million), and gives a diagnostic: power laws appear as straight lines on a log-log plot, while lognormal distributions curve away.

## Why It Matters

Recognizing that a phenomenon is power-law rather than normally distributed changes what "prepare for the worst case" means in practice — under a normal distribution, extreme events are effectively impossible to plan for and safe to ignore, while under a power law they are rare but *routine enough to budget for*, whether the domain is financial risk, natural disasters, viral content, or firm size. Misclassifying a fat-tailed process as normal is one of the most consequential and common measurement errors in forecasting and risk management.
