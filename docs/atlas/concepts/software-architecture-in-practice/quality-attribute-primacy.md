---
type: Concept
title: Quality Attribute Primacy
description: A system's ability to exhibit required qualities like performance or security is set mainly by its architecture, not by its functionality.
book: software-architecture-in-practice
chapters: [2, 4]
tags: [architecture, quality-attributes, design, tradeoffs, non-functional-requirements]
created: 2026-07-12
---

# Quality Attribute Primacy

## Definition

Whether a system will exhibit its desired qualities — performance, security, modifiability, availability — is substantially determined by its architecture, not by getting the functions right. Functionality can almost always be built into any structure; quality attributes cannot, because they depend on how responsibilities are divided and how elements communicate. Architecture is necessary but not sufficient: "the architecture giveth and the implementation taketh away."

## In the Book

Chapter 2 opens with thirteen ways architecture matters and leads with this one first: if a system needs high performance, the architect must manage inter-element communication and shared-resource contention; if it needs modifiability, responsibilities must be assigned so a typical change touches one element, not many; if it needs security, communication paths and access must be controlled and specialized elements introduced. The book is explicit that a good architecture cannot guarantee quality by itself — obscure, tangled code inside a single module can defeat an otherwise ideal architecture — but no amount of careful coding can retrofit modifiability into a system where responsibilities are scattered across the wrong seams. Chapter 4 builds on this by treating quality attributes, not functions, as the requirements that should drive early design decisions, since functionality is comparatively indifferent to structure while quality attributes are not.

## Why It Matters

This reframes what a design review, an architecture diagram, or an early technical decision should be optimized for. Requirements documents are dominated by functional descriptions because they are easy to enumerate, but the properties that determine whether a system succeeds or fails in production — can it survive an outage, can it be changed safely, can it scale — are governed by structural decisions made long before most functionality exists. Any system where "what it does" and "how well it does it" are separable in this way benefits from asking, early, which few structural choices actually control the outcomes stakeholders care about.
