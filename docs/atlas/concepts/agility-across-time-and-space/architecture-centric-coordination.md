---
type: Concept
title: "Architecture-Centric Coordination"
description: "A strategy for reducing inter-team dependencies in distributed projects by designing software architecture first, then aligning team boundaries and task division to that architecture, enabling independent parallel work."
book: agility-across-time-and-space
chapters: [15, 22]
tags: [architecture, team-structure, coordination, distributed-teams, dependency-management]
created: 2026-07-15
---

# Architecture-Centric Coordination

## Definition

Architecture-Centric Coordination inverts the typical bottom-up flow of distributed development. Rather than teams at different sites working on assigned features and discovering integration challenges later, this approach first defines the software architecture, then organizes team boundaries and task assignments to respect architectural boundaries. By doing so, teams can work on separate architectural components in parallel with minimal real-time coordination across locations. The architecture itself becomes the "coordination mechanism," reducing the need for synchronous communication between geographically separated teams and enabling asynchronous handoffs along well-defined interfaces.

## In the Book

Bosch and Bosch-Sijtsema studied three large-scale distributed companies and found that top-down process-centric coordination approaches (where management tries to choreograph dependencies) led to "interaction problems" and bottlenecks. Instead, successful large distributed projects explicitly designed their software architecture first, then mapped teams to architectural components. One example involved "Roadmapping" (architecture-level planning), followed by "Requirements" (at component level), then "Architecture" (internal design), "Development" (teams working independently), "Integration or Composition" (at component seams). In architecture-centric organizations, a "Technical Service Team" ensured conceptual integrity (that components fit together), but development teams could work largely independently. This reduced the number of synchronous decisions teams needed to make across time zones. Chapters 15 and 22 emphasize that "architecture-centric software engineering" becomes not just a quality practice but a coordination mechanism necessary for global agile projects.

## Why It Matters

This concept reveals that distributed agile development requires a shift from people-centric coordination (constant meetings, alignment discussions) to structure-centric coordination (well-defined boundaries that reduce the need for alignment). It addresses a deep tension in distributed agile: agile manifesto values direct communication and responsiveness, but geographic distribution makes synchronous communication costly. Architecture-centric coordination accepts this reality and bakes the coordination need into the design itself, rather than trying to overcome it with more meetings. The insight applies beyond software: any distributed knowledge work (product design, legal discovery, research collaboration) can benefit from front-loading structural decisions that reduce later coordination burden.
