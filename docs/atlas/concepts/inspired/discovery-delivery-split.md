---
type: Concept
title: Discovery and Delivery as Two Tracks
description: Fast, cheap, disposable experiments to learn whether an idea is worth building run continuously alongside — not before — the slow, careful work of building it right.
book: inspired
chapters: [33]
tags: [experimentation, learning, workflow, risk-reduction, feedback]
created: 2026-07-12
---

# Discovery and Delivery as Two Tracks

## Definition

Cagan distinguishes two activities that a strong product team runs continuously and in parallel, not sequentially. Delivery is the work of building production-quality software: scalable, tested, instrumented, maintainable, releasable with confidence — the part most teams already know how to do well. Discovery is the work of finding out, fast and cheap, whether a given idea is even worth that delivery effort — and Cagan argues most teams are far worse at this half. The two tracks have opposite operating rules: discovery optimizes for speed and is allowed to be sloppy and throwaway; delivery optimizes for quality and cannot be.

## In the Book

The introduction to Part IV states the mechanism directly: "the purpose of product discovery is to make sure we have some evidence that when we ask the engineers to build a production-quality product, it won't be a wasted effort." Cagan defines "product" narrowly — reserving the word for something that can actually run a business on it, with the regression tests, analytics, internationalization, and brand consistency that implies — precisely so the cost of getting delivery wrong is visible. Doing that full weight of engineering work before the product manager even knows the idea is right, he writes, "is a recipe for product failure and big waste."

Chapter 33 grounds the two tracks in the four risks (value, usability, feasibility, business viability): discovery techniques are built to test each of these against real users and stakeholders without requiring developer time or pushing experiments into production. Discovery's job is explicitly framed around speed — trying out many ideas and, for the promising ones, multiple approaches — because Cagan's working assumption is that most ideas won't survive contact with real customers, so the cost of finding that out has to stay low.

## Why It Matters

Collapsing discovery and delivery into one sequential pipeline — decide, then build, then find out if it worked — means the expensive, hard-to-reverse work happens before the cheap, easy-to-reverse learning does. Running them as separate, differently-tuned tracks lets an organization spend its cheap-and-fast budget liberally (many ideas, most of them discarded) while reserving its slow-and-careful budget only for what has already survived contact with reality. The pattern generalizes to any system that must both explore possibilities and commit resources: keep the exploring loop fast and disposable, and let it gate entry into the expensive, quality-bound loop rather than running behind it.
