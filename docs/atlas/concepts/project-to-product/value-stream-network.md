---
type: Concept
title: Value Stream Network
description: Software delivery is a rerouteable network of collaborating tools and people, not a linear production line — so its bottlenecks behave like traffic, not like a stalled conveyor belt.
book: project-to-product
chapters: [1, 7, 9]
tags: [network-topology, bottlenecks, visibility, systems-thinking, tooling]
created: 2026-07-12
---

# Value Stream Network

## Definition

Kersten's third epiphany, arrived at after repeatedly failing to map software
delivery onto a manufacturing-line metaphor: the flow of business value through an
organization's people, processes, and tools is not a linear pipeline but a **Value
Stream Network** — structurally closer to an airline route map than to an assembly
line. In a linear process a single blocked dependency halts everything downstream; in
a network, work reroutes around a constraint the way air traffic reroutes around bad
weather, with some delay but without a full stop. This means the "find the bottleneck
and fix it" logic borrowed wholesale from Lean manufacturing doesn't transfer to
software delivery unmodified.

## In the Book

The epiphany came from Kersten's own team at Tasktop: while he kept pushing for
manufacturing-style Value Stream Mapping diagrams, colleague Nicole Bryan's
visualizations of how delivery artifacts actually flowed through internal value
streams looked nothing like a production line and everything like an airline network
(Figure 9.1). This resolved a puzzle he'd been stuck on — that real delivery teams
facing a blocker (a UX team with no bandwidth, an API a team hadn't built yet) don't
halt like a stopped assembly line; they reroute, building their own workaround APIs or
borrowing skills from adjacent teams, and the reroute itself becomes a defect or debt
flow item to reconcile later. This network structure is grounded empirically in
Kersten's "Mining the Ground Truth of Enterprise Toolchains" study of 308 enterprise
IT organizations' tool networks (Chapter 7) — since nearly every action a developer
takes is tracked in some tool, the tool network itself is the only reliable "ground
truth" of how work actually moves, comparable to a Gemba walk of the production floor
but for knowledge work. The book explicitly rejects the idea that a company could just
copy BMW's Leipzig plant: the plant's paint-shop bottleneck is fixed and visible to
every employee walking past the cafeteria, while a software bottleneck can appear,
get routed around by a creative team, and vanish before management even notices it.

## Why It Matters

This concept warns against importing bottleneck-hunting techniques from linear
systems (assembly lines, pipelines, single-threaded processes) into any system that
is actually a network with alternate paths — the diagnostic question shifts from
"where is the one blocking step" to "where does reroute traffic concentrate, and what
is the hidden cost of the workarounds." It applies to any organization whose real
structure (communication paths, dependency graphs, actual collaboration patterns) is
more densely connected than its org chart suggests — the network is the ground truth,
and the chart is a convenient fiction.
