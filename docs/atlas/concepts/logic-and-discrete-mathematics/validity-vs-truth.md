---
type: Concept
title: Validity Is About Form, Not Truth
description: An inference can be logically correct in structure while its premises or conclusion are factually false, and vice versa — correctness and truth are independent axes.
book: logic-and-discrete-mathematics
chapters: [3]
tags: [logic, argumentation, formal-reasoning, fallacies]
created: 2026-07-12
---

# Validity Is About Form, Not Truth

## Definition

An inference rule is "logically sound if its conclusion follows logically from the
premises," and a specific inference is "logically correct if it is an instance of a
logically sound inference rule" — a purely structural property. Whether an inference is
correct is entirely separate from whether its premises or conclusion happen to be true in
the world. A correct inference guarantees a true conclusion only when all its premises are
actually true; a false premise can ride along a perfectly correct inference rule to a false
conclusion, and a true conclusion can come out of a structurally broken inference by
accident.

## In the Book

Section 3.2.2 builds this apart with paired examples. Modus Ponens ("p→q, p, therefore q")
is sound, so "Chantel is singing; if Chantel is singing then Chantel is happy; therefore
Chantel is happy" is logically correct. The book then gives the same-shaped but unsound
rule "p, q→p, therefore q" and shows the counterexample: "2 plus 2 equals 4; if 5 is
greater than 3 then 2 plus 2 equals 4; therefore 5 is greater than 3" is logically
incorrect despite every statement in it being true. It sharpens the point further with "5
divides 6; if 5 divides 6 then 5 divides 11; therefore 5 divides 11" — a logically correct
instance of Modus Ponens that reaches a false conclusion, because its first premise is
false. The book also shows the reverse trap: "Today is Monday; therefore tomorrow will be
Tuesday" reaches a true conclusion reliably, but not through logical form — it depends on
an unstated fact about how days of the week are ordered, and the underlying rule
("p, therefore q") is unsound.

## Why It Matters

This decouples two things people habitually fuse: whether an argument's reasoning is
structurally sound, and whether its content is factually correct. It gives a way to
criticize an argument on exactly one axis without conceding the other — you can say "your
logic is fine but your premise is false" or "your conclusion happens to be true but your
reasoning doesn't actually establish it," which is the difference between attacking an
argument's form and attacking its content. That separation transfers directly to debugging
(a program can run without crashing yet be wrong), to law (an argument can be procedurally
valid yet built on a false factual premise), and to everyday persuasion, where a
true-sounding conclusion is often used to smuggle past a broken inference.
