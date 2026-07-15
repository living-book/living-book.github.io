---
type: Concept
title: "Hybrid Process Framework"
description: "Pragmatically combine practices from Scrum, XP, Agile Modeling, Unified Process, Agile Data, and Kanban rather than rigidly adhering to a single methodology."
book: disciplined-agile-delivery
chapters: [1, 3]
tags: [methodology, hybrid, pragmatism, tailoring, practices]
created: 2026-07-15
---

# Hybrid Process Framework

## Definition

DAD is explicitly a hybrid process framework that borrows from multiple sources rather than insisting on doctrinal purity. It adopts Scrum's iterative project management structure, XP's technical practices (continuous integration, test-driven development, refactoring), Agile Modeling's modeling and documentation strategies, Unified Process's governance and phase structure, Agile Data's data-focused practices, and Kanban's flow-based approaches. Rather than debating which framework is "right," DAD acknowledges that each offers useful ideas and that real projects benefit from intelligent combination.

## In the Book

Chapter 1 frames DAD as "the happy medium between Scrum (lightweight, construction-focused) and RUP (comprehensive but heavyweight)." Chapter 3 details the foundations and sources explicitly. The book describes each source discipline:

- **Scrum** (project management): Working from a prioritized backlog, time-boxed iterations, product owner, daily standups, sprint reviews and retrospectives.
- **Extreme Programming (XP)** (technical practices): Continuous integration, refactoring, test-driven development (TDD), pair programming, collective code ownership.
- **Agile Modeling (AM)** (modeling and documentation): Lightweight, just-in-time modeling; requirements envisioning; architecture envisioning; continuous documentation; model storming.
- **Unified Process (UP)** (governance and phases): Phase-based structure (Inception, Elaboration/Construction, Transition); explicit milestones; risk-driven approach; architecture-centric design.
- **Agile Data (AD)** (data practices): Agile approaches to database schema evolution, data migration, and data governance.
- **Kanban** (flow): Continuous flow without time-boxes; WIP limits; pull-based work management; metrics-driven improvement.

The book observes that many organizations independently discover the same hybrid: they adopt Scrum as a foundation, then find they need better technical practices (so they add XP), better governance (so they add UP elements), and better data strategies (so they add AD ideas). Why not start with a framework that already combines these? This is DAD's pragmatic value proposition.

The book emphasizes that hybrid does not mean "take a little bit of everything and hope for the best." It means thoughtfully combining practices where they complement each other. For example, Scrum's iteration boundary and XP's continuous integration work together: iterations create natural release points, and CI ensures code is always in a releasable state within those boundaries. Similarly, UP's phase structure and risk-driven milestones add explicit gates to Scrum's sprint rhythm, surfacing project viability without the bureaucracy of traditional phase gates.

## Why It Matters

Hybrid process frameworks are pragmatic responses to organizational reality. No single methodology perfectly fits all contexts. By acknowledging multiple sources of wisdom and combining them intelligently, DAD avoids both rigid fundamentalism ("we only do Scrum, exactly as described") and chaotic eclecticism ("we do whatever feels right this week"). It also legitimizes the observation that many organizations have already discovered these combinations empirically, suggesting that DAD's synthesis is based on real-world experience, not theory. For practitioners, this is liberating: it removes the pressure to choose a "true" methodology and instead focuses energy on tailoring a coherent combination of practices to the situation at hand. For enterprises, it provides a named, documented path for scaling agile beyond small-team Scrum without abandoning agile values.

