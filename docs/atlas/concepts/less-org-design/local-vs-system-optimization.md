---
type: Concept
title: Local Optimization vs. System Optimization
description: Organizations structured around specialties each optimize their own efficiency, creating delays and waste elsewhere; true optimization requires viewing the whole system.
book: less-org-design
chapters: []
tags: [systems-thinking, efficiency, coordination, trade-offs]
created: 2026-07-12
---

# Local Optimization vs. System Optimization

## Definition

Local optimization occurs when each group or step in a process is run to maximize its own efficiency—analysts write perfect specs before handing to developers, developers maximize lines of code per person, testers catch defects late. The aggregate result is slow system throughput and low customer delight. System optimization subordinates local efficiency to overall customer value and cycle time.

## In the Book

Larman dramatizes the problem with the "watch the ball, not the players" exercise: "everyone is busy and doing their best on their task, yet the system is delivering slow and not delighting the user." He traces this through multiple structures: intermediate analysts optimize their spec clarity (local); architects optimize design purity (local); component teams optimize component efficiency (local). Each handoff between specialists adds delay, rework, and knowledge loss. The classic example is the "Contract Game"—a planning phase that optimizes forecast accuracy before development starts, creating massive front-loaded analysis and a long queue of "requirements ready to code" that create waiting and inventory. The antidote is removing local optimizations through feature teams (no analyst → developer handoff), co-location, and continuous learning. Larman explicitly asks: "what's the One True system optimizing goal?"—and answers: delivering maximum customer value per unit time (concept-to-cash cycle time, customer delight).

## Why It Matters

This concept reframes efficiency entirely. A step that looks "productive" (everyone busy, high utilization) can be a major bottleneck if it creates queues for downstream steps. Understanding system optimization explains why flat utilization and slack capacity matter, why feature teams beat specialist silos, and why "be more efficient" as an instruction often makes the system worse. It is foundational to lean thinking and flow.
