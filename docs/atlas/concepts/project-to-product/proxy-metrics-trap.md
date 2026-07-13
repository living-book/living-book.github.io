---
type: Concept
title: The Proxy-Metrics Trap
description: Measuring transformation by activity (tools adopted, people trained, ceremonies held) instead of by business outcome lets an organization "succeed" on its own metrics while actually declining.
book: project-to-product
chapters: [2, 6]
tags: [measurement, metrics, incentives, goodharts-law, local-optimization]
created: 2026-07-12
---

# The Proxy-Metrics Trap

## Definition

An activity-based proxy metric measures whether the *mechanics* of a change happened
— how many people were trained, how many teams adopted a tool, how many ceremonies
run — rather than whether the change produced the intended business result. Kersten's
diagnosis is that these proxies can read as unambiguous success (every activity
checkbox ticked) while the underlying business outcome quietly fails, because the
proxy was never causally tied to the outcome it was meant to indicate. He pairs this
with **local optimization**: even a genuine improvement, if applied to a part of the
value stream that is not the actual bottleneck, produces measured activity without
moving the end-to-end result.

## In the Book

The book's central cautionary case is Nokia. Consultants used the "Nokia Test" —
questions about Scrum ceremony adherence — as proof that Agile scaled to large
enterprises, and by every activity metric Nokia's transformation was on track,
"right down to the adoption of the Agile tool." But Kersten's interviews found
developers suffering severe friction because the Symbian OS's architecture made
adding features extremely difficult — a bottleneck the activity metrics never
surfaced, because "the tie-in between business outcomes and software production
metrics was either not explicit or nonexistent." He states it plainly: "the proxy
metrics could deem the Nokia Agile transformation a success" while the actual
business result — the inability to shift to a software-and-screen-centric phone in
time to compete with the iPhone — failed. He generalizes this as Nokia's Agile
rollout being a *local optimization*: enormous investment went into making
development teams more agile, when development was never the bottleneck; the real
constraint was upstream, in an architecture and a business-to-engineering feedback
loop that no amount of team-level agility could fix. The same pattern reappears with
"LargeBank," whose billion-dollar transformation was tracked entirely against cost
reduction rather than business outcome — Kersten predicted its failure the moment he
saw the metric being used.

## Why It Matters

This concept names a specific failure mode of measurement systems: a metric that
correlates with success under old conditions keeps being reported as if it still
does, even after the causal link to the real outcome has broken (a close cousin of
Goodhart's Law, argued here through a concrete corporate autopsy rather than
abstractly). It gives a portable diagnostic — before trusting a metric, ask whether
it is tracking the *activity* of doing a thing or the *result* the activity was
supposed to cause, and whether the metric is scoped to the actual system bottleneck
or to a locally convenient but non-critical piece of it. That question applies
identically to training completion rates in a company, output metrics in a
bureaucracy, or vanity engagement numbers in a product.
