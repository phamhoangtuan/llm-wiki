---
title: "TDD Methodology"
type: concept
tags: [tdd, testing, methodology, design, python, clean-code]
created: 2026-06-03
updated: 2026-06-03
sources: [tdd-python-percival]
---

## Summary

Test-Driven Development (TDD) is a software discipline where you **write a failing test before writing any application code**. The cycle — Red, Green, Refactor — drives design from the outside in, ensuring every line of code exists to satisfy a verified requirement. TDD is not primarily about testing; it's a **design methodology** that produces loosely coupled, testable code by default.

## The Testing Goat

> "Do nothing until you have a test."

The "Testing Goat" is a metaphor for stubborn discipline: no application code is written without a failing test demanding it. This isn't about tools — it's about engineering humility. We can't hold all the complexity in our heads, so tests become external memory that keeps us safe.

## The Red-Green-Refactor Cycle

The heartbeat of TDD:

| Phase | Action | Purpose |
|-------|--------|---------|
| **Red** 🔴 | Write a failing test | Define desired behavior before implementation |
| **Green** 🟢 | Write minimal code to pass | Satisfy the test — no more, no less |
| **Refactor** 🔵 | Clean up code, reduce duplication | Improve design without changing behavior |

Key rules:
- Write the **minimal code** to pass — resist the urge to over-engineer.
- Refactor is **mandatory**, not optional. The test safety net enables fearless cleanup.
- Each cycle should take **seconds to minutes** — fast feedback is essential.

## Outside-In TDD (Double Loop)

```
                ┌──────────────────────────┐
   Big Loop ───►│  Functional Test (fail)   │  ← User story perspective
                └──────────┬───────────────┘
                           │
                ┌──────────▼───────────────┐
   Small Loop ─►│  Unit Tests (R-G-R cycle) │  ← Code design perspective
                └──────────────────────────┘
```

1. Write a **functional test** describing a user story (fails because nothing exists).
2. To make it pass, drop into the **inner loop**: write unit tests to drive each piece of logic.
3. When unit tests are green, the functional test should pass — confirming the feature works from the user's perspective.

## YAGNI (You Ain't Gonna Need It)

- Build only what **today's tests** demand.
- Don't predict future requirements — speculative code adds complexity with zero current value.
- **Rule of Three Strikes**: if you write similar code 3 times before seeing a pattern, then refactor. Not before.

## Hacking vs Engineering

| Hacking (No Tests) | Engineering (TDD) |
|--------------------|-------------------|
| Fear of refactoring | Confidence — tests catch regressions |
| Code complexity grows unchecked | Decoupled, clean design |
| Manual verification, slow | Automated regression, fast |
| Productivity decreases as project grows | High velocity regardless of scale |

## Psychological Benefits

- **Psychological safety**: freely refactor, knowing tests will catch mistakes.
- **Flow state protection**: fast unit tests keep you in the zone; slow tests break focus ("Hot Lava" — developers avoid running them).
- **"Thanks, tests" moments**: when a test catches a regression you would never have predicted.

---
- Informs [[functional-testing]] — functional tests form the outer loop of Outside-In TDD
- Foundation for [[testing-strategy]] — TDD provides the methodology; testing strategy selects what to test
- Enabled by [[pytest-basics]] — pytest is the tool that makes the Red-Green-Refactor cycle fast in Python
- Benchmark source: [[sources/tdd-python-percival]] — Percival's hands-on TDD with Django and Selenium
- Related to [[fail-fast]] — both principles advocate catching problems at the earliest possible point
