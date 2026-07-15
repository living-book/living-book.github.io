---
type: Concept
title: Constrained Optimization via Lagrange Multipliers
description: Fold a constraint into the objective function with a multiplier λ, and solving for λ both finds the optimum and prices the constraint itself.
book: mathematics-for-economics-and-business
chapters: [5]
tags: [optimization, constraints, calculus, shadow-price, decision-making]
created: 2026-07-14
---

# Constrained Optimization via Lagrange Multipliers

## Definition

To optimise an objective function f(x, y) subject to a constraint w(x, y) = M, form the Lagrangian g(x, y, λ) = f(x, y) + λ[M − w(x, y)], then solve the three simultaneous equations ∂g/∂x = 0, ∂g/∂y = 0, ∂g/∂λ = 0 for x, y, and λ. The third equation always reduces to the original constraint, so it is automatically satisfied at any solution. The multiplier λ is not a throwaway artifact of the algebra: its value equals ∂g/∂M — the approximate change in the optimal objective value produced by relaxing the constraint by one unit.

## In the Book

Section 5.6 works a pure-math example first — optimising x² − 3xy + 12x subject to 2x + 3y = 6 — building g(x, y, λ) = x² − 3xy + 12x + λ(6 − 2x − 3y), then solving the resulting three-equation system by elimination to reach the optimum (−1, 8/3) with λ = 1. It then applies the method to a monopolist producing two goods with joint cost TC = 10Q₁ + Q₁Q₂ + 10Q₂ and a fixed production quota Q₁ + Q₂ = 15, finding maximum profit 475 at (Q₁, Q₂) = (10, 5) with λ = 30. The book then explicitly interprets that 30: rather than re-solving the whole problem with the quota raised from 15 to 16, it shows ∂g/∂M = λ directly gives the approximate change in optimal profit from a one-unit quota increase — profit rises by about 30, to roughly 505. A further example uses the method on a Cobb–Douglas production function subject to a cost constraint to derive that at the optimum the ratio of marginal product to input price is equal across all inputs — the general condition for efficient input allocation.

## Why It Matters

Lagrange's method turns "the best point given this restriction" into a single system to solve, working for nonlinear constraints and any number of variables where substitution becomes unworkable — but its real export is the multiplier itself: λ is a shadow price, telling you exactly how much the optimal outcome would improve per unit of relaxed constraint, without redoing the whole optimisation. Any time a system is bound by a scarce resource — budget, capacity, time, a regulatory quota — this shadow-price reading answers "what is loosening this constraint worth?", which is usually the more actionable question than "what is the optimum under the current constraint?"
