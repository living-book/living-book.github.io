---
type: Concept
title: "Given-When-Then: Scenario Structure"
description: "A standard template for expressing examples and acceptance criteria using three clauses that describe precondition, action, and expected outcome."
book: bdd-in-action
chapters: [1, 5]
tags: [scenario-language, gherkin, structure, communication]
created: 2026-07-15
---

# Given-When-Then: Scenario Structure

## Definition

Given-When-Then is a template for structuring concrete examples into scenarios that can be executed as tests and understood by both technical and non-technical readers. A Given clause establishes the preconditions and initial state, the When clause describes the action or event under test, and the Then clause specifies the expected outcomes. This structure makes examples unambiguous enough to automate while remaining readable as English prose, bridging the gap between natural language and executable code.

## In the Book

Smart explains the Given-When-Then structure in chapter 5 as part of the Gherkin format used by BDD tools. He provides the direct definition: "The natural order of a scenario is Given ... When ... Then: Given describes the preconditions for the scenario and prepares the test environment. When describes the action under test. Then describes the expected outcomes" (1549-1553). He illustrates with a money-transfer example: "Given my Current account has a balance of 1000.00 / And my Savings account has a balance of 2000.00 / When I transfer 500.00 from my Current account to my Savings account / Then I should have 500.00 in my Current account / And I should have 2500.00 in my Savings account" (1528-1532). The And and But keywords allow multiple steps within each clause to be chained together readably. Smart emphasizes that "Each scenario is made up of a number of steps, where each step starts with one of a small number of keywords" (1547-1548), and tools like Cucumber and JBehave use pattern matching to map each step text to corresponding test code.

## Why It Matters

Given-When-Then provides a universal vocabulary for expressing requirements that avoids the ambiguity of prose while remaining accessible to people without coding skill. Because the structure is predictable, tools can reliably parse and automate it. Because the language is English (not pseudocode or formal notation), business stakeholders can write, read, and refine scenarios directly without a translation layer. The structure also enforces clear thinking—the discipline of separating precondition, action, and outcome surfaces underspecified assumptions and hidden edge cases that prose requirements hide.
