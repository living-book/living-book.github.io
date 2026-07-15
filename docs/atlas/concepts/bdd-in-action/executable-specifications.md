---
type: Concept
title: Executable Specifications
description: "Automated tests expressed in business language that serve as both acceptance criteria and living documentation."
book: bdd-in-action
chapters: [1, 5, 6]
tags: [automation, testing, documentation, acceptance-criteria]
created: 2026-07-15
---

# Executable Specifications

## Definition

An executable specification is an automated test that illustrates and verifies how the application delivers a specific business requirement. It uses concrete examples from requirements, written in a structured format like Gherkin that both business stakeholders and developers can understand, and gets executed as code to validate the system behavior. Unlike traditional test cases written after code is complete, executable specifications guide development and stay synchronized with implementation through their failure when code drifts.

## In the Book

Smart explains executable specifications as the core mechanism for bridging the gap between business requirements and code. In chapter 1, he illustrates this with a money-transfer scenario: "Scenario: Transferring money to a savings account / Given my Current account has a balance of 1000.00 / And my Savings account has a balance of 2000.00 / When I transfer 500.00 from my Current account to my Savings account / Then I should have 500.00 in my Current account / And I should have 2500.00 in my Savings account." 

This example becomes an executable specification by matching each step to test code. When JBehave or Cucumber executes the scenario, it extracts variables (like $amount and $accountType) from the step text and runs the corresponding application code. The key difference from traditional tests is that "requirements and executable specifications are the same thing; when the requirements change, the executable specifications are updated directly in a single place" (1675-1676). They run as part of the build process and generate reports that show both test results and readable documentation of what the system does.

## Why It Matters

Executable specifications eliminate the multiple translations that destroy information fidelity in traditional development. Instead of business analyst writing requirements in English, developer translating to code, and tester translating requirements into test cases (three opportunities for misunderstanding), everyone works from the same executable artifact. Because the specification is code, it cannot drift from reality—a failing test immediately reveals misalignment. This means teams have a continuously accurate, always-up-to-date reference for how the system actually works, and developers can make changes confidently knowing what they've broken because the tests fail before the change reaches production. The dual role—both acceptance criterion and documentation—eliminates the dead-weight of maintaining a separate requirements document.
