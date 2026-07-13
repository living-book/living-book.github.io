---
type: Concept
title: Axis Shenanigans
description: Manipulating a graph's axes — truncating, omitting labels, breaking continuity, or stretching scale — makes the eye draw a false conclusion the numbers don't support.
book: field-guide-to-lies
chapters: [1]
tags: [data-visualization, graphs, deception, perception, measurement]
created: 2026-07-12
---

# Axis Shenanigans

## Definition

Because the human eye reads visual patterns far more readily than tables of numbers, a graph's axes — their labels, starting point, continuity, and scale — do most of the persuasive work, independent of the underlying data. A graph can be numerically accurate and still visually lie, by choosing an axis treatment that exaggerates or minimizes the difference the data actually shows.

## In the Book

Levitin catalogs the specific techniques: unlabeled axes (a conference poster comparing "SZ" and "HCs" on a y-axis with no units, so the reader cannot tell what is even being measured); a truncated vertical axis, illustrated by a 2012 Fox News graph of the Bush tax cuts expiring, where a bar six times the height of another visually implies a 600% tax hike when the real change is 35% to 39.6% — a 13% relative increase, made obvious once the axis is redrawn starting at zero; a discontinuous axis, where a steady 5%-per-year crime increase is made to look like a dramatic spike by compressing five years of data into the graphic space previously used for two; and an artificially extended axis on a home-price graph, which bends a constant 15% annual growth rate into a curve that visually implies runaway acceleration — a distortion Levitin resolves by noting that steady percentage growth should be plotted on a logarithmic scale, where it shows up correctly as a straight line.

## Why It Matters

Once you know the specific repertoire of axis manipulations, you can check any chart in seconds — look at the axis labels, the starting value, and whether the scale is continuous — before accepting the visual impression it creates. This matters anywhere data gets summarized into a picture for a non-technical audience: news broadcasts, investor decks, dashboards, policy debates. The concept generalizes beyond graphs to any visual encoding of a quantity: the presentation format itself is a persuasive choice, separable from and sometimes contradicting the data it claims to represent.
