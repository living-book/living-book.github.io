---
type: Concept
title: The Five Whys
description: Repeatedly asking "why" about a problem, five times or more, to move past the first plausible cause and reach the actual root cause before acting.
book: toyota-production-system
chapters: [2]
tags: [root-cause, diagnosis, problem-solving, causality, method]
created: 2026-07-12
---

# The Five Whys

## Definition

The Five Whys is the practice of repeatedly asking why a problem occurred — not stopping at the first, most obvious answer — until the chain of causes bottoms out at something actually fixable. Ohno calls it deceptively hard: "it sounds easy" but is "difficult to do even though it sounds easy," because the instinct is to fix the first symptom encountered and move on.

## In the Book

Ohno's worked example (Chapter 2) is a machine that stopped: (1) why did it stop? an overload blew the fuse; (2) why the overload? insufficient bearing lubrication; (3) why insufficient lubrication? the pump wasn't pumping enough; (4) why not pumping enough? the pump shaft was worn and rattling; (5) why was the shaft worn? no strainer was attached, so metal scrap got in. Only the fifth answer — install a strainer — actually prevents recurrence; replacing the fuse or the pump shaft, the "obvious" first-order fixes, would let the same failure return within months. Ohno then generalizes the method beyond machine breakdowns: he describes the Toyota production system itself as having been "built on the practice and evolution of this scientific approach," and traces several of its core ideas back to a chain of whys — asking why one worker could run only one machine (leading to autonomation), why a part couldn't be made just-in-time (leading to production leveling), and why too many parts were being made (leading to visual control and eventually kanban). He is explicit that data are respected at Toyota but facts obtained by direct, repeated questioning matter more, "This is the scientific basis of the Toyota system."

## Why It Matters

Most fixes address the nearest cause to the symptom, because that's where the fix is cheapest and fastest to apply — but the nearest cause is rarely the actual cause, and patching it just resets the clock until the same failure recurs. The Five Whys is a discipline against stopping early: it forces the diagnosis past "what broke" to "what allowed it to break," which is usually a design or process gap rather than a component failure. The method transfers directly to any domain where symptom and cause are separated by several links of a causal chain — incident postmortems, recurring customer complaints, organizational dysfunction — wherever the temptation is to replace the fuse instead of asking why it blew.
