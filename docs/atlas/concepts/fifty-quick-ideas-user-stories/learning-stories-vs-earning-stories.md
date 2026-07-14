---
type: Concept
title: Learning Stories vs. Earning Stories
description: Split investigation work into its own time-boxed story with an explicit information goal, instead of disguising research as a feature story nobody can estimate.
book: fifty-quick-ideas-user-stories
chapters: [4]
tags: [research, estimation, uncertainty, planning, scope]
created: 2026-07-14
---

# Learning Stories vs. Earning Stories

## Definition

Work that involves a genuine unknown — an unfamiliar third-party API, a migration risk, a new standard — can't be honestly estimated, because nobody knows what it entails until they've investigated it. Rather than disguise this as a feature story ("As a developer, I want to understand how the new external API works") or leave it as an unbounded background task, the book proposes naming it a *learning story*: a time-boxed investigation with an explicit goal — the specific information stakeholders need to make a planning decision — as distinct from an *earning story*, which delivers value directly to end-users.

## In the Book

Chapter 5 traces the failure mode: vague investigation work introduces variability that breaks short-term planning, and fake "developer stories" have no real acceptance criteria because there's no way to specify what "understanding the API" looks like when done. The fix is to make the learning story's output an explicit deliverable — negotiated with stakeholders up front: what information do they need to approve or reject the real work, how much detail, is a quick prototype needed or is a written list of risks enough — and then timebox it, so a team commits only to the investigation, not to a vague promise of eventual delivery. The book adds a citation to Larman and Vodde's warning against overusing this pattern: it should be reserved for genuine "study far outside the familiar," not become a cover for ordinary solution design.

## Why It Matters

Separating "we don't know yet" from "we're going to build this" keeps uncertainty from silently corrupting a team's velocity and estimates — a learning story can honestly fail to reach a conclusion, and that failure is itself useful information, whereas a disguised feature story that "fails" looks like a broken commitment. The same split — bound the cost of finding something out, separately from committing to act on what you find — applies to due diligence, pilot studies, spikes, and any planning process where estimation is being forced onto genuine unknowns.
