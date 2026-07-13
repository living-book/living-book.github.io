---
type: Concept
title: Batch Size Economics
description: Batch size is a controllable economic variable, traded off against transaction cost, whose reduction cuts cycle time, variability, risk, and overhead together.
book: product-development-flow
chapters: [5]
tags: [batch-size, economics, transaction-costs, variability]
created: 2026-07-12
---

# Batch Size Economics

## Definition

Batch size — how much work accumulates before it moves to the next step — is an
economic dial most product developers never notice they're turning, let alone
optimizing. Reinertsen shows that smaller batches shrink queues (and thus cycle time),
reduce flow variability, accelerate feedback, lower risk, and often *reduce* overhead
rather than raising it — reversing the intuition that big batches are more efficient. The
optimum batch size is set where transaction cost (the fixed cost of moving or reviewing a
batch) and holding cost (the cost of the queue that accumulates while waiting to batch)
balance against each other — and that optimum shifts whenever transaction cost changes.

## In the Book

Chapter 5 builds its case through ten stacked principles. B1 uses a cumulative-flow-diagram
argument: since queue size is proportional to batch size and Little's Law ties queue size to
cycle time, shrinking batches shrinks cycle time without touching capacity or demand. B2
uses a restaurant seating a steady trickle of diners versus a single 80-person tour bus — "an
elephant traveling through a boa constrictor" — to show large batches create the load
spikes that overwhelm a process even when average demand is unchanged. B5 and B6
attack the common assumption directly: batching 300 open software bugs instead of 30
means every new bug must be checked against 300 duplicates instead of 30, and status
reporting scales with both batch size and the resulting longer cycle time — so large batches
raise overhead, they don't reduce it. The chapter's economic engine is the trade-off between
transaction cost and holding cost (echoing the classical Economic Order Quantity model),
and Reinertsen's key twist is Principle B12: transaction cost is not fixed — Toyota's SMED
program cut die-changeover time from 24 hours to minutes, proving that investing in
lowering transaction cost pays for itself by unlocking a much smaller optimal batch size.

## Why It Matters

"Reduce batch size" reframes a long list of seemingly unrelated agile and lean practices —
continuous integration, small pull requests, iterative releases, rapid prototyping — as
instances of one underlying economic mechanism rather than separate best practices to
imitate. It also supplies the lever for improving all of it at once: instead of treating batch
size as fixed and accepting its overhead, invest in cutting the fixed cost of each transition
(automation, tooling, checklists), which lets you shrink batches further and compounds the
gain. The same logic explains why network protocols split large files into small packets
and why staggering arrivals (like lunch hours) can eliminate a queue more cheaply than
adding capacity.
