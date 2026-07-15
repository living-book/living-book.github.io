---
type: Concept
title: Outside-In Development
description: "An implementation approach starting from acceptance criteria and working inward, writing acceptance tests before unit tests, and unit tests before code."
book: bdd-in-action
chapters: [10]
tags: [development-approach, test-driven-development, design, implementation]
created: 2026-07-15
---

# Outside-In Development

## Definition

Outside-In Development is an approach where developers work from the outside edges of a system inward: start with high-level acceptance criteria, write executable specifications that express those criteria, then implement whatever code is needed to make those specifications pass. At each level—acceptance tests, unit-level specifications, implementation code—developers begin by writing the test or specification first, then implement the minimal code that satisfies it. This contrasts with inside-out approaches that write code first and verify it afterward.

## In the Book

Smart describes Outside-In Development in chapter 10 as the natural consequence of writing executable specifications. He explains that "Developers practicing BDD typically use an outside-in approach. When they implement a feature, they start from the acceptance criteria and work down, building whatever is needed to make those acceptance criteria pass. The acceptance criteria define the expected outcomes, and the developer's job is to write the code that produces those outcomes. This is a very efficient, focused way of working" (1681-1687). He then shows the concrete flow: "Start with a high-level acceptance criterion / Automate the acceptance criteria scenarios / Implement the step definitions / Understand the domain model / Write the code you'd like to have / Use the step definition code to specify and implement the application code" (1423-1427). The step definitions themselves then become specifications that guide lower-level unit tests. For example, when a step definition creates an account with `Account.ofType(type).withInitialBalance(amount)`, the developer hasn't yet written the Account class—they write a unit test that specifies how Account should behave, implement the Account class to pass that test, then the step definition is automatically satisfied.

## Why It Matters

Outside-In Development produces a natural hierarchy of specifications aligned with business outcomes. Because acceptance tests drive the work, no code gets written that doesn't contribute to a feature, eliminating speculative "architecture" or utilities that might be useful someday but distract from the goal. The approach also surfaces design problems early when they're cheap to fix—if acceptance tests are hard to write, the system boundary is poorly designed. Working from acceptance criteria down also keeps developers focused on solving the customer's problem rather than optimizing implementation details. Each level of tests documents the corresponding level of design, so the relationship between high-level requirements and low-level code structure remains visible and coherent.
