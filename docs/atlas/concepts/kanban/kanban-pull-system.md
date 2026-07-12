---
type: Concept
title: The Kanban Pull System
description: A capped number of signal tokens lets new work start only when finished work frees a token, pulling work through a system instead of pushing it.
book: kanban
chapters: [2, 6, 7]
tags: [pull-systems, visualization, queueing, self-organization]
created: 2026-07-12
---

# The Kanban Pull System

## Definition

A kanban system puts a fixed number of "signal" tokens into circulation, one per unit of work-in-progress. A new piece of work can start only when a free token is available; when work completes, its token is recycled and one new item is pulled in. This inverts the normal relationship between demand and capacity — work is pulled into the system when there is room for it, rather than pushed in on a schedule regardless of load — and it is made visible on a shared board so everyone can see what is flowing and where it is stuck.

## In the Book

Anderson traces the idea to an April 2005 visit to the Imperial Palace Gardens in Tokyo, where an attendant handed him plastic admission cards at the entrance that had to be returned at the exit — no money changed hands, and no explanation was given. He realized the cards weren't a security measure but a kanban system: a bounded number of tokens in circulation limits how many visitors are inside the park at once, and new visitors queue outside once the tokens run out (chapter 2). Applied to software, this becomes a "virtual kanban system" — there is no physical card, but the signal to pull new work is inferred by comparing the visual quantity of work-in-progress on a board against a stated limit. Chapter 2 is explicit that popular Agile "card walls" — index cards or sticky notes moved across a whiteboard — are "not inherently kanban systems... merely visual control systems": without an explicit WIP limit and a pull signal, a card wall only shows work, it doesn't govern it. Chapters 6 and 7 work through the mechanics — drawing a card wall, defining a work item card, setting input and output boundaries — that turn a visual board into an actual kanban system.

## Why It Matters

It separates *visibility* from *control*. Many teams put work on a board and believe they are managing flow, but without a binding limit on how much can be in progress at once, the board only documents the queue instead of shaping it. The same distinction generalizes to any system where units flow through stages with limited capacity — hospital beds, manufacturing cells, a personal task list — wherever "we can see the queue" is being mistaken for "we control the queue."
