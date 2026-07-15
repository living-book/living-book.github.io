---
type: Concept
title: Sensitivity Analysis and Shadow Prices
description: After solving an optimization model, measure how much its inputs could change before the optimal decision itself would change, and what one more unit of a constraint is worth.
book: intro-to-management-science
chapters: [3]
tags: [optimization, uncertainty, robustness, valuation, decision-making]
created: 2026-07-12
---

# Sensitivity Analysis and Shadow Prices

## Definition

Sensitivity analysis asks how much a linear program's coefficients — profit
per unit, or the amount of a resource available — can change before the
optimal solution itself would change. Two numbers do the work: the range of
optimality for each objective coefficient (how far it can move while the
current decision stays best) and the dual value, "the change in the objective
function value per unit increase in a constraint's right-hand side" — what
economists elsewhere call a shadow price, the marginal worth of one more unit
of a scarce resource.

## In the Book

Chapter 3 reopens the Par, Inc. golf-bag problem from Chapter 2 to show why a
single optimal answer isn't the end of the analysis. It asks what happens if
the profit contribution for the standard bag falls from $10 to $8.50, and
shows that as long as an objective coefficient stays within its computed range
(for the deluxe bag, the book works through whether that range is a
comfortable $6.67–$14.29 or a fragile $8.90–$9.25), the same 540-standard/252-
deluxe production plan remains optimal — so management doesn't need to resolve
the whole model every time an estimate shifts. It then turns to the
right-hand sides: because the optimal solution uses all 630 available hours of
cutting-and-dyeing time, the book computes the dual value of that constraint
($4.375) — the added profit from one more hour — and cautions that this
per-unit value predicts the effect of resource changes only within a computed
range, and only for constraints that are actually binding at the optimum.

## Why It Matters

A single optimal solution invites false confidence in inputs that were only
estimates. Sensitivity analysis lets a decision-maker separate the numbers
worth double-checking (those near the edge of their range of optimality) from
the ones that don't matter much, and it converts a scarce resource from an
abstract constraint into a priced object — telling you exactly how much it
would be worth to acquire more of it, which is the basis for any real
build-versus-buy-more-capacity decision.
