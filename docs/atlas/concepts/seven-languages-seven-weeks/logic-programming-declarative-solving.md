---
type: Concept
title: Logic Programming as Declarative Constraint Solving
description: State facts and rules about a world and let an inference engine search for values that satisfy them, instead of coding the search yourself.
book: seven-languages-seven-weeks
chapters: [4]
tags: [declarative, logic-programming, constraint-solving, search, prolog]
created: 2026-07-12
---

# Logic Programming as Declarative Constraint Solving

## Definition

Prolog programs consist of facts (direct assertions about the world), rules (inferences built from facts), and queries (questions posed against the resulting knowledge base). The programmer never writes a search algorithm; Prolog's unification engine automatically tries combinations of values until it finds ones that make a query true, or exhausts the possibilities and reports failure. Tate summarizes the shift bluntly: "With Prolog, you don't have to know how. The computer does the reasoning for you."

## In the Book

The book builds this up from a minimal knowledge base: `likes(wallace, cheese).`, `likes(grommit, cheese).`, `likes(wendolene, sheep).`, and a rule `friend(X,Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).` Querying `friend(wallace, grommit)` returns yes because Prolog searches for some Z that both wallace and grommit like (cheese) and confirms X ≠ Y — the programmer specified the *relationship*, not the search procedure. Tate then shows the more powerful case of leaving a variable unbound in the query itself: asking `food_type(What, meat)` against a small facts table returns each matching food (`spam`, then `sausage`) one at a time as Prolog backtracks through the knowledge base looking for alternate bindings that satisfy the goal. The chapter's headline demonstration — flagged in the introduction as one of the book's three deep-dive projects — is solving a full Sudoku puzzle in under twenty lines of Prolog, which Tate calls "an eye-opening experience," precisely because the programmer states the constraints of a valid Sudoku (rows, columns, and boxes contain 1–9 once each) and never writes a solving algorithm.

## Why It Matters

Separating "what must be true" from "how to search for it" turns an entire class of problems — scheduling, configuration, puzzle-solving, constraint satisfaction — into a specification exercise instead of an algorithm-design exercise, often collapsing what would be dozens of lines of nested loops and backtracking logic into a handful of declarative rules. The same shift shows up wherever a system separates rule statement from rule execution: SQL queries versus hand-written joins, spreadsheet formulas versus procedural recalculation, or business-rule engines versus if/else chains buried in application code. Recognizing "this is a constraint-satisfaction problem, not a step-by-step procedure" is often the harder insight than actually writing the Prolog.
