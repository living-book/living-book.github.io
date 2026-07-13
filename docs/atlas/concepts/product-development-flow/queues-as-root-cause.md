---
type: Concept
title: Queues as the Root Cause
description: Product development's waste, risk, and quality problems trace back to invisible queues of waiting work, not to slow activities.
book: product-development-flow
chapters: [3]
tags: [queueing-theory, waste, invisibility, systems-thinking]
created: 2026-07-12
---

# Queues as the Root Cause

## Definition

Queues — work waiting for a busy resource — are, in Reinertsen's framing, the primary
source of economic waste in product development, more damaging than in manufacturing
because they are both physically and financially invisible. Unlike a factory's work-in-process
inventory, which a CFO can read off the balance sheet, "design-in-process" inventory shows
up nowhere in the accounts, so it accumulates unmanaged, unmeasured, and often
unnoticed.

## In the Book

Chapter 3 borrows vocabulary from queueing theory (Erlang's 1909 work on telephone
networks; the M/M/1/∞ queue) to argue that product development's real problem is
periods of inactivity, not slow activity. Principle Q1, "The Principle of Invisible Inventory,"
uses an anecdote from a Hewlett-Packard engineering manager — "our inventory is bits on
a disk drive, and we have very big disk drives" — to show why queues escape scrutiny:
they leave no physical trace the way a factory floor's stacked inventory does. Principle Q2
traces six distinct kinds of damage that queues cause: they increase cycle time (a
quantifiable cost-of-delay effect), raise risk by lengthening exposure to shifting
requirements and competitor moves, amplify variability at high utilization, raise reporting
overhead (the book contrasts a 16-week-lead-time factory needing 60 status transactions
against a lean factory needing two), and — most importantly for quality — delay the
feedback that catches bad assumptions before they compound.

## Why It Matters

Most organizational diagnosis stops at symptoms (missed deadlines, low quality, high
overhead) and proposes symptom-level fixes (more status meetings, more testing, more
resources). Naming queues as the shared root cause redirects attention to the one lever
that, if pulled, improves cycle time, risk, cost, and quality simultaneously — and it explains
why adding resources to a bottleneck without shrinking the queue in front of it often fails
to help. It also generalizes past software and hardware development to any system where
"inventory" is information rather than physical stock, and therefore easy to accumulate
without anyone noticing.
