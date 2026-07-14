---
type: Concept
title: Describe a Behaviour Change, Not a Feature
description: Define a story's value as a measurable change in what someone does differently afterward, not as the feature or capability being built.
book: fifty-quick-ideas-user-stories
chapters: [1]
tags: [value, measurement, requirements, acceptance-criteria, behaviour]
created: 2026-07-14
---

# Describe a Behaviour Change, Not a Feature

## Definition

Value statements on stories routinely describe a capability someone will have ("being able to import contacts") rather than a change from their current state — and if the capability already exists, the statement provides no real success criterion at all. Drawing on Robert Brinkerhoff's principle that valuable initiatives produce "an observable change in someone's way of working," the book argues a story should name the specific before/after behaviour delta, quantified where possible: not "faster," but how much faster, from what, to what.

## In the Book

Chapter 1 works through a team stuck on acceptance criteria for a story to split a background import process in two — value framed as "being able to import contacts," even though users already could, and still would be able to, either way. Pushing to name the actual behaviour change surfaces the real problem: large contact files were timing out mid-HTTP-request, forcing users to re-upload and wait. Naming the change as "upload larger sets of contacts faster" opens a better solution (store the file and complete the request immediately, letting the same background job process it asynchronously) that is both cheaper and doesn't depend on speeding up the background process at all — the opposite of what the original story called for. The book also gives a "start to / stop doing" variant for brand-new capabilities: a trading team facing weeks of work to support a new product category instead "started to" trade it via a manual Excel log months before the full system shipped.

## Why It Matters

Naming the behaviour delta forces a "how much?" question that the original capability language hides, which both filters out non-stories (nothing will actually change) and opens better solution space (once you know why report speed mattered, you may not need to speed up reports at all). It's a general test for any initiative dressed up as a deliverable: state what will be different in someone's behaviour afterward, not what will exist — the same discipline behind outcome-based goals, OKRs, and theory-of-change models outside software.
