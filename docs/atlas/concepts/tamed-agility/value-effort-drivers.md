---
type: Concept
title: Value and Effort Drivers
description: "A system of visual annotations on model elements (features, processes, data) that explicitly identify which ones create business value, user value, complexity, or risk, making prioritization decisions transparent and traceable."
book: tamed-agility
chapters: [2, 5, 6, 8]
tags: [requirements-prioritization, visual-communication, decision-transparency, stakeholder-alignment, annotation-system]
created: 2026-07-15
---

# Value and Effort Drivers

## Definition

Value and effort drivers are a set of symbolic annotations that stakeholders apply to model elements during Interaction Room workshops to explicitly mark *why* something matters and how difficult it will be. Business value markers indicate features essential to the system's purpose; user value markers indicate features users want; effort markers indicate factors that increase complexity (security requirements, integration dependencies, policy constraints, flexibility needs, uncertainty). By making these drivers visible as symbols on the wall models, the team creates a shared, traceable record of what stakeholders care about and why, allowing informed trade-offs when scope or resources shift.

## In the Book

The Interaction Room uses dozens of annotation symbols applied to elements on process, object, feature, and interaction canvases. Common effort drivers include: security (needs special access controls), reliability (must never fail), flexibility (must adapt to future changes), policy constraint (regulatory requirement), complexity (needs expert knowledge), uncertainty (stakeholders don't yet agree on the requirement), accuracy (needs careful validation), automation (previously manual, now IT-supported), and external resource (depends on third-party systems).

Value drivers include: business value (creates essential value for the organization), user value (creates value users will notice and want), and innovation (introduces new business or technical capability). A feature marked with high business value and high effort is likely a critical priority. A feature marked high effort but no value is a candidate for deferral. Most critically, elements marked with multiple effort drivers *and* value drivers are red-flagged as high-risk: high effort + uncertainty + high value means the team needs to tackle the uncertainty early or be prepared for failure.

The annotations are discussed face-to-face during workshop rounds. The IR domain coach asks stakeholders to explain their annotations, and their reasoning is recorded. This serves two purposes: first, it ensures that "security" means the same thing to the business expert and the architect (not always obvious), and second, it forces explicit prioritization conversations ("If that feature is both high-effort AND uncertain, do we still want to do it in the first sprint?") that would otherwise remain unspoken.

The book illustrates this in the Cura case study (Chapter 19), where process canvas elements were annotated with business value, user value, and effort drivers, then the team used these annotations to prioritize which business processes were essential for the first sprint and which could wait. Process steps marked with both external resource and business value constraints (e.g., "our vendor's API is new and unpredictable") got special attention in risk planning.

## Why It Matters

Value and effort drivers matter because they make tacit knowledge explicit. When a stakeholder says "that's important," the reason why is often implicit: important to the business? Important to the user? Important because it's mandated by law? Different stakeholders may think "important" means different things. By naming the driver symbolically and discussing it, the team ensures alignment and creates a record that justifies later trade-offs. A team can say "We deferred feature X because it was low business value, and now that's been documented so we can explain it to the C-suite." Effort drivers serve a similar function: by marking sources of complexity explicitly, the team can estimate more accurately (a feature marked "accuracy" signals "this needs careful testing") and allocate expertise (assign the best security engineer to features marked "security").
