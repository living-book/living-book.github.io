---
type: Concept
title: "Commonality and Variation: Identifying What Stays and What Changes"
description: "A design technique that explicitly separates stable domain elements from those that vary, using this distinction to structure architecture that resists brittleness."
book: lean-architecture
chapters: [5]
tags: [design-technique, commonality, variation, domain-structure, flexibility]
created: 2026-07-15
---

# Commonality and Variation: Identifying What Stays and What Changes

## Definition

Commonality and Variation is a design practice (descended from feature-oriented domain analysis) that requires teams to explicitly identify which elements of a domain remain constant across all scenarios and which change based on context or requirement. This distinction becomes the organizing principle of architecture. Elements that are common become stable abstractions; elements that vary become extension points. The result is an architecture that can absorb change in high-variation areas while keeping low-variation foundations fixed.

## In the Book

Chapter 5, "What the System Is, Part 1: Lean Architecture," introduces commonality and variation as a fundamental design step, coming after stakeholder engagement and problem definition but before final implementation choices. The book presents this as tacit at first (developers and domain experts recognize patterns in examples) and then explicit (writing down which things change together and which are always the same). Making commonalities and variations explicit prevents them from being scattered unconsciously across the code.

The book illustrates this through domain examples. In a banking context, the concept of Account is common (every transfer, deposit, and withdrawal involves an account). The *type* of account varies (savings, checking, investment). Rules about minimum balance vary; rules about currency don't. By naming these distinctions early, architects can design accounts to be extensible at the right boundaries. An abstract Account base class captures commonality; derived types or strategies capture variation. This keeps the system from being over-constrained and equally from being a maze of irrelevant flexibility.

## Why It Matters

Many systems fail because they either lock in too much (every change requires rearchitecture) or are so flexible they become unmaintainable (variations everywhere, no coherent pattern). By explicitly separating the two, a team can apply different design strategies to each. Commonalities warrant careful, up-front thought because they'll be expensive to change later. Variations can be designed for local flexibility without global impact. This also aligns decision-making: domain experts focus on commonalities (what defines the essence of a domain entity); product managers and users drive variation (which flavors the market needs). The separation makes priorities clear and prevents premature generalization.

