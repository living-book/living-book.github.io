---
type: Concept
title: Lead Time and MTTR as Core Quality Metrics
description: Two complementary metrics measuring how fast new features and production fixes reach customers; together they reveal code maintainability and system stability.
book: agile-metrics-in-action
chapters: [8]
tags: [measurement, quality, speed, production, delivery]
created: 2026-07-12
---

# Lead Time and MTTR as Core Quality Metrics

## Definition

**Lead time** measures the elapsed time from when a feature is defined to when it reaches the customer — the full cycle through development, testing, build, and deployment. **Mean Time To Repair (MTTR)** measures the elapsed time from when a production problem is detected to when a fix is deployed — triage, code change, testing, and deployment combined.

Together, these metrics reveal whether code is maintainable (short times mean easy to change and deploy) and whether the system is stable (low MTTR means quick response to problems). Unlike proxy metrics like velocity or code coverage, lead time and MTTR measure actual customer impact — how fast value flows to production.

## In the Book

Chapter 8 breaks down both metrics as they move through the delivery pipeline. Lead time spans from project tracking (when a task is defined) through source control, CI/build, deployment tools, and ends when the feature is live. MTTR spans from application monitoring (when an anomaly is detected) through the same pipeline and ends when the fix is deployed. The formula for each is simple:

- Lead Time = Task Complete Date − Task Start Date
- MTTR = Anomaly End Time − Anomaly Start Time

But the formulas are just starting points. The chapter shows how to break down a 35-hour average MTTR into its components (triage, development, build, test, deploy) to find where to focus. In one example, testing consumed most of the time — adding automation would reduce MTTR more than optimizing triage.

The book also introduces the **Maintainable Release Rating (MRR)**, which combines MTTR with fix frequency: MRR = MTTR (in minutes) × (Total Fixes / Total Releases). A team with 60 releases and 10 fixes, each taking 4 hours to fix, has an MRR of 40. A team with the same 4-hour MTTR but a hotfix in every release has an MRR of 240 — the second team's code is less maintainable.

## Why It Matters

Velocity tells you how much work the team says it's doing; lead time tells you how fast actual value reaches customers. Code coverage tells you what percentage of code has tests; MTTR tells you whether the system is stable when problems do occur. Short lead times and MTTR reveal a codebase that's easy to understand and change — qualities that enable continuous delivery and reduce risk. When these metrics are long or increasing, it's a signal that technical debt is accumulating or the system is becoming harder to reason about, even if the team feels busy.
