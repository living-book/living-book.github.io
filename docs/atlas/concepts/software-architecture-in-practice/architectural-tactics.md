---
type: Concept
title: Architectural Tactics
description: A design decision that moves one quality attribute response in isolation, without resolving tradeoffs — the atomic unit beneath a pattern.
book: software-architecture-in-practice
chapters: [4, 13]
tags: [design-decisions, quality-attributes, patterns, catalog, tradeoffs]
created: 2026-07-12
---

# Architectural Tactics

## Definition

A tactic is a design decision that influences the achievement of a single quality attribute response — it directly affects how the system reacts to a given stimulus. Crucially, a tactic contains no built-in tradeoff resolution; it just moves one dial. Architectural patterns, by contrast, bundle multiple tactics together along with the tradeoffs among them already baked in. The book's stated contribution is not inventing tactics but isolating, cataloging, and naming techniques architects were already using informally.

## In the Book

Chapter 4 introduces tactics as the layer between a quality attribute requirement and a chosen architectural pattern: patterns are often too coarse or don't quite fit, and understanding the tactics inside a pattern lets an architect adapt or augment it to hit a specific quality goal. Chapters 5 through 11 each provide a tactics catalog for one quality attribute — availability tactics like fault detection (ping/echo, heartbeat), recovery (rollback, retry, exception handling), and prevention (removal from service); performance tactics for managing demand and resources; security tactics for detecting, resisting, and reacting to attacks — with each tactic explained as a targeted lever, not a complete solution. Chapter 13 then generalizes: it shows how the tactics catalogs for each quality attribute were constructed systematically (by examining possible responses to the ways things can go wrong), how tactics relate to patterns, and how multiple tactics get combined and reconciled within one design, since real designs pull tactics from several quality attributes at once and the tradeoffs between them are exactly the part tactics alone don't resolve.

## Why It Matters

Separating the tactic (a single-purpose lever) from the pattern (a pre-packaged bundle of levers with tradeoffs already made) gives a vocabulary for design flexibility below the level of "pick a pattern off the shelf." It explains why patterns sometimes need adapting rather than adopting wholesale — the pattern was optimized for a different mix of quality goals than yours — and it gives a shared name for the move of isolating exactly which small decision is responsible for a given desirable or undesirable system behavior. Any field with reusable, higher-level solution templates (patterns, playbooks, protocols) can ask the same question: what are the atomic levers this template bundles, and which one do I actually need to pull.
