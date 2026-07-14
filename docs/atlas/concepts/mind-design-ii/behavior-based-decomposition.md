---
type: Concept
title: Behavior-Based Decomposition (Intelligence Without Representation)
description: Building intelligence as parallel layers that each connect sensing directly to action, rather than one central symbolic model, lets the world serve as its own model.
book: mind-design-ii
chapters: [15]
tags: [robotics, representation, decomposition, emergence, embodiment]
created: 2026-07-14
---

# Behavior-Based Decomposition (Intelligence Without Representation)

## Definition

Brooks proposes decomposing an intelligent system "by activity" instead of "by function": rather than chaining a perception module, a central symbolic reasoner, and an action module, each layer of a behavior-based system independently connects its own sensing to its own action, running in parallel with the others and deciding for itself when to act. His hypothesis: "Representation is the wrong unit of abstraction in building the bulkiest parts of intelligent systems" — because "it turns out to be better to let the world itself serve as its own model" than to build and maintain an internal symbolic description of it.

## In the Book

Brooks contrasts two engineering strategies. "Decomposition by function" — the traditional AI architecture — pipes a symbolic description from perception modules into a central reasoning system and out to action modules; he argues this leaves interfaces between modules unrealistic because researchers on each module choose both its inputs and outputs in isolation, and the resulting brittleness shows up in systems like MYCIN, which can diagnose bacterial infections yet has no model of what a human being even is. Against this he describes his own mobile robots, built by "decomposition by activity": a first layer that merely avoids obstacles is built, debugged, and set loose in the real world; a second layer, added later, injects motor commands to pursue distant visible goals while running in parallel with — and entirely unaware of — the first layer's obstacle-avoidance, which continues operating independently underneath it. He calls the resulting incremental, layered systems "Creatures," and argues each layer must be a complete, tested, real-world-operating system in its own right before the next is added.

## Why It Matters

This is a direct architectural alternative to the physical-symbol-system picture of intelligence: instead of a central representation mediating between sense and action, competence emerges from many parallel, world-coupled layers, each simple and robust on its own. It generalizes past robotics to any system-design question about whether central coordination through a shared model beats decentralized, task-specific components that interact directly with their environment and with each other.
