---
type: Concept
title: "What vs. How: Form and Functionality"
description: "The architecture of a system (what it is) differs fundamentally from its functionality (what it does), requiring separate design considerations."
book: lean-architecture
chapters: [2, 5]
tags: [architecture, design, form, function, separation-of-concerns]
created: 2026-07-15
---

# What vs. How: Form and Functionality

## Definition

Every software system has two distinct designs: its form (the stable structural organization reflecting domain knowledge) and its functionality (the services and tasks it performs). The architecture embodies what the system *is* — its fundamental shape — while use cases and algorithms describe what it *does*. These two concerns drive different stakeholder perspectives and decision rhythms, and conflating them leads to architecture that neither endures nor adapts.

## In the Book

Coplien and Bjørnvig structure the entire book around this duality. Chapter 2 introduces "what the system is" as the terrain — the stable platform reflecting long-standing domain expertise — while "what the system does" is the animation that brings it to life for end users.

The book contrasts this with classical architecture approaches that rush into implementation details. Instead, Lean architecture captures form early (through abstract base classes that express domain structure) but defers implementation of functionality until requirements clarify. A house's foundation and load-bearing walls (form) can be decided long before the interior decoration (implementation). In software, deciding that a system needs accounts, transfers, and roles (form) is separate from deciding how money moves in a specific transfer scenario (functionality). This separation lets developers reshape the system's responses to users without rearchitecting the stable domain model underneath.

## Why It Matters

This distinction unlocks two separate optimization paths. The domain form — what the system is — changes slowly and can be designed for longevity using deep domain knowledge and stakeholder collaboration. Functionality — what the system does — changes frequently, driven by market feedback and emerging use cases. By keeping them separate in both design and code, a team can stabilize the architecture (reducing rework) while remaining agile in feature delivery (responding to change). It also clarifies stakeholder roles: domain experts shape what the system is, while end users and business drive what it should do.

