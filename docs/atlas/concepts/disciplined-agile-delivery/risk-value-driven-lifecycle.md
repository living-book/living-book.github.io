---
type: Concept
title: "Risk-Value Driven Lifecycle"
description: "Prioritize work not just by stakeholder value but by risk exposure, using explicit milestone gates to surface and kill doomed projects early, reducing wasted investment."
book: disciplined-agile-delivery
chapters: [1]
tags: [risk, lifecycle, milestones, viability, value]
created: 2026-07-15
---

# Risk-Value Driven Lifecycle

## Definition

A risk-value lifecycle extends value-driven agile (deliver high-value features first) by explicitly treating risk as a priority criterion alongside value. Work items addressing key project risks—architectural unproven technology, stakeholder consensus, regulatory unknowns—bubble up the same way high-value features do. The lifecycle then gates advancement with explicit, lightweight viability milestones where stakeholders formally assess whether the project should continue, killing or reprioritizing efforts based on evidence of success or failure rather than optimistic planning.

## In the Book

Chapter 1 lays out the six explicit milestones that punctuate the DAD lifecycle:

1. **Stakeholder Consensus** (end of Inception): Do stakeholders agree on the vision? The book notes that organizations should expect to cancel 10–25% of projects at this gate—agreement is hard, and early cancellation saves dramatically compared to failure late in construction.

2. **Proven Architecture** (early Construction): The architecture is not proven by models or analysis, only by working code. A "vertical slice" or "steel thread" through all architectural tiers proves the architecture can support actual requirements. This addresses the single largest source of technical risk in IT projects.

3. **Continued Viability** (periodic, typically every 1–2 months): Stakeholders explicitly assess whether the project remains worth pursuing. The book acknowledges this rarely happens in pure Scrum because stakeholders have political inertia; DAD makes it a formal, repeatable review.

4. **Sufficient Functionality** (end of Construction): Enough features are complete to justify the cost and risk of transition. The term "minimally marketable release" (MMR) names this precisely—shipping more than necessary wastes resources; shipping less leaves value on the table.

5. **Production Ready** (end of Transition): Operations and support staff confirm the solution is actually deployable and supportable in the target production environment.

6. **Delighted Stakeholders** (post-deployment): The ultimate measure—do users find value in the solution in real operation?

The risk-value framing also shapes daily work. Teams simultaneously pursue high-value features *and* features that reduce architectural, technical, or stakeholder-alignment risk. A risky architectural assumption or regulatory unknown moves up the backlog even if the stakeholder doesn't yet see its business value, because unaddressed risk kills projects.

## Why It Matters

Risk-value lifecycle transforms agile from an optimistic, "ship value continuously" model into one that acknowledges high-stakes project failure. The explicit milestones create forcing functions: stakeholders cannot drift passively into a failing project if they are formally asked "should we continue?" every 1–2 months. The risk prioritization ensures teams discover and address showstoppers early—when fixing them is cheap—rather than late—when fixing or living with them is catastrophically expensive. This is particularly powerful in regulated and large-scale contexts where a missed regulatory requirement or architectural flaw can doom a multi-year, multi-million-dollar effort. The combination of continuous value delivery with periodic risk gating gives enterprises confidence in agile where pure Scrum feels reckless.

