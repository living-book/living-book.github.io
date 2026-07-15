---
type: Concept
title: Feature Injection
description: "A technique for identifying and prioritizing features by first discovering business value, then injecting features that can deliver it."
book: bdd-in-action
chapters: [3]
tags: [requirements, business-alignment, value-discovery, prioritization]
created: 2026-07-15
---

# Feature Injection

## Definition

Feature Injection is a requirements-discovery process that works in two steps: "hunt the value" to identify business goals, then "inject the features" that will deliver that value. Instead of starting with a customer's requested feature, Feature Injection begins by understanding why that feature matters to the business, discovering the underlying business goal through repeated questioning, and then proposing features that solve the right problem. The approach recognizes that stakeholders frame requests as specific solutions, but the development team has a responsibility to propose the most appropriate features to achieve those underlying goals.

## In the Book

Smart introduces Feature Injection in chapter 3 as the antidote to building features nobody wants. He describes the classic "why" iteration: when a media director requests "people posting printed classified ads online," the team asks "why?" repeatedly. Each answer reveals a deeper truth: "Because people don't read classifieds anymore" → "Because revenue is falling" → "Because more people will browse online" → until the real goal emerges: increase classified ads revenue by getting faster product sales and higher commission volume. Smart frames this as "popping the why stack," using "five why-style questions" (3671-3672) to identify underlying business value. Feature Injection also incorporates "spot the examples" (207-208) where testers and analysts use concrete scenarios to explore corner cases, and "inject the features" step where the team proposes multiple ways to deliver the discovered business goal rather than implementing the original request mechanically.

## Why It Matters

Feature Injection reorients teams away from the "wish-list execution" model where every requested feature gets built regardless of whether it solves the actual problem. By forcing a conversation about business value before design starts, teams discover that many features are solutions to the wrong problem or not solutions at all. This conversation also puts the team in position to propose better, faster, cheaper alternatives—technical approaches the stakeholder never imagined. More importantly, when changes inevitably occur (because requirements shift during any project), teams that understand the underlying business goal can reassess whether a feature remains relevant, rather than treating requirements as fixed documents that must be honored regardless of changed circumstances.
