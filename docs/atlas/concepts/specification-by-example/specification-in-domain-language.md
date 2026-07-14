---
type: Concept
title: Specification in Domain Language
description: Specifications written in the business's own vocabulary, not invented testing or implementation jargon, stay readable to everyone and need no translation layer.
book: specification-by-example
chapters: [8, 11]
tags: [domain-language, communication, documentation, shared-understanding, requirements]
created: 2026-07-12
---

# Specification in Domain Language

## Definition

When a delivery team invents its own jargon for testing or implementation concepts, business users can't read the specification without a translator — usually the business analyst, who becomes a bottleneck and a source of information loss. Writing specifications in the domain's own vocabulary (Eric Evans's Ubiquitous Language, applied to specifications rather than code) removes the translation step: one consistent language serves business users, testers, developers, and future readers of the documentation alike.

## In the Book

Chapter 8's refinement of the "bad" payroll specification is the concrete demonstration: the original test used an invented concept, "Paycheck Inspector," that means nothing to a payroll business user; Adzic renames it "All checks printed" — using language a payroll clerk would actually use — and separates business concepts (employee name, salary, payment date) from implementation artifacts (database identifiers), which get removed entirely because the domain doesn't need them. He explicitly ties this practice to Eric Evans's Ubiquitous Language from Domain-Driven Design, applying the same principle to specifications rather than to code architecture. Chapter 11 extends this into living documentation over the long term: teams are advised to "evolve a language" deliberately as the system grows, sometimes basing it on personas, and to document their vocabulary's building blocks so the documentation stays consistent as multiple people add to it over years.

## Why It Matters

Any system with two groups of stakeholders who don't share vocabulary — engineers and clinicians, quants and regulators, developers and payroll clerks — pays a permanent translation tax: one side becomes a bottleneck, and information degrades every time it crosses the boundary. Insisting that the artifact both sides rely on (a spec, a contract, a dashboard) is written in the audience's own language, not the producer's internal jargon, removes the bottleneck entirely rather than just documenting around it.
