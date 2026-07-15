---
type: Concept
title: Shippable Quality Standards
description: "A framework using severity and impact dimensions to prioritize production bugs into fix-immediately, negotiate-release, or backlog categories based on customer risk."
book: collaboration-at-scale
chapters: [1]
tags: [quality, bugs, prioritization, decision-framework, production]
created: 2026-07-15
---

# Shippable Quality Standards

## Definition

Shippable Quality Standards use a two-dimensional severity/impact matrix to classify defects and decide whether they must be fixed before release, can be negotiated, or belong in the backlog. Severity measures the effect on the customer (data loss, crash, error), while impact measures how many customers are affected. The intersection determines priority action.

## In the Book

The book shows that preventing production bugs requires building quality criteria into Definition of Done rather than trying to sort them later. It provides a concrete severity/impact matrix where severity ranges from "Data Loss" (extreme) to "Feature Request" (not a bug), and impact ranges from "80%+ of customers" (I4) to "1-10% in special conditions" (I1).

The combined matrix categorizes responses: Data Loss/Many Customers = "Fix Immediately"; Crash-No-Workaround/Most Customers = "Fix in Sprint"; Crash-with-Workaround/Some Customers = "Negotiate Release"; lower severity/impact combinations = "Add to Backlog (Maybe)" or "Delete." The book emphasizes that this framework prevents the ad-hoc prioritization debates that consume time and that quality standards should be part of Definition of Done to stop bugs from reaching production in the first place.

## Why It Matters

Without explicit standards, organizations waste cycles debating whether each bug must be fixed now. A severity/impact matrix makes the decision rule explicit, transparent, and repeatable across teams. It also prevents two pathologies: over-fixing low-impact issues and under-prioritizing high-impact ones. By embedding quality standards in Definition of Done, teams catch problems earlier rather than waiting for production failures.
