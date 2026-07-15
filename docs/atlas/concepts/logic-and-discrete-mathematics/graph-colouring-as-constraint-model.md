---
type: Concept
title: Graph Colouring as a Constraint Model
description: Recast "assign labels so that no two connected things share one" as colouring a graph's vertices — turning a scheduling or conflict problem into a solvable structural question.
book: logic-and-discrete-mathematics
chapters: [7]
tags: [graph-theory, constraint-satisfaction, modeling, reduction]
created: 2026-07-12
---

# Graph Colouring as a Constraint Model

## Definition

A colouring of a graph G assigns one colour to every vertex so that adjacent vertices never
share a colour; a graph is k-colourable if this is possible with k colours, and its
chromatic number χ(G) is the smallest such k. The move that matters is not the definition
itself but the translation step: any problem of the shape "assign values to items such
that conflicting pairs never match" can be re-expressed as a graph — items become vertices,
conflicts become edges — and solving the original problem becomes finding χ(G) or a
k-colouring.

## In the Book

Section 7.7 motivates colouring with radio-frequency assignment: stations become vertices,
an edge connects two stations whose broadcast areas overlap, and assigning interference-
free frequencies becomes exactly the graph-colouring problem, with the number of available
frequencies as k. The book's centerpiece application of this translation is the four-colour
problem: representing each country on a map as a vertex and drawing an edge between any two
countries sharing a border, it shows a one-to-one correspondence between planar graphs and
maps, so "can every map be coloured with four colours so neighbouring countries differ"
becomes the purely graph-theoretic Theorem 7.7.3, "every planar graph is 4-colourable"
(proved by Appel and Haken in 1976 using 1200 hours of computer case-checking). The book
also proves the weaker five-colour theorem by induction on vertex count, and separately
applies the same graph-colouring lens to Sudoku, representing cell constraints as a graph
whose proper 9-colourings are exactly the valid solutions.

## Why It Matters

Once a problem is recast as graph colouring, decades of graph theory (chromatic number
bounds, planarity results, colouring algorithms) become available for free — the hard part
of solving the problem shifts to the easy part of noticing it fits an existing pattern.
This modeling move — turning "conflicting pairs" into edges and "valid assignment" into
proper colouring — generalizes far past maps: exam/room scheduling, register allocation in
compilers, and any resource-assignment problem with pairwise conflicts are all graph-
colouring problems in disguise. The larger lesson is that finding the right structural
representation of a problem can be more valuable than any cleverness applied within a
naive representation.
