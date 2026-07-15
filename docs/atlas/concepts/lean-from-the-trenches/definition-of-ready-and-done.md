---
type: Concept
title: "Definition of Ready and Done"
description: Explicit state gates at column boundaries that clarify when work moves forward, enabling cross-functional collaboration and breaking down specialty silos.
book: lean-from-the-trenches
chapters: [7]
tags: [kanban, workflow, collaboration, clarity]
created: 2026-07-15
---

# Definition of Ready and Done

## Definition

Each column on a Kanban board has explicit criteria for what "ready" and "done" mean at that stage. For example: a feature is "ready for development" only after requirements are estimated, acceptance tests are agreed upon, and all specialties have signed off; a feature is "ready for system test" only after developers have tested it locally, merged it to trunk, and demonstrated it to the team. These gates shift work from happening in isolation to requiring continuous cross-functional conversation.

## In the Book

The PUST police project had a critical breakthrough when they defined these gates explicitly on the project board. Previously, requirements analysts considered their work "done" when a document was written and signed off, developers when code was checked in, and testers when features passed system test—no handoffs between teams, lots of confusion. After defining "Ready for Development" (estimated, broken down, acceptance tests agreed), the team discovered that analysts couldn't move a feature forward without developers and testers having a conversation. At the same time, "Ready for System Test" required that embedded testers work with feature teams during development, not after. This simple visibility exposed the siloed specialization that was killing collaboration and forced people to actually work together to move a card from one state to the next.

## Why It Matters

Definition of ready and done transforms a Kanban board from a progress tracker into a collaboration forcing function. It makes handoff points visible and explicit, so people can't hide behind documents or sequential phases. In large multiteam projects where a single person's "done" is someone else's starting point, this clarity eliminates confusion about what really needs to happen next—and makes it impossible to complete your work without first understanding what the next person actually needs. This is the opposite of "throw it over the wall."
