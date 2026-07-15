---
type: Concept
title: "Face-to-Face Bug Fixing"
description: When testers find bugs, they immediately locate and talk to the developer who wrote the code, fix it together or watch the fix, instead of logging it in a system.
book: lean-from-the-trenches
chapters: [9]
tags: [communication, bugs, quality, lean-waste]
created: 2026-07-15
---

# Face-to-Face Bug Fixing

## Definition

Replace the bug tracker workflow (find bug → log it → change-control board → assign → developer picks up days later) with immediate synchronous collaboration: tester finds a bug, talks directly to the developer (often their embedded teammate), and the two fix it together or the developer fixes it while the tester watches. Only blockers or very high-priority bugs follow this path; lower-priority bugs can be logged if space exists in a capped tracker (30 bugs max in PUST).

## In the Book

Under the old process, testers would find bugs during system test at the end of the cycle and log hundreds of them. The change control board met weekly to prioritize them, and developers would pick them up later—context lost, code cold. After moving to Kanban with embedded testers in each feature team, the PUST team inverted this. When a tester found a bug, they'd write it on a pink sticky note (like any impediment) and walk over to the developer. In most cases, they knew who to talk to because they'd been working together all along. The developer and tester would sit down and fix it immediately, or the developer would fix it and report back within hours. Higher bandwidth (face-to-face), faster learning (both parties understand the code right then), faster fixes (context still hot), and less administrative waste (no meetings, no tracking overhead).

## Why It Matters

This flips the invisible assumption that bugs are administrative items that travel through formal channels. It treats bugs as urgent interruptions that deserve immediate attention, which changes the entire cost structure: the cost of a bug isn't the time to log and manage it, but the time the whole team wastes while the bug exists unfixed. Synchronous face-to-face collaboration is higher-bandwidth than asynchronous tracking, so even though the developer stops what they're doing, the total time to resolution is far shorter. This applies beyond bugs to any knowledge work where the bottleneck is context switching vs. context continuity.
