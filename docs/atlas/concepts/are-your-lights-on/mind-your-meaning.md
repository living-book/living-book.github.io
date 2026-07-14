---
type: Concept
title: Mind Your Meaning
description: A problem statement's words don't have one meaning until deliberately played with — through stress, negation, substitution, and paraphrase — to expose hidden disagreements.
book: are-your-lights-on
chapters: [10]
tags: [ambiguity, language, requirements, communication]
created: 2026-07-12
---

# Mind Your Meaning

## Definition

Ordinary sentences carry many latent readings, and people routinely assume
everyone present shares their own reading — an assumption that fails often enough
to be expensive. Because "mere quantity of effort" spent writing more carefully
or reading more carefully doesn't reliably fix this, the book prescribes an active
social process instead: "ONCE YOU HAVE A PROBLEM STATEMENT IN WORDS, PLAY WITH THE
WORDS UNTIL THE STATEMENT IS IN EVERYONE'S HEAD" — a deliberate practice of word
games rather than a one-time proofread.

## In the Book

A program specification stating "the exception information will be in the XYZ
file, too" was read by its writer as "the XYZ file is one more place this
information appears" (implying duplication existed elsewhere) and by the
programmer as "another kind of information the XYZ file holds is exception
information" (implying no duplication) — the gap cost roughly $500,000 in
unrecoverable data before anyone noticed the two readings diverged. The book
demonstrates the fix on the sentence "Mary had a little lamb": stressing each word
in turn produces a different implied meaning (not John's lamb; doesn't have it
anymore; not several; not a big one), and running "had" through a dictionary's 31
listed definitions turns the innocent sentence into open comedy. From this the
book compiles a "Golden List of Word Games" — swap MAY for MUST, AND for OR,
SOME for EVERY, replace a defined term with its explicit definition everywhere it
appears, replace persuasive words like OBVIOUSLY with the argument they're
standing in for — as reusable tools to run against any problem statement before
committing resources to it.

## Why It Matters

Ambiguity in a stated problem is invisible from the inside — everyone silently
substitutes their own most natural reading and feels no friction until the
divergent readings collide downstream, often after money has already been spent
in the wrong direction. Treating word choice as something to actively probe,
using small mechanical transformations rather than trusting careful reading,
converts a latent disagreement into a visible, cheap-to-resolve one before it
becomes an expensive, hard-to-trace one.
