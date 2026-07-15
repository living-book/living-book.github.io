---
type: Concept
title: Price Elasticity of Demand
description: A unit-free ratio of percentage changes — not absolute changes — that tells whether raising or lowering price will raise or lower total revenue.
book: mathematics-for-economics-and-business
chapters: [4]
tags: [measurement, economics, calculus, decision-making, sensitivity]
created: 2026-07-14
---

# Price Elasticity of Demand

## Definition

Price elasticity of demand, E, is the ratio of the percentage change in quantity demanded to the percentage change in price: E = (%ΔQ)/(%ΔP), which simplifies to E = (P/Q)(ΔQ/ΔP), or in the limit, the point elasticity E = (P/Q)(dQ/dP). Because demand curves slope downward, E is always negative, so economists work with its magnitude |E| and classify demand as inelastic if |E| < 1, unit elastic if |E| = 1, and elastic if |E| > 1.

## In the Book

Section 4.5 motivates elasticity by asking what a price change does to total revenue (TR = PQ) — a question the raw slope of the demand curve cannot answer because it mixes absolute price and quantity units that aren't comparable. The book first computes an approximate "arc elasticity" using averaged endpoint values — working the demand function P = 200 − Q² for a price fall from 136 to 119, averaging P to 127.5 and Q to 8.5, and getting E ≈ −0.88 — then shows this is only an estimate over a stretch of the curve, and derives the exact "point elasticity" E = (P/Q)(dQ/dP) by letting the arc shrink to a point. A separate worked example (P = 200 − Q²) computes E = −1.5 at a specific price and shows |E| > 1, so demand there is elastic. The section then connects elasticity directly back to marginal revenue, deriving that MR = P(1 + 1/E), which is the mathematical bridge between the elasticity concept and the marginal-analysis machinery of the previous section.

## Why It Matters

Elasticity solves a problem that a raw derivative can't: comparing sensitivity across quantities measured in different units (dollars vs. tons, minutes vs. dollars) by converting both changes to percentages first. Whenever a decision-maker needs to know whether nudging one lever up will move an outcome by more or less than proportionally — pricing, taxation, wages, interest rates — this ratio-of-percentage-changes construction, and the elastic/inelastic/unit-elastic trichotomy it produces, is the general-purpose tool, independent of the specific economic setting it was built for.
