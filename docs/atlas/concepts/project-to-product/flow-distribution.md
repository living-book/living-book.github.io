---
type: Concept
title: Flow Distribution
description: The deliberately tuned ratio of work-item types a value stream commits to, set by business need rather than left as an unconscious byproduct of daily prioritization.
book: project-to-product
chapters: [4, 6]
tags: [prioritization, resource-allocation, tradeoffs, strategy, metrics]
created: 2026-07-12
---

# Flow Distribution

## Definition

Flow Distribution is "the proportion of each flow item within a value stream,
adjusted depending on the needs of each stream to maximize business value." Because
the four flow items (features, defects, risks, debts) are mutually exclusive and
collectively exhaustive, their distribution is a forced trade-off: increasing one
share necessarily decreases the others. Rather than letting this ratio emerge as an
accident of whoever shouts loudest in planning, the Flow Framework treats it as a
dial that leadership and teams set on purpose, and re-set as the product's maturity,
market position, or life-cycle stage changes.

## In the Book

Kersten contrasts a new product's value stream — which should skew heavily toward
Feature flow to hit launch, since there are few customers to generate defects and low
public exposure to create risk work — against a legacy back-end service kept alive
only to support other systems, whose flow distribution should shift almost entirely
to defect fixes and risk reduction with minimal feature investment. He ties the dial
explicitly to Geoffrey Moore's Zone Management (Incubation, Transformation,
Performance, Productivity zones): each zone implies a different target distribution,
and making that target explicit lets managers and teams share an understanding of
what a given value stream is currently optimized for. The clearest illustration is
Bill Gates's 2002 Trustworthy Computing memo at Microsoft, which the book reads as a
company-wide flow-distribution reset toward risk and security work, later followed by
a deliberate pivot back toward feature flow to fight the web-platform disruption
threat. Chapter 6 uses the concept diagnostically again: the industry-wide rise in
software-related automotive recalls is evidence that flow distribution across the
automotive sector has drifted too far toward features relative to defects and risk,
and needs to be consciously rebalanced.

## Why It Matters

Flow Distribution names a decision that most organizations make unconsciously and
retroactively — discovering their real priorities only by looking backward at what
got shipped — and turns it into a forward-looking, adjustable setting tied explicitly
to a system's current life-cycle stage. Any system with a fixed capacity and multiple
categories of competing, non-fungible demand (a factory splitting output between new
product lines and existing-customer support, a research group splitting time between
new results and replication, a government agency splitting budget between new
programs and enforcement) faces the identical tuning problem: the ratio should track
the system's current strategic posture, not calcify around whatever it happened to be
last quarter.
