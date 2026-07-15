---
type: Concept
title: "Domain-Driven Form: Architecture Grounded in Domain Knowledge"
description: "Architecture that reflects end-user mental models and domain expertise, expressed as abstract base classes and domain structure rather than speculative frameworks."
book: lean-architecture
chapters: [2, 5]
tags: [domain-knowledge, mental-model, architecture, domain-experts, form]
created: 2026-07-15
---

# Domain-Driven Form: Architecture Grounded in Domain Knowledge

## Definition

Lean architecture begins with domain knowledge — the long-standing structures and patterns that domain experts recognize across years of work in a field. These patterns become the foundational form of the system: abstract base classes, key domain entities, and their relationships. This form reflects what end users and domain experts understand the world to be, independent of any specific use case. A banking system has Accounts, Customers, and Ledgers not because a use case mentions them, but because those entities reflect the stable shape of banking itself.

## In the Book

Chapters 2 and 5 emphasize that architecture should capture domain reality, not speculative platforms. Coplien and Bjørnvig contrast this with classical architecture approaches that try to predict every future possibility and build a generalized framework upfront. Instead, Lean architecture works with stakeholders—especially domain experts—in the early project phases to articulate what the system fundamentally *is*. This happens through conversations, site visits, and watching domain experts work.

The book describes how domain experts reveal the abstract structure through examples and patterns. Rather than an architect imposing a framework, the domain experts and end users show the team the entities, relationships, and key distinctions that have mattered in their work for years. These become the abstract base classes. The book notes that Simula, the first object-oriented language (1965–1967), was designed with exactly this goal: to reflect end-user world models in the system design. But that vision was lost in decades of methodology and programming language obfuscation. Lean architecture restores it.

## Why It Matters

Grounding architecture in domain knowledge produces two benefits: longevity and adaptability. Because the form reflects stable, timeless concepts rather than guesses, it endures even as requirements and use cases change. Adding a new type of transfer doesn't rearchitect the Account concept; it's a variation on stable foundations. Second, because the architecture reflects how domain experts actually think about their world, developers and domain experts can communicate using the same vocabulary. The code becomes a literal expression of domain understanding, not a translation layer requiring intermediaries. This alignment is what makes Agile change sustainable — the team doesn't have to decipher an architecture that was designed for a fictional future.

