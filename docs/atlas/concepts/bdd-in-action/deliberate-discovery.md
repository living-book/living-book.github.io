---
type: Concept
title: Deliberate Discovery
description: "Proactively uncovering unknowns through concrete examples and conversations rather than planning around them or discovering them in production."
book: bdd-in-action
chapters: [4]
tags: [uncertainty, learning, requirements, risk-reduction]
created: 2026-07-15
---

# Deliberate Discovery

## Definition

Deliberate Discovery is the practice of actively seeking out and surfacing the unknowns, edge cases, and false assumptions in a project through examples and collaboration, rather than hoping they'll reveal themselves through execution or discovering them after delivery. It treats ignorance and uncertainty not as obstacles to plan around but as opportunities to learn cheaply and early by asking specific questions and exploring concrete scenarios with stakeholders.

## In the Book

Smart introduces Deliberate Discovery in chapter 4 as a companion to Real Options thinking. The opening sonnet by Liz Keogh frames the concept: "We didn't know we didn't know before" and "Discover tiny dragons, be they few, / And all the mightiest, with equal praise" (70, 108). Smart explains that "When a user proposes an example of how a feature should behave, project team members often ask for extra examples to illustrate corner cases, explore edge cases, or clarify assumptions. Testers are particularly good at this, which is why it's so valuable for them to be involved at this stage of the project" (1509-1513). He frames examples as discovery tools: "Examples are a great way to explore and expand your knowledge" (1509). The technique is deliberate because it's not accidental—teams actively work through scenarios, asking "what if?" and "what happens when?" to surface boundary conditions, impossible states, and contradictory requirements while they're still cheap to fix, before implementation locks them in.

## Why It Matters

Deliberate Discovery reduces risk by converting hidden assumptions into visible ones that can be validated or corrected. When a tester asks "what if the transfer amount exceeds the balance?" in a requirements conversation, the team discovers a missing business rule while code hasn't been written yet. This is vastly cheaper than discovering the same issue in production or in a failed test after implementation is complete. Because discovery happens through concrete examples, the knowledge gained is not abstract (and forgettable) but specific and grounded in scenarios the team can return to. The practice also builds shared understanding—when the team collectively works through examples, they reach consensus on edge cases and document that consensus in the executable specifications that follow.
