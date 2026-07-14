---
type: Concept
title: Pattern Matching as a Decision Construct
description: Branch on the shape of data itself — destructuring and binding variables in the same step — instead of testing values with chained conditionals.
book: seven-languages-seven-weeks
chapters: [4, 5, 6]
tags: [pattern-matching, control-flow, destructuring, declarative, language-design]
created: 2026-07-12
---

# Pattern Matching as a Decision Construct

## Definition

Pattern matching lets a program simultaneously test whether a piece of data has a given shape and extract its component values into variables, replacing the two-step idiom of "check a condition, then manually pull out the fields you need." Tate lists it in the introduction as one of the fundamental "decision constructs" languages offer beyond ifs and whiles, alongside Prolog's unification. Erlang treats every `=` as a pattern match rather than a plain assignment — an assignment is just the special case where the left side is an unbound variable.

## In the Book

The book develops pattern matching cumulatively across three languages so each reinforces the last. Prolog (Chapter 4) establishes the root idea through unification: a query like `food_type(What, meat)` matches the variable `What` against every fact in the knowledge base and backtracks through each match that succeeds. Scala (Chapter 5) uses `match`/`case` for both simple value dispatch (a `factorial` function branching on `case x if x > 0`) and structural extraction from XML nodes. Erlang (Chapter 6) is where the mechanism is shown as central rather than incidental: `{person, {name, Name}, {profession, Profession}} = Person` matches the tuple shape and binds `Name` and `Profession` in one step, list matching like `[Head|Tail] = [1, 2, 3]` destructures head from tail, and `receive` clauses use pattern matching to decide which handler a given inbound message triggers — the same mechanism used for data extraction is also the actor model's message-dispatch mechanism. Tate is explicit about the lineage: "If you worked through the Prolog chapter, you got a pretty solid foundation of pattern matching," noting the one difference — Prolog matches against an entire database of facts, while Erlang and Scala match a single value at a time.

## Why It Matters

Pattern matching collapses type-checking, null-checking, and field extraction — three separate defensive steps in most C-family languages — into one construct that fails loudly and immediately if the shape doesn't fit, rather than letting a mismatch propagate silently as a null or a wrong-type value. It also unifies two things that usually look unrelated: parsing/validating incoming data and routing control flow, since both are really "what shape is this, and what should happen for each shape." Recognizing a chain of `if isinstance(x, ...)` or nested field-existence checks as a disguised pattern-match is often the fastest route to simplifying it.
