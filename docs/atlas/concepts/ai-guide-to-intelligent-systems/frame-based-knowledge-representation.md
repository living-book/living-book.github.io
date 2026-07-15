---
type: Concept
title: Frame-Based Knowledge Representation
description: Bundle everything known about one object or concept — attributes, defaults, and attached procedures — into a single named structure, instead of scattering facts across independent rules.
book: ai-guide-to-intelligent-systems
chapters: [5]
tags: [knowledge-representation, expert-systems, object-oriented, inheritance, structure]
created: 2026-07-12
---

# Frame-Based Knowledge Representation

## Definition

A frame is a data structure holding the typical knowledge about a particular object or concept, organized into named slots — attributes like name, weight, or price — each of which can carry a value, a default value used "when no evidence to the contrary has been found," a range that a valid value must fall within, or a procedure that computes or reacts to the value. Frames related by class (a specific computer frame belonging to the class Computer, which belongs to the class Hardware) inherit slot values and defaults down the hierarchy unless overridden. Frames are, in the book's framing, expert systems' version of object-oriented programming: an object combining data structure and behavior in one entity, first proposed by Marvin Minsky in the 1970s.

## In the Book

Chapter 5 motivates frames against the limits of pure rule-based systems: a rule-based system's facts are scattered through the entire knowledge base, so answering a question about, say, Qantas frequent flyers can mean searching through irrelevant knowledge about other airlines' passengers. Frames fix this by collecting all the relevant facts about one entity into a single structure, illustrated with paired airline boarding-pass frames (`Carrier`, `Gate`, `Seat`) and a `Person`/`Computer` example showing typed slots (symbolic, numeric, Boolean) and default values (a car frame defaulting to four wheels). The chapter covers slot procedures in detail — WHEN CHANGED and WHEN NEEDED "demons" that fire automatically when a slot's value is set or requested — and inheritance through frame hierarchies, before building BUY SMART, a demonstration frame-based expert system that recommends a personal computer purchase by combining frames with production rules, showing frames and rules working together rather than as competing techniques.

## Why It Matters

Frames formalize a design instinct that recurs whenever information about one entity needs to be looked up together instead of reconstructed by scanning a flat pile of independent facts: bundle everything about the entity — its own values, the defaults it inherits from its type, and the behavior triggered when those values change — into one addressable structure. This is the same shape as a class in object-oriented programming, a document schema with inherited templates, or a customer record that defaults to its account tier's settings until overridden — the payoff is locality (you know where to look) and inheritance (you don't have to restate what's already true of the category).
