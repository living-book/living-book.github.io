---
type: Concept
title: Linear Programming (Feasible Region and Corner-Point Optimization)
description: When every constraint and the objective are linear, the optimum always sits at a corner of the feasible region, so a search over infinite points reduces to checking a handful of vertices.
book: mathematics-for-economics-and-business
chapters: [8]
tags: [optimization, constraints, decision-making, resource-allocation, geometry]
created: 2026-07-14
---

# Linear Programming (Feasible Region and Corner-Point Optimization)

## Definition

A linear programming problem optimises a linear objective function subject to a system of linear inequality constraints. Each inequality (like 2x + y ≤ 4) defines a half-plane, tested by picking any point not on the boundary line and checking whether it satisfies the inequality; the intersection of all the half-planes is the feasible region — the set of points satisfying every constraint simultaneously. The optimum of the objective function is always attained at one of the corners (vertices) of this feasible region, never at an interior point, which converts an infinite search into a check of a small, enumerable set of points.

## In the Book

Section 8.1 builds the feasible region concept from a single inequality (y ≥ x, then 2x + y < 4), using a test point like (3, 2) to decide which side of the boundary line to shade, then layers multiple inequalities to form a bounded polygon — in one worked example a triangle with corners (0, 0), (0, 2) and (4, 0). To find the optimum over this region the book introduces the "family of lines" sweep method: superimposing a family of parallel lines representing the objective function at different constant values and sliding it across the feasible region until it touches the region at exactly one point — for one problem this identifies (12, 0) as the solution. The book explicitly notes this corner-point result is "not simply a coincidence" and proves it generally, then works a four-corner case, (0, 6), (1, 4), (4, 1) and (8, 0), by directly evaluating the objective at each vertex. It also covers the two special cases that break the simple story: an unbounded feasible region (open at one side, so no finite maximum may exist) and problems where the objective's sweep line lies parallel to one edge of the region, giving infinitely many optimal solutions along that whole edge rather than a single point. Section 8.2 then shows how a resource-allocation problem stated in words (e.g. production planning under labour and material limits) is translated into this constraint-and-objective form.

## Why It Matters

The corner-point theorem is the reason linear programming is computationally tractable at any scale — it says the search space for "best combination under multiple hard constraints" is never the whole continuous region but only its vertices, which is the structural fact underlying the simplex method and every large-scale resource-allocation solver in industry. More broadly, the sweep-and-touch construction is a general recipe for constrained optimisation with inequality (rather than equality) constraints — where Lagrange multipliers assume an equality binds exactly, linear programming's feasible-region approach handles "at most" and "at least" limits, which is the more common shape of real resource constraints (budgets, capacity, headcount).
