---
type: Concept
title: The Four Flow Items
description: A MECE taxonomy of everything that competes for capacity in a value stream — features, defects, risks, and debts — each pulled by a different stakeholder.
book: project-to-product
chapters: [3]
tags: [taxonomy, prioritization, measurement, tradeoffs, work-classification]
created: 2026-07-12
---

# The Four Flow Items

## Definition

Kersten defines a **Flow Item** as "a unit of business value pulled by a stakeholder
through a product's value stream," then derives exactly four categories that are
mutually exclusive and collectively exhaustive (MECE): **Features** (new value,
pulled by customers), **Defects** (quality fixes, pulled by customers), **Risks**
(security/governance/compliance work, pulled by risk officers), and **Debts**
(architectural and infrastructure improvement, pulled by architects). Because the
categories are MECE, all work in a software value stream falls into exactly one of
them — which means prioritizing between them is a genuine zero-sum allocation, not an
open-ended wish list.

## In the Book

The chapter builds the taxonomy from first principles rather than borrowing it: Lean
thinking starts with what the customer pulls, so features and defect fixes are the
obvious first two items (the customer exchanges money or attention for them). The
other two — risk and debt — come from Kersten's "Mining the Ground Truth of
Enterprise Toolchains" study of 308 enterprise IT tool networks, which surfaced two
further kinds of work that are invisible to the customer but are pulled internally: by
Chief Risk Officers (regulatory, security, compliance) and by architects (technical
debt reduction). Table 3.1 tabulates each item's example artifacts (epic/user
story, bug/incident, vulnerability/regulatory requirement, API addition/refactoring).
The book insists debt work should only ever be prioritized when it increases future
flow through the value stream — not "for the sake of architecture alone" — meaning
flow of the four items should shape the architecture, not the reverse. It also uses
the taxonomy diagnostically in the automotive-software recall crisis (Chapter 6):
rising software-related car recalls are read as evidence that carmakers have let
Feature flow crowd out Defect and Risk flow, a trade-off the framework makes visible
and nameable rather than implicit.

## Why It Matters

Most organizations argue about priority using an unbounded, incommensurable list of
work types. Collapsing all software work into four exhaustive, non-overlapping
buckets turns "what should we work on" into an explicit allocation problem across a
fixed set of categories — and exposes invisible categories (risk, debt) that customer-
facing prioritization habitually starves. The pattern generalizes to any system where
some claimants on capacity are visible and vocal (customers) while others are silent
until they cause a crisis (regulators, future maintainers) — a structure recognizable
in engineering, public policy, and personal time management alike.
