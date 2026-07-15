---
type: Concept
title: Role-Based Metrics Hierarchy
description: "Different organizational roles need different data granularity and time horizons: teams track daily tactical metrics, managers track weekly trends, executives track strategic outcomes."
book: agile-metrics-in-action
chapters: [9]
tags: [measurement, communication, reporting, leadership, metrics]
created: 2026-07-12
---

# Role-Based Metrics Hierarchy

## Definition

A single metrics dashboard cannot serve a developer, a manager, and an executive at the same time. Developers need to know "are we moving good code through the pipeline right now?" (pull request age, build ratio, task recidivism), visible hourly or daily. Managers need to know "is this team improving and consistent?" (trend in lead time, velocity, estimate accuracy), visible weekly or monthly. Executives need to know "is this business succeeding?" (revenue, customer engagement, release frequency), visible monthly or quarterly. Each layer answers a different question and requires different data aggregation.

## In the Book

Chapter 9 maps out this hierarchy with concrete dashboard examples. At the team level (Blastamo's development team), the metrics focus on immediate workflow health: pull request comment count, PR hours open, commits per PR, lead time, and development time. These are tracked daily because the team can respond immediately — if PR comments spike, they know code is controversial and should discuss design before reviewing.

At the manager level (program management in the case study), the metrics roll up to cross-team comparison: lead time trends, velocity/volume, estimate health, and committer distribution. These are tracked weekly or biweekly because managers use them to spot teams falling behind or stuck on certain work types, to redistribute resources, or to share what one team is doing well with another.

At the executive level (leadership team), the metrics are entirely business-focused: monthly revenue, customer engagement (tweets, app store ratings), and release frequency. The executives don't care how many pull requests were open or whether the code had good comments — they care whether the investment is paying off.

The book's Blastamo case study shows all three layers working together: development team watches their dashboards to fix things immediately, program management uses aggregated team metrics to spot patterns and make coaching decisions, and leadership uses simplified business metrics to decide if the strategy is working.

## Why It Matters

Showing a team an executive dashboard (which just has revenue) doesn't help them improve their code or process. Showing an executive a developer dashboard (which has build timing and PR comments) is noise — they can't act on it. Role-based metrics ensure that each person in the organization gets the information they actually use. It also prevents micromanagement: if managers can see that lead time is trending down and bugs are dropping, they can trust the team to manage daily details instead of asking for daily standup reports.
