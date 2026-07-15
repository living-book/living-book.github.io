---
type: Concept
title: "Potentially Consumable Solution"
description: "Every iteration delivers not just working software, but a solution ready for use: tested, documented, operationally prepared, addressing real user concerns."
book: disciplined-agile-delivery
chapters: [1, 13, 15]
tags: [delivery, solution, quality, completeness, stakeholder-value]
created: 2026-07-15
---

# Potentially Consumable Solution

## Definition

Scrum delivers "potentially shippable" software—code that is built, tested, and integrated. DAD extends this to potentially *consumable* solutions: work products that are not just functionally correct but are deployable, usable, and valuable to real stakeholders. A consumable solution addresses the full scope of making something work in the real world: functional correctness, performance, security, data migration, user documentation, operations procedures, training materials, and stakeholder sign-off. The phrase "potentially" means the team does not require stakeholder permission to declare work done; it means the work is genuinely ready to use if the stakeholder chooses to release it.

## In the Book

Chapter 1 introduces the concept in contrast to Scrum's "potentially shippable software." Chapters 13–15 detail how Construction iterations produce consumable solutions through deliberate inclusion of non-software activities: requirements envisioning (so features address real needs), iteration modeling (so design is visible and reviewable), regression testing (so code doesn't regress), documentation (so users and operations understand the system), and stakeholder demos (so feedback shapes the solution's evolution).

The book explicitly addresses the false dichotomy between "shippable" and "consumable." Many teams deliver code that technically ships but is not consumable: it lacks necessary operational setup, has no user guide, is insecure without configuration, or lacks the data migration that makes it actually usable. Conversely, some teams over-invest in documentation and procedure that could be addressed during Transition. DAD guides teams to the balanced middle: produce something that a stakeholder could genuinely use tomorrow if business conditions warranted, without over-engineering transition activities that belong in the Transition phase.

The book acknowledges that consumability is context-dependent. For a web application, a potentially consumable increment might be a feature set tested end-to-end in a production-like environment, with API documentation and user-facing messaging. For a regulated medical device, it would include regulatory compliance documentation, validated test reports, and operational procedures. For an internal business system, it would include training scenarios and data migration scripts. The form follows the context, but the principle is constant: the team does not hand off half-baked work to QA or operations; they take ownership of the whole value chain.

## Why It Matters

The shift from "shippable software" to "consumable solution" forces teams to think about the total value delivered, not just code written. It makes visible the hidden work that waterfall buried in separate testing and operations phases, exposing waste and delays. When a team must make an increment consumable every iteration, they either find ways to parallelize testing and operations work with development, or they surface the realistic cost of doing so and adjust expectations accordingly. For enterprises, this is powerful: it prevents the common pattern of "agile" teams shipping code at high velocity while operations groans under impossible deployment demands. It also forces earlier engagement with stakeholders on non-functional concerns—performance, security, scalability, user experience—that are often afterthoughts in software-centric delivery.

