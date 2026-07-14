---
type: Concept
title: Specifying Collaboratively
description: Requirements written by one role in isolation end up either unreadable or unmaintainable — specifications must be built jointly by business, testing, and development perspectives together.
book: specification-by-example
chapters: [2, 6]
tags: [collaboration, requirements, teams, communication, shared-understanding]
created: 2026-07-12
---

# Specifying Collaboratively

## Definition

A specification produced by any single role working alone predictably fails: business analysts and testers writing without developers produce documents too hard to automate or maintain; developers writing alone produce specifications too tightly coupled to implementation for anyone else to read. Specifying collaboratively means building the specification through structured conversation among business, testing, and development perspectives at once — the shared discussion is what produces a document that is simultaneously precise, testable, and understandable.

## In the Book

Chapter 6 documents this failure pattern repeatedly across interviewed teams: at LMAX, Jodie Parker found developers and testers each assumed the other wasn't interested in the conversation, until they discovered testers could catch code-base impacts developers missed; Marta Gonzalez Ferrero describes testers handing over FitNesse tables that developers "couldn't automate" until the two groups started working together; Lisa Crispin at ePlan Services concluded she should have paired with developers because writing tests alone left her with too many hard-to-refactor specifications. The chapter's central recommended pattern is the "Three Amigos" meeting — one developer, one tester, one business analyst — as a lighter-weight alternative to large all-team specification workshops (which the book recommends when a team is just starting out, as uSwitch did, because they surface obscure business rules early). Rob Park's team institutionalized this: the direct output of their Three Amigos session is the Given-When-Then feature file itself, agreed as content-complete before any code is written.

## Why It Matters

Whenever one function of an organization writes a specification, contract, or plan for another function to execute, the same three failure modes recur: it's incomplete (missing what only the executor knows), unmaintainable (missing what only the writer's audience needs), or misunderstood (missing the shared vocabulary that only conversation builds). Structuring a small, deliberately mixed conversation — not a big meeting, not a solo document — before committing to a plan is a transferable fix wherever roles hand work to each other across a knowledge boundary.
