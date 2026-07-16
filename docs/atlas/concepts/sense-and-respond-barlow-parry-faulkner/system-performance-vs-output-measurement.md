---
type: Concept
title: "System Performance vs. Output Measurement"
description: "End-to-end capability measurements predict system behavior better than output metrics; measuring averages masks variation and causes mismanagement of performance."
book: sense-and-respond-barlow-parry-faulkner
chapters: [4]
tags: [measurement, capability, variation, systems-thinking]
created: 2026-07-15
---

# System Performance vs. Output Measurement

## Definition

System performance measurement captures how long it takes for a complete customer request to move through the entire organization end-to-end, while accounting for variation around that time. This differs fundamentally from output measurement (e.g., "calls answered per hour"), which counts work units completed but reveals nothing about predictability or where bottlenecks exist. End-to-end measurements predict future performance; output metrics only indicate that a problem exists without specifying how to fix it.

## In the Book

The book introduces control-chart techniques from Walter Shewhart and David Edwards Deming to distinguish common-cause variation (built into system design) from special-cause variation (random external events). Output metrics hide this distinction. For example, measuring an average on-time delivery rate of 68% masks the fact that the system delivers between 57% and 80%—a range so wide that staff trying to improve the average will simply "try harder" without understanding systemic constraints.

The authors emphasize that if an organization measures only averages, "don't be surprised to find yourself running an average business." They illustrate with a travel-time example: declaring comfort because on average one foot is in lava and one is in liquid nitrogen is absurd. Similarly, measuring a call center by average handle time or conversion rate disguises the fact that some requests take ten minutes while others take ten days for the same work—not due to staff performance but due to system design (batch-and-queue, handoffs, approvals).

The book advocates for capability-of-means measurements: understanding what the system is capable of delivering under current design, then identifying which common causes of variation constrain performance. When system changes are made, the same end-to-end measurement can be used to measure their effectiveness. This approach reveals that many "performance problems" are actually design problems.

## Why It Matters

System performance measurement creates accountability for system design rather than individual performance. It prevents organizations from setting impossible targets based on a handful of exceptional results. It reveals where to invest improvement efforts (the common causes that constrain the range) rather than where to blame people. Organizations that shift to capability measurements find they can reliably predict performance and explain it to customers, moving from reactive firefighting to proactive capacity planning. This framework is essential for sense-and-respond operations because it enables organizations to identify when system changes are needed to handle new customer demands.
