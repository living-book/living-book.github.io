---
type: Concept
title: Equivalence Relations Partition a Set
description: Any relation that is reflexive, symmetric, and transitive automatically carves its set into disjoint classes — equivalence and partition are the same structure viewed two ways.
book: logic-and-discrete-mathematics
chapters: [2, 5]
tags: [relations, abstraction, classification, sets]
created: 2026-07-12
---

# Equivalence Relations Partition a Set

## Definition

A binary relation R on a set X is an equivalence relation if it is reflexive (xRx),
symmetric (xRy implies yRx), and transitive (xRy and yRz implies xRz). The book builds
this definition directly from the informal notion of "sameness": every object is
equivalent to itself, equivalence goes both ways, and equivalence chains through a shared
middle term. Every equivalence relation on X generates equivalence classes [x]_R = {y ∈ X
| xRy}, and these classes are always pairwise disjoint and cover all of X — i.e., they form
a partition. The book proves the converse too: any partition of X defines an equivalence
relation (two elements related exactly when they're in the same block), so equivalence
relations and partitions are provably the same object described two different ways.

## In the Book

Section 2.5 grounds the definition with concrete examples on the integers: equality
itself, "having the same absolute value," and "having the same remainder when divided by
3" (which sorts every integer into exactly three classes: {...,-3,0,3,6,...},
{...,-2,1,4,7,...}, {...,-1,2,5,8,...}), plus similarity of triangles in the plane. The
book proves the key structural facts — x is always in its own class, and if x is in y's
class then their classes are identical, otherwise the classes are entirely disjoint — using
a proof by contrapositive. Chapter 5 revisits this machinery for congruence modulo n,
building modular arithmetic directly on top of equivalence classes and residue systems,
and Section 2.5.3 extends it to the "kernel equivalence" of a function f (x and y related
exactly when f(x)=f(y)), which is itself always an equivalence relation.

## Why It Matters

This is the formal machinery behind "ignoring irrelevant distinctions": whenever you
decide that some differences don't matter for the purpose at hand (two fractions with the
same value, two states with the same observable behavior, two people the same age bracket),
you are implicitly defining an equivalence relation, and the theorem guarantees your
groupings are automatically well-behaved — every item lands in exactly one group, with no
overlap or gaps. This underlies quotient constructions across mathematics and computing:
modular arithmetic, database normalization (grouping rows by a key), type systems
(equivalence up to isomorphism), and clustering (grouping by a similarity criterion) all
rest on the same guarantee that a good "sameness" rule automatically yields clean, non-
overlapping categories.
