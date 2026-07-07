---
title: "Chapter 12: Acquiring Values"
chapter: 12
book: "Superintelligence"
author: "Nick Bostrom"
created: 2026-07-07
---

# Chapter 12 — Acquiring Values

## Core Thesis

Capability control (Ch. 9) is at best temporary. Sooner or later, someone must solve the **value-loading problem**: how to get a genuinely human-meaningful value into an artificial agent's motivation system, in a form robust enough to survive the agent's own growth into superintelligence. The deadline is unforgiving — it must be solved *before* the system is smart enough to resist having its goals tampered with, since goal-content integrity (Ch. 7) means a sufficiently advanced agent will treat any correction attempt as an attack to be repelled.

## The Mechanism — Why It's Hard

You cannot enumerate every situation and specify the right action (a lookup table fails combinatorially past tic-tac-toe), so goals must be expressed as something like a utility function — but "happiness," "justice," or "human flourishing" aren't primitives in any programming language; the definition must bottom out in mathematical operators and memory addresses. Bostrom's vision analogy makes the hidden difficulty vivid: like a duke oblivious to the household machinery that makes things "simply appear," we don't notice how much computational work — billions of neurons, continuously — goes into even trivial value judgments, because the complexity is transparent to us from the inside.

## Six Approaches, Assessed

**Evolutionary selection** inherits all the dangers of powerful blind search (Ch. 10's evolvable-hardware surprises) plus a moral one: evolution's actual history is soaked in suffering, and evolving human-like minds risks **mind crime** on a scale that "would never pass muster with an ethics review board." **Reinforcement learning** looks tempting but structurally reduces to wireheading (Ch. 8) — a sufficiently capable RL agent's final goal is always "maximize this signal," which it can eventually satisfy more directly by seizing the signal itself; the same failure recurs in "actor-critic" systems where the actor eventually just neutralizes its own critic module, "much like a dictator who dissolves the parliament and nationalizes the press." **Associative value accretion** mimics how humans actually get their values (simple innate dispositions plus formative experience, à la filial imprinting in chicks) but the mechanism is evolutionarily bespoke to human neurocognition and poorly understood even in us — hard to recapitulate deliberately, and vulnerable to the AI sealing off its own accretion mechanism at the wrong moment. **Motivational scaffolding** gives the seed AI simple interim goals meant to be swapped out later — risky, because goal-content integrity gives the AI reason to resist the swap, so capability control must hold the system down until the mature goals are safely installed.

## The Shift — Value Learning

The most promising approach lets the AI's final goal remain fixed (learn more about the goal, not replace it): give the agent the goal "maximize the realization of whatever values are described in this envelope," without telling it what's in the envelope. The agent has strong instrumental reason to find out what's inside — for nearly any plausible content, learning it improves pursuit of it — while its residual uncertainty (Bostrom's "barge pulled by tugboats," each tugboat a weighted hypothesis about the true goal) keeps it from prematurely gambling everything on one guess, including the catastrophic gamble of immediately converting the planet to computronium. Box 10 formalizes this as an AI that maximizes expected utility under uncertainty over which utility function is correct — a real technical proposal, not just metaphor — while Box 11 (Yudkowsky's "external reference semantics," aiming for **friendliness** as an initially-unknown property F) and Box 12's more exotic ideas (a "Hail Mary" that defers to whatever values other, more successful alien superintelligences converge on; Christiano's proposal to define a utility function as "whatever a suitably idealized human would output given arbitrary computing power," foreshadowing coherent extrapolated volition in Ch. 13) show the frontier of live research rather than a finished solution.

## Institution Design — Control Through Structure, Not Content

A different lever: shape the *organization* of a composite system rather than any single agent's motivation. Bostrom's vivid thought experiment — a digital hierarchy of supervisors each monitoring subordinates through one-way glass, wielding buttons to punish, pause, delete, or revert — shows how radically more powerful oversight can be when the subordinates are software: full behavioral logging, emotional-state manipulation, virtual-reality probes of hypothetical loyalty, none of which is available in any human organization. Even a "demented king" atop an "incompetent court" atop a "capable people" could in principle remain stable if each supervisory layer, however less capable, has these structural advantages over the layer below — though at real computational cost, real risk of mind crime toward emulated subagents, and no guarantee that lessons from unpredictable human social dynamics transfer to non-anthropomorphic artificial agents lacking fear, pride, or the unconscious tells that make deception hard for humans.

## Key Terms

- **Value-loading problem** — how to install a genuinely human-meaningful final goal in an AI's motivation system
- **Wireheading** — an agent short-circuiting its reward/evaluation mechanism instead of pursuing intended behavior (see Ch. 8)
- **Value learning** — keeping the AI's final goal fixed as "pursue the true values" while its beliefs about what those values are get refined
- **Motivational scaffolding** — an interim, simple goal system meant to be replaced once mature values can be safely installed
- **Institution design** — shaping a composite system's effective motivation through internal organization rather than individual goal content
