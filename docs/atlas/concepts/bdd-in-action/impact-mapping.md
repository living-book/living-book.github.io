---
type: Concept
title: Impact Mapping
description: "A visual mind-map connecting business goals to actors, impacts they need, and features that deliver those impacts."
book: bdd-in-action
chapters: [3]
tags: [requirements, visualization, business-alignment, stakeholder-analysis]
created: 2026-07-15
---

# Impact Mapping

## Definition

Impact Mapping is a visual technique for aligning software features with business goals by mapping relationships across four levels: why (business goal), who (actors affected), how (impacts or capabilities needed), and what (features). Created as a mind-map during collaborative conversations, an impact map makes visible the assumptions connecting goals to features, validates that proposed features will actually achieve the goal, and helps teams cut low-impact work when trade-offs are needed.

## In the Book

Smart introduces Impact Mapping in chapter 3 as a practical tool within the Feature Injection process. He explains that "Impact Mapping is a way of visualizing the relationship between the business goals behind a project, the actors that will be affected by the project, and the features that will enable the project to deliver the expected results. Impact maps are simple to create and easy to understand, and they can be a very useful tool for documenting business goals and validating assumptions" (3734-3738). He describes the four types of questions that structure an impact map: "Why? Who? How? What?" (3745-3748). The technique begins with the business goal at the center, branches to identify the actors who influence or enable the goal, then maps what each actor needs to do differently (the "how" or capability), and finally identifies which features would enable that behavior change. Smart notes that "An impact map is a mind-map built during a conversation, or series of conversations, between stakeholders and members of the development team" (3743-3744), emphasizing that the mapping process itself—the discussion and validation—is as valuable as the resulting diagram.

## Why It Matters

Impact Mapping makes the assumptions connecting goals to features explicit and testable, moving from "build this feature" to "build this feature because it will cause this actor to do this thing which enables our goal." This clarity reveals when features are disconnected from goals, when multiple features target the same actor, or when features assume behavior changes that won't happen without additional enablement (training, incentives, etc.). For teams facing scope trade-offs, an impact map immediately shows which features have low impact on the goal and can be deferred. The visual format also makes it easier for non-technical stakeholders to participate in requirements conversation and to spot gaps or contradictions in strategy.
