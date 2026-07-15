---
type: Concept
title: "DCI Architecture: Data, Context, Interaction"
description: "An architectural pattern that maps user mental models and use case algorithms directly into code through data objects, context classes, and role methods that bridge domain structure and behavior."
book: lean-architecture
chapters: [8, 9]
tags: [dci, architecture-pattern, roles, mental-model, use-cases]
created: 2026-07-15
---

# DCI Architecture: Data, Context, Interaction

## Definition

Data, Context, Interaction (DCI) is an architectural pattern that makes end-user mental models executable in code. It separates domain objects (data) — which capture stable, timeless entities like Account or Person — from the algorithms and interactions (context and roles) that animate them for specific use cases. A role method lives in a trait or role class, not in the domain class, so a single use case scenario is readable as a coherent narrative, and the domain objects themselves stay clean and focused on structure rather than behavior.

## In the Book

Chapter 9 develops DCI in detail, with examples in C++, Ruby, Python, Scala, and Smalltalk. The book frames DCI as the answer to a decades-old problem in object-oriented programming: how to capture user mental models in code without scattering use case logic across many domain classes. In a money transfer scenario, the traditional object approach puts transfer logic inside an Account class, entangling the concept of "account" (a domain entity) with the concept of "account in a transfer" (a context-specific role the account plays). DCI separates these: an Account class stays simple, capturing only what an account *is*. A MoneyTransferContext class orchestrates the scenario, binding accounts to roles (TransferSource, TransferSink) and expressing the algorithm as a sequence of role method calls that read like the end user's understanding of what happens.

The book illustrates this through the Account example: transferring money requires roles for source, sink, and the context that binds them. The role methods (withdraw, deposit, verify) are methodful objects that carry the interaction logic, while domain objects carry only state. This separation lets a developer read the context code and see exactly how the use case unfolds without decoding scattered logic across multiple classes.

## Why It Matters

DCI bridges the long-standing gap between the end user's mental model and the developer's code. It makes algorithms traceable to use cases, so changes in requirements map cleanly to localized code changes. It improves testability and code comprehension because a single scenario can be read as one coherent flow. It also redefines what "object orientation" means: not "put methods in classes" but "make structure and behavior alignable with human understanding." For systems that must change frequently (most modern software), this alignment is the difference between adaptive code and brittle code.

