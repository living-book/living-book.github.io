---
type: Concept
title: Monte Carlo Risk Modeling
description: Simulating thousands of randomly sampled scenarios from input ranges reveals a decision's true probability of loss, replacing ambiguous "high/medium/low" risk labels.
book: how-to-measure-anything
chapters: [6]
tags: [risk, simulation, uncertainty, decision-modeling]
created: 2026-07-12
---

# Monte Carlo Risk Modeling

## Definition

A Monte Carlo simulation generates a large number of scenarios by randomly drawing a specific value for each uncertain input (from its calibrated probability range), computing an output for that scenario, and repeating thousands of times — producing a full probability distribution of outcomes instead of a single point estimate. Risk, in this framing, is simply the range of possible losses implied by using ranges instead of fixed point values for costs and benefits: if every input in a business case were known exactly, there would be zero risk by definition, so risk is a direct mathematical consequence of using honest ranges rather than an extra "risk score" bolted on afterward.

## In the Book

Chapter 6 first attacks the alternative: ordinal risk-scoring schemes ("high/medium/low" or 1-to-5 scales) that Hubbard argues add rounding error and give identical scores to wildly different risks — his diagnostic example is asking whether a "medium risk" investment with 15% ROI beats a "high risk" one with 50% ROI, which the labels cannot answer. He traces Monte Carlo methods to Enrico Fermi's 1930s work estimating neutron behavior, and to Stanislaw Ulam, John von Neumann, and Nicholas Metropolis's use of early computers for the Manhattan Project, with Ulam naming the method after the Monte Carlo casino in honor of his gambling uncle. Two client cases ground the mechanism: a Chicago investment firm's CIO who claimed to have "a pretty good handle on risk" but admitted her team just "picked a number" for the IT benefit in basis points — meaning she had no ranges to feed a real risk calculation and was, per Hubbard, not doing risk analysis at all; and a large healthcare system's cybersecurity group, where Hubbard Decision Research replaced a 1-to-9 additive scoring model with an Excel tool running 5,000 simulations per risk event, letting the director finally answer concrete questions like "what's the chance total losses exceed $10 million over five years?"

## Why It Matters

Monte Carlo modeling converts vague risk talk into an actual probability distribution over outcomes, which is what lets you compare options, set risk tolerances, and — crucially — feed the result into a value-of-information calculation. It generalizes to any domain where multiple uncertain inputs combine nonlinearly to produce an outcome: project cost overruns, portfolio returns, epidemiological forecasts, or engineering tolerances all benefit from replacing single "best guess" numbers with sampled ranges.
