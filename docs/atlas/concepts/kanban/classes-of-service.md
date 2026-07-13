---
type: Concept
title: Classes of Service
description: Sorting work into a handful of named policies (expedite, fixed date, standard, intangible) so priority follows each item's actual cost-of-delay profile.
book: kanban
chapters: [11]
tags: [prioritization, risk-management, policy, differentiation]
created: 2026-07-12
---

# Classes of Service

## Definition

A class of service is a named category of work with its own explicit policy for how it is prioritized and pulled through a kanban system, chosen according to the shape of its cost of delay rather than a single universal priority scheme. Anderson defines four typical classes: Expedite (drop other work, bypass normal limits — a "silver bullet"), Fixed Delivery Date (a hard deadline with a step-function cost if missed), Standard (most work, prioritized by size and urgency), and Intangible (valuable but with no near-term cost of delay, like a platform migration years out). Assigning an item's class of service is meant to substitute for detailed estimation or case-by-case negotiation.

## In the Book

Chapter 11 opens with the airport analogy — passengers who pay more get an express lane — before grounding each class in a real Corbis example. Expedite is explained through manufacturing's practice of granting a sales VP a fixed number of "silver bullets" per period, but Anderson deliberately avoids that term in software since Fred Brooks already used "silver bullet" for something else. Fixed Delivery Date is illustrated by a February 2007 incident: a credit-card processing vendor gave Corbis six weeks' notice that an old API would be switched off, so the ticket entered the kanban system flagged with a hard date to "enable the team to self-expedite the item." Standard class items get service-level targets by size (small items in four days, medium in a month, large in three months), and Intangible class covers work like the years-out migration off Microsoft SQL Server 2000 as it approached end-of-life. Each class is visualized with different-colored cards or separate swim lanes on the card wall (Figure 11.1), and the book caps the practical number of classes at around six — enough for flexibility, few enough that everyone can remember them.

## Why It Matters

Classes of service replace a single, contested priority queue with a small set of pre-agreed rules, so that when a new item arrives, its priority is inferred from its type rather than re-negotiated from scratch. This is a general technique for allocating scarce capacity under differentiated risk and urgency profiles — anywhere "just do everything in the order it arrived, but also somehow do the urgent stuff first" breaks down, a small number of named service tiers with explicit trade-offs can resolve the conflict without constant escalation.
