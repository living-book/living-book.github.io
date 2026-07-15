---
type: Concept
title: "Staged Release Audiences"
description: "Releasing completed work through multiple tiers—internal team, early adopters, preview audience, public—to gather feedback and catch issues at increasing scale before full release."
book: agile-pm-with-kanban
chapters: [4, 6]
tags: [deployment, kanban, continuous-delivery, feedback]
created: 2026-07-15
---

# Staged Release Audiences

## Definition

Rather than releasing once, Brechner's Xbox team releases the same completed work through multiple concentric audiences: first to the product development team ("dog food"), then to a passionate early adopter community, then to a broader preview audience, finally to all customers. Each release is a complete, production-quality build that's been through the same Validate done rule. Feedback from each tier drives fixes before the next tier sees it.

## In the Book

Brechner describes Xbox One's model: "We released new platform builds to the Xbox product team weekly, then to the early adopter program the week after, and then to a preview audience monthly. We released fixes immediately for issues found by each audience." This wasn't a beta program of incomplete half-tested builds; each build met Kanban's done rules—production-ready. The key difference from Waterfall's beta is timing and frequency. Instead of waiting months to release to one beta audience, he's releasing weekly to insiders, bi-weekly to adopters, monthly to preview, then public a few weeks later.

The benefits include: product team learns first, uses what they ship; early adopters get genuine feature richness and reliability, becoming true evangelists; preview audience gives a two-week window for last-minute issues before public; public release is low-risk because issues have been found and fixed already. The logistics (dog food, early adopter signup, preview program) already existed from earlier Xbox releases; moving to a monthly cadence just accelerated the process.

## Why It Matters

This approach lets quality bake in gradually while revenue and adoption ramp. A bug found by the product team is fixed in days, not escalated to a triage meeting months later. Feedback from early adopters informs the next release's priorities, not post-release patches. The preview audience sees the product in near-final form, reducing shock and support burden at launch. By the time it hits public, the team has already addressed the categories of real-world use, not just lab scenarios. This requires Kanban's continuous delivery capability—if releases happen quarterly, you can't afford to stage through four tiers; if they happen monthly or more, the added logistics are worth the risk reduction.

---

*related concepts: continuous-publishing (CATALOG), continuous-deployment (CATALOG), validated-learning-discovery (CATALOG)*
