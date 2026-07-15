---
type: Concept
title: Production Metrics Over Process Metrics
description: The true measure of team success is not how much code is written or how many tasks are completed, but what customers actually do with the software in production.
book: agile-metrics-in-action
chapters: [6, 10]
tags: [measurement, customer, business, impact, outcomes]
created: 2026-07-12
---

# Production Metrics Over Process Metrics

## Definition

Process metrics (velocity, code coverage, deployment frequency, pull request approval time) measure activity inside the development cycle. Production metrics (user engagement, conversion rate, error rate, feature adoption) measure what actually happens when customers use the software. A team can look great on process metrics—shipping fast, testing coverage at 95%, low MTTR—while shipping features nobody uses or that actively harm the business. Production metrics prevent this misalignment by making customer impact the final measure.

## In the Book

Chapter 6 is dedicated to production data. The book shows that a team practicing continuous delivery and deploying multiple times a day can feel successful (deployment frequency is high, velocity is consistent) but still miss the mark if customer engagement isn't moving.

The case study is particularly stark: a development team moved to DevOps, automated everything, and was delivering new features multiple times per day. In their biweekly report, the BI team showed that conversion rate and site stickiness (how long users stay) hadn't changed. The team was shipping features, but customers weren't adopting them.

The fix wasn't to ship faster or with more features — it was to involve the BI team in sprint planning. For every new feature, the team now asks: "What is the business value? How do we measure it? Does it affect conversion or engagement?" Then they add custom metrics to production (button clicks, feature adoption, search queries) and track them for each release. Only when they see that a feature is actually being used do they celebrate delivery.

The book also covers semantic logging and arbitrary metrics — instrumenting production to capture customer behavior that matters to the business. Rather than just tracking page views, log what customers search for, which recommendations they click, which checkout steps they abandon. This turns production monitoring from "is the system up?" into "what are customers actually doing?"

## Why It Matters

Process metrics are leading indicators — they tell you if conditions are right for success. Production metrics are outcome indicators — they tell you if you've actually succeeded. Both matter. A team with poor process metrics (low velocity, high recidivism) is unlikely to deliver customer value. But a team with excellent process metrics and poor production metrics is optimizing for the wrong thing. Production metrics anchor the feedback loop: if a feature ships and customer engagement doesn't improve, that's data the team needs immediately to decide whether to refine the feature, kill it, or double down. Without production metrics, teams can work hard, feel successful, and still miss the goal.
