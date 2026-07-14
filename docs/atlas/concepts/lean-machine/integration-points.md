---
type: Concept
title: Integration Points
description: The real control points of a development process are the events where independent design cycles must converge, not the phase-gate checklists layered on top of them.
book: lean-machine
chapters: [10]
tags: [synchronization, coordination, design-cycles, convergence, product-development]
created: 2026-07-12
---

# Integration Points

## Definition

An integration point is an event — a prototype build, a system test — where every subsystem's design work must physically or logically converge before the project can proceed. Regardless of how many redesign iterations a subsystem needs, it has to be ready by the integration point, or the point slips and every downstream subsystem waits. Integration points, not phase gates, are the true pacing and control mechanism of product development: "everything has to converge at the integration points."

## In the Book

Chapter 10 reframes the discovery from the Product Development Limit Curve: the reason the curve has the shape it does is that different subsystems have design-iteration cycles of very different lengths, and the dominant long cycles determine how much time is available before an integration point. If a chassis takes six months per design loop while an electrical harness takes one, the harness team can refine six times while the chassis team refines once — and a mismatch this large routinely produces parts that don't fit together at the prototype build, because the "faster" subsystem has drifted several design generations ahead of the slower one. Oosterwal's conclusion overturns years of prior improvement work: value-stream-mapping the phase-gate process to streamline individual activities was largely wasted effort, because it didn't touch what actually controlled outcomes — synchronizing design-cycle lengths across subsystems and shortening the longest one. Once integration points are seen as the leverage points, "phases and gates gave way to development cycles and integration points" as the operating model.

## Why It Matters

This concept separates the visible schedule structure of a project (its milestones) from the structure that actually governs it (the pace of the slowest converging workstream). It's the product-development analogue of a critical-path or bottleneck argument: optimizing any activity that isn't gating the next convergence event does nothing for the whole, while synchronizing — even slowing down a fast component to match a slow one — can measurably speed up delivery. The lesson generalizes to any multi-team effort with a hard convergence event: a merge, a launch, a joint venture close.
