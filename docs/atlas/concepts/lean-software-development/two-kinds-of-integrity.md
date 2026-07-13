---
type: Concept
title: Perceived Integrity and Conceptual Integrity
description: A system needs two distinct kinds of coherence — matching what the customer actually values, and holding together internally as an architecture — and each fails differently.
book: lean-software-development
chapters: [6]
tags: [architecture, coherence, customer-value, communication, design]
created: 2026-07-12
---

# Perceived Integrity and Conceptual Integrity

## Definition

Perceived integrity means the system, as experienced, actually delivers what the customer values — the balance of function, usability, reliability, and economy matches customer expectations. Conceptual integrity means the system's internal architecture is a smooth, cohesive whole where components fit together and the design achieves a working balance of flexibility, maintainability, efficiency, and responsiveness. The two are separate failure modes: a system can be internally elegant but solve the wrong problem, or genuinely useful to customers while being an unmaintainable architectural tangle.

## In the Book

For perceived integrity, the book's model is the Japanese automotive chief engineer, who personally carries a vision of what the target customer wants and continuously refreshes it in the engineers making detailed tradeoffs — a role the authors argue sequential software development structurally lacks, because requirements pass through analysis, design, and coding as successive handoffs, each losing information, with the programmers making day-to-day tradeoffs two or three documents removed from the customer. Their fix is establishing direct customer-developer information flow: small co-located teams with short iterations, customer tests, shared models the customer and programmer both use without translation, or a master developer playing the chief-engineer role on larger systems. The chapter's sidebar example is a matrix model — one spreadsheet crossing 25 entities against roughly 150 transactions — that became the single requirements artifact a customer and developers pored over together and kept updated, illustrating the book's broader endorsement of Eric Evans's domain-driven "ubiquitous language." Conceptual integrity is framed as the architectural counterpart, achieved the way a complex machine's design is unified rather than accreted feature by feature — the book explicitly treats the two integrities as parallel disciplines with different failure surfaces and different remedies.

## Why It Matters

It's common to conflate "good software" into one undifferentiated quality judgment, which makes it hard to diagnose why a technically admired system disappoints users, or why a beloved product becomes unmaintainable. Splitting integrity into two kinds gives you separate diagnostic questions — does this match what the customer values, and does this hang together as a coherent whole — and each points to a different intervention: closer customer-developer information flow for one, disciplined architectural ownership for the other.
