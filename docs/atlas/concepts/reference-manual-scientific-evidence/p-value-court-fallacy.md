---
type: Concept
title: The p-Value Is Not the Probability the Null Is True
description: A statistically significant result tells you what's likely to happen if the null hypothesis is correct, not the probability that the null hypothesis is correct — a distinction courts and lawyers routinely collapse.
book: reference-manual-scientific-evidence
chapters: [6]
tags: [statistics, statistical-significance, legal-standards, hypothesis-testing, misinterpretation]
created: 2026-07-12
---

# The p-Value Is Not the Probability the Null Is True

## Definition

A p-value is the probability of seeing data as extreme as, or more extreme than, the observed data if the null hypothesis were true. It is easy — and wrong — to read a p-value of .05 as "only a 5% chance the null hypothesis is correct." From the frequentist statistical framework the manual describes, a hypothesis is simply true or false; probabilities describe how samples behave under an assumed model, not the model itself. The manual calls the 5% and 1% thresholds "icons of science and the legal process" that are nonetheless "at best useful conventions," not a natural boundary between chance and causation.

## In the Book

The Statistics reference guide documents courts making exactly this error, quoting *Waisome v. Port Authority*: "Social scientists consider a finding of two standard deviations significant, meaning there is about one chance in 20 that the explanation for a deviation could be random," and *Magistrini v. One Hour Martinizing Dry Cleaning*: "a statistically significant... study shows that there is only 5% probability that an observed association is due to chance" — both restating the p-value as if it were the posterior probability of chance. The chapter also separates statistical significance from practical significance: with a large enough sample, "even a tiny effect will be" statistically significant, so a court finding a "statistically significant" disparity (as in *Waisome* itself) may still need to ask whether it was "of limited magnitude" and therefore not legally important. It further warns that repeated testing inflates the odds of a spuriously "significant" finding by chance alone, and that the choice between a one-tailed and two-tailed test can double a reported p-value — meaning the number a court treats as an objective fact is itself sensitive to a judgment call made before the data were seen.

## Why It Matters

This is the statistical cousin of the prosecutor's fallacy: both come from treating "probability of the evidence given the hypothesis" as if it were "probability of the hypothesis given the evidence," two quantities related by Bayes' theorem but not equal to each other without knowing the prior. Anywhere a p-value, a confidence level, or a significance threshold gets reported as a headline number — a scientific paper, a news story, an A/B test result, a courtroom exhibit — this same substitution is available to make, and catching it is the difference between "unlikely to be pure chance" and the much stronger, unearned claim "very likely true."
