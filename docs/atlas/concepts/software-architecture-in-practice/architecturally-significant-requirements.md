---
type: Concept
title: Architecturally Significant Requirements
description: The small subset of a system's requirements that will actually shape its structure — everything else is downstream detail that any competent design can absorb.
book: software-architecture-in-practice
chapters: [16]
tags: [requirements, prioritization, architecture, design-drivers, elicitation]
created: 2026-07-12
---

# Architecturally Significant Requirements

## Definition

Architecturally significant requirements (ASRs) are the requirements that will have profound effects on the architecture — as opposed to the majority of a requirements document, which any reasonable design can satisfy without special structural provision. The term originates with the Software Architecture Review and Assessment group. Locating them, rather than trying to design from the full requirements document, is what lets an architect start designing at all.

## In the Book

Chapter 16 gives three methods for surfacing ASRs: mining existing requirements documents (the book's discussion question has readers literally color-code a spec — red for irrelevant, yellow for maybe, green for architecturally significant — and reports that most documents turn out mostly red), interviewing stakeholders directly, and running structured elicitation exercises such as a Quality Attribute Workshop or PALM (Pragmatic Architecture Leverage Method) that traces ASRs back to explicit business goals rather than treating them as self-evident. The gathered ASRs are then organized into a utility tree — a hierarchy that starts from coarse quality attribute categories (performance, modifiability, security...) and refines them down to concrete, prioritized six-part scenarios at the leaves. That prioritized tree becomes, in the book's words, the architect's "marching orders." Chapter 17 then makes ASRs the explicit input to the Attribute-Driven Design method: at each decomposition step, the architect marshals the ASRs relevant to that part of the system before choosing a design concept.

## Why It Matters

This concept names a triage discipline applicable anywhere a large, undifferentiated set of stated requirements or demands must be turned into a small number of structural commitments. Most requirements are satisfiable by competent execution and don't constrain the shape of the solution; a few are load-bearing and, if missed, force expensive rework later. The ASR move — actively hunting for the requirements that constrain structure, rather than accepting the full list as equally weighted — generalizes to any planning process where "requirements gathering" risks becoming an undifferentiated wish list instead of a small set of real design drivers.
