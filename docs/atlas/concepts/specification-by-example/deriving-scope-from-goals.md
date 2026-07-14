---
type: Concept
title: Deriving Scope from Goals
description: Push back on requirements framed as solutions and derive project scope from the underlying business goal instead, often finding a cheaper answer.
book: specification-by-example
chapters: [2, 5]
tags: [requirements, scope, goals, collaboration, problem-framing]
created: 2026-07-12
---

# Deriving Scope from Goals

## Definition

Business users and customers almost always present requirements as solutions rather than goals — they specify what to build, not the problem it solves. Deriving scope from goals means treating the requested solution as one candidate answer, asking "why" and "who" until the real underlying goal surfaces, and then designing (or redesigning) scope from that goal collaboratively, rather than accepting the suggested scope as fixed. As Adzic puts it, scope itself "implies a solution," so passively accepting it is already accepting someone else's design.

## In the Book

Chapter 5 opens with the F-16 Fighting Falcon: the U.S. Air Force's original requirement was Mach 2-2.5 speed, but when designer Harry Hillaker asked why, the answer was "to escape from combat" — a goal satisfiable through superior agility rather than raw speed, which is what actually made the aircraft's 30-year production run possible. Adzic pairs this with Peter Janssens's story at a Belgian traffic-data company: a team spent four months and budgeted 100,000 euros for a web application to merge per-country Access databases, until an engineer asked "why" and "who" the day before go/no-go — discovering only ten people updated the data a few times a year — and solved it overnight by putting the existing database on a Citrix remote-desktop server instead. The chapter also covers using goals to simplify prioritization: Rob Park's team at a U.S. insurance provider stopped estimating individual stories once they anchored prioritization to business value at the feature level (e.g., "50% of support calls were about proof-of-insurance PDFs"), and instead just measured cycle time.

## Why It Matters

Every requirement handed to a delivery team is already a proposed solution, and accepting it at face value locks in whatever assumptions the requester made — often assumptions they never examined themselves. Asking "why" and "who" before "how" surfaces a cheaper, simpler, or altogether different design, and it converts prioritization from guessing relative effort to comparing goals people can actually explain. The same move generalizes to any handoff where a request arrives pre-packaged as a solution: interrogate the goal behind it before committing resources to build what was literally asked for.
