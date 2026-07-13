---
type: Concept
title: Zombie Projects
description: Low-value, barely-alive initiatives that never get killed keep silently siphoning time and attention away from higher-value work, protected by sunk-cost thinking.
book: making-work-visible
chapters: [1.5]
tags: [technical-debt, sunk-cost-fallacy, prioritization, resource-allocation, maintenance]
created: 2026-07-12
---

# Zombie Projects

## Definition

A zombie project (DeGrandis credits the term to Donald Reinertsen) is an initiative that is technically still funded and staffed but delivers little value — "barely alive," "starving for money, resources, and people" — yet persists because no one formally kills it. Distinct from ordinary neglected maintenance, the zombie-project pattern is specifically about work that survives past the point its economics justify, protected by sunk-cost fallacy: the more already invested, the harder it becomes to walk away, even when only the incremental cost-to-finish versus incremental value should matter.

## In the Book

Section 1.5 (Neglected Work) is grounded in DeGrandis's own experience at Corbis maintaining JD Edwards (JDE), a ten-year-old, unsupported, heavily customized ERP system. Upgrades broke customized tables, so the team froze it in place; deployments routinely overwrote configuration files and silently disappeared new orders; eventually "everyone became afraid to touch the JDE server," and it sat neglected for a decade until replaced by SAP. She generalizes this into a claim that maintenance of legacy systems is one of the most neglected categories of work precisely because "busy" people chasing new features get credited, while quiet decay doesn't show up until it becomes an emergency.

She then names the sunk cost fallacy explicitly and cites Reinertsen's *The Principles of Product Development Flow*: the only economically sound question is the incremental investment to finish versus the incremental return, not what's already been spent. Her prescription is blunt — "when you discover a zombie project, kill it," on the logic that if it's truly needed it "can return from the dead," but until then it should stop siphoning capacity from higher-value work in progress.

## Why It Matters

This names a failure mode that's easy to rationalize one project at a time but obvious in aggregate: portfolios accumulate zombies because killing something already invested-in feels like admitting loss, while letting it limp along feels neutral — it isn't. The concept gives permission (and a decision rule: incremental cost vs. incremental value, not sunk cost) to prune a portfolio actively rather than merely triaging what's newest or loudest.
