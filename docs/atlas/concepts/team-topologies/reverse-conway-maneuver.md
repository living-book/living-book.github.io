---
type: Concept
title: The Reverse Conway Maneuver
description: Deliberately design team boundaries first so that Conway's Law produces the software architecture you actually want, instead of discovering it as an accident.
book: team-topologies
chapters: []
tags: [organizational-design, software-architecture, conways-law, intentional-design, strategy]
created: 2026-07-12
---

# The Reverse Conway Maneuver

## Definition

Conway's Law observes that a system's architecture ends up mirroring the communication structure of the organization that built it. The Reverse Conway Maneuver inverts the causality on purpose: instead of letting architecture emerge as a byproduct of whatever teams already exist, an organization first shapes its team boundaries to match the architecture it wants, and lets Conway's Law then pull the software into that shape.

## In the Book

Step 4, "Use the 'Reverse Conway' approach," lists three things this maneuver is meant to accomplish: drive software systems that align to the flow of business change pressure, produce software architectures that are sustainable by the organization (not just technically elegant), and constrain — and align — the search space for technical solutions before they're chosen. The source names the technique and its intended payoffs but, consistent with its poster format, does not walk through a specific before/after reorganization example.

## Why It Matters

This concept turns a passive observation (organizational structure leaks into system structure) into an active lever: if you can't yet see the target architecture clearly, you can still shape the org toward the properties you want the eventual system to have (aligned to how the business actually changes, sustainable by the people who'll run it, with a narrowed and coherent solution space) and trust that structure to follow. It's a generalizable move wherever a structure you can't design directly is nonetheless shaped by a structure you can — team boundaries pulling architecture, but also, elsewhere, incentive structures pulling behavior, or interfaces pulling implementation.
