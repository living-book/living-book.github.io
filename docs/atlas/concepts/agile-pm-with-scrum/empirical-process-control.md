---
type: Concept
title: Empirical Process Control
description: "Managing complex work by making process aspects visible, inspecting frequently, and adapting quickly when outcomes diverge from acceptable ranges."
book: agile-pm-with-scrum
chapters: [1]
tags: [complexity, feedback, control, inspection]
created: 2026-07-15
---

# Empirical Process Control

## Definition

Empirical process control is a method for managing work where the underlying mechanisms are too complex to predict in advance. Instead of defining a process in detail upfront and executing it as planned (defined process control), empirical control relies on three interconnected mechanisms: making work and outcomes visible, inspecting them frequently, and adapting the process or materials quickly when they diverge from acceptable ranges.

## In the Book

Schwaber grounds Scrum in industrial process control theory, contrasting empirical control with defined control. In defined control, you can plan a process precisely because the underlying mechanisms are well-understood (like manufacturing a standard part). Software development is fundamentally different: requirements are ambiguous and changing, technologies are unreliable, and people's capabilities vary. Schwaber argues that these three dimensions of complexity—requirements, technology, and people—make it impossible to plan software development as a defined process.

The three legs of empirical process control are visibility, inspection, and adaptation. Visibility means those aspects affecting the outcome must be visible to those controlling the process—and what is visible must be true. Schwaber illustrates this with code reviews: if a team labels code "done" but means different things by that word (some assume it includes unit testing, others don't), visibility breaks down. Inspection must occur frequently enough to detect unacceptable variance before large investments go wrong, but not so frequently that the inspection itself becomes burdensome. Adaptation means the inspector must adjust either the process or the work itself as quickly as possible to minimize drift.

Scrum implements this through sprint cycles (30-day iterations with daily standups for inspection), sprint reviews (showing stakeholders completed work), and retrospectives (adapting the team's process). The Product Backlog and burndown chart provide visibility. These mechanisms create a feedback loop that prevents the kind of large-scale project failure common in traditional, plan-driven approaches.

## Why It Matters

This concept reframes how we think about managing complex work. It moves away from the idea that better planning prevents problems, toward the idea that frequent inspection and fast adaptation do. In domains where outcomes are inherently unpredictable—product development, research, organizational change—empirical control explains why short cycles, visible progress, and collaborative adjustment outperform elaborate upfront plans. The principle applies beyond software: product design, strategy execution, and any work involving discovery over execution benefits from visibility-inspection-adaptation loops.
