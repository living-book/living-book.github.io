---
type: Concept
title: Simulation as Experimentation
description: Build a model relating controllable and probabilistic inputs to an output, then generate many randomly sampled scenarios to see the output's full range and risk of loss, without touching the real system.
book: intro-to-management-science
chapters: [12]
tags: [uncertainty, risk, modeling, probability, experimentation]
created: 2026-07-12
---

# Simulation as Experimentation

## Definition

Simulation builds a model that relates controllable inputs (decisions) and
probabilistic inputs (uncertain quantities) to an output of interest, then
generates many randomly sampled values for the probabilistic inputs to see the
resulting distribution of outputs — most often to assess risk of loss before
committing real resources. The book is explicit about a boundary condition
that separates it from optimization: "Simulation is not an optimization
technique. It is a method that can be used to describe or predict how a
system will operate given certain choices for the controllable inputs and
randomly generated values for the probabilistic inputs."

## In the Book

Chapter 12 introduces simulation through PortaCom's decision to launch a new
portable printer, where selling price ($249) and marketing costs are known but
direct labor cost, parts cost, and first-year demand are uncertain. The book
first tries what-if analysis by hand: plugging in a base-case scenario
(profit of $710,000), then a worst-case scenario (all three uncertain inputs
at their worst simultaneously, a $847,000 loss) and a best-case scenario
(a $2,591,000 profit) — and notes this leaves management with only three
points, no sense of how likely each is. The chapter then generalizes the
approach to a full simulation that samples probability distributions for each
uncertain input many times over, producing a distribution of possible profit
outcomes rather than three anecdotes. The same structure is reapplied later in
the chapter to an inventory-policy problem and to simulating the Hammondsport
Savings Bank ATM waiting line, and the "Call Center Design" case shows a real
company using waiting-line simulation to size a call center's staffing before
changing its actual service program.

## Why It Matters

Simulation lets a decision-maker rehearse a system's behavior under
uncertainty — including its downside risk — without experimenting on the real
system, and without pretending a single best-guess forecast captures what
could happen. It sits deliberately apart from optimization: rather than
solving for a single "best" answer, it shows the full range of outcomes a
decision could produce, which is often the more honest and more useful
question when the future is genuinely uncertain rather than merely unknown.
