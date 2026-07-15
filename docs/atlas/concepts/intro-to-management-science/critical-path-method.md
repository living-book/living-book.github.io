---
type: Concept
title: Critical Path Method
description: Map a project as activities with predecessor dependencies and durations to find the one chain of activities whose total time sets the project's minimum completion time.
book: intro-to-management-science
chapters: [9]
tags: [scheduling, project-management, constraints, coordination, modeling]
created: 2026-07-12
---

# Critical Path Method

## Definition

PERT/CPM models a project as a network of activities, each with a duration and
a list of immediate predecessors that must finish before it can start. Adding
up the longest chain of dependent activities from start to finish gives the
project's minimum possible completion time, and that chain is the critical
path: every activity on it is "critical" — any delay to a critical activity
delays the whole project — while activities off the critical path have slack,
meaning they "can be delayed... before they cause an increase in the total
project completion time" without changing the finish date.

## In the Book

Chapter 9 works the method through the Western Hills Shopping Center expansion
project, listing activities such as "Prepare architectural drawings"
(activity A, 5 weeks, no predecessor), "Identify potential new tenants"
(activity B, 6 weeks, no predecessor), "Develop prospectus for tenants"
(activity C, 4 weeks, depends on A), and "Select contractor" (activity D, 3
weeks, depends on A), building out a full activity-predecessor-duration table
before constructing the network diagram and computing the critical path and
project completion time. The book distinguishes PERT (developed for the Navy's
Polaris missile project, built to handle activities whose durations were
genuinely uncertain) from CPM (developed at DuPont for industrial projects
with known activity times and known cost/time trade-offs for compressing
them), and revisits the same shopping-center project later in the chapter
under uncertain activity times to show how probabilistic durations change
which path is likely to be critical.

## Why It Matters

Not every task in a complex project matters equally to the deadline — the
critical path identifies exactly which activities the project manager must
protect and which have room to slip without consequence, replacing a
generalized sense of "everything is urgent" with a specific, defensible answer
about where schedule risk actually concentrates. That distinction — a small
subset of a system's parts that fully determines its overall throughput time,
with everything else carrying slack — is the same structural insight that
recurs anywhere dependent tasks compete to determine an aggregate deadline.
