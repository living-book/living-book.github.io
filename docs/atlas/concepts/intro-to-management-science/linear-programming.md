---
type: Concept
title: Linear Programming
description: Modeling a decision as decision variables, a linear objective to maximize or minimize, and linear constraints, then solving for the optimal combination.
book: intro-to-management-science
chapters: [2]
tags: [optimization, modeling, constraints, decision-making, resource-allocation]
created: 2026-07-12
---

# Linear Programming

## Definition

Linear programming (LP) formalizes a decision problem as three pieces: decision
variables (the controllable choices), a linear objective function to maximize
or minimize (usually profit or cost), and a set of linear constraints (usually
limited resources) that the variables must satisfy. The optimal solution is the
combination of variable values that best satisfies the objective without
violating any constraint. As the book puts it, "problem formulation, or
modeling, is the process of translating the verbal statement of a problem into
a mathematical statement."

## In the Book

Chapter 2 builds the method entirely through the Par, Inc. golf-bag example.
Par, Inc. must decide how many standard bags (S) and how many deluxe bags (D)
to produce, given that each bag consumes a different number of hours in
cutting-and-dyeing, sewing, finishing, and inspection-and-packaging, and only a
fixed number of hours are available in each department. The book walks through
formulating the objective (Max 10S + 9D, the profit contribution per bag),
writing each department's hour limit as a constraint (e.g., 7/10 S + 1D ≤ 630
for cutting and dyeing), and then solving graphically: plotting the feasible
region bounded by the constraints and finding the extreme point where the
objective function is highest (540 standard bags, 252 deluxe bags). The
chapter generalizes this into a repeatable formulation procedure — understand
the problem, describe the objective, describe each constraint, define decision
variables, then write the objective and constraints in terms of those
variables — and shows the same structure recurring across a portfolio problem
(funds constrained by budget) and a media-selection problem (spend constrained
by budget and media availability).

## Why It Matters

Linear programming gives a disciplined way to convert "we have limited
capacity and competing demands on it" into a solvable structure, rather than
leaving the trade-off to intuition or trial and error. Once a problem is cast
as variables, an objective, and constraints, the same solution machinery
applies whether the scarce resource is factory hours, investment capital,
advertising budget, or shelf space — which is precisely why the formulation
discipline, more than any specific numeric answer, is the exportable skill.
