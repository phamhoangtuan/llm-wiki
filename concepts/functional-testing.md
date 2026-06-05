---
title: "Functional Testing"
type: concept
tags: [testing, tdd, selenium, e2e, quality, python]
created: 2026-06-03
updated: 2026-06-03
sources: [tdd-python-percival]
---

## Summary

Functional tests (also called end-to-end or acceptance tests) verify that an application works from the **user's perspective**. They simulate real user interactions — clicking buttons, filling forms, seeing results — through a real browser or HTTP client. Unlike unit tests, which validate individual code units in isolation, functional tests confirm that all pieces integrate correctly to deliver business value.

## Functional Tests vs Unit Tests

| Aspect | Functional Tests | Unit Tests |
|--------|-----------------|------------|
| **Perspective** | User's view | Developer's view |
| **Purpose** | Verify app works correctly (delivers business value) | Verify code is clean and logically correct |
| **Tool** | Selenium (browser), HTTP client | unittest, pytest |
| **Speed** | Slow (seconds to minutes — renders UI, real network) | Fast (milliseconds) |
| **Scope** | Tests the whole stack | Tests a single unit (function, class) |
| **Role in TDD** | Outer loop: defines user story | Inner loop: drives detailed design |

## The Double Loop Pattern

Functional tests form the **outer loop** of Outside-In TDD:

1. Write a functional test that describes what the user should see and do.
2. The test fails (the feature doesn't exist yet).
3. Use **unit tests** (inner loop) to build each piece needed.
4. When unit tests pass, the functional test should also pass — confirming end-to-end correctness.

## What to Test (and What Not To)

**Test behavior, not constants:**

- ✅ Test: "User can add an item to a to-do list and see it appear."
- ❌ Test: "The heading text is exactly 'My To-Do List'."

Testing literal strings makes refactoring templates painful. Test **actions and outcomes**, not implementation details.

## Atomic Tests

Each functional test should verify **one user story or workflow**. When a functional test fails, you should immediately know what broke — not sift through a test that checks 15 different things.

## CI/CD Integration

- Run functional tests in CI on every commit.
- **Green build is sacred**: a failing functional test is treated as a site outage — fix before any new commits.
- Use **headless browsers** (Xvfb) in CI environments.
- Capture **screenshots on failure** — essential for debugging headless test failures.

## Speed Management

- Functional tests are inherently slower than unit tests.
- Don't let them become "Hot Lava" — tests so slow developers avoid running them.
- Keep the functional test suite under **a few minutes**; parallelize if needed.
- Fresh database state per test run — no side effects between tests.

---
- Driven by [[tdd-methodology]] — functional tests are the outer loop of Outside-In TDD
- Foundation for [[testing-strategy]] — functional tests are the 20-30% integration/E2E effort in the test pyramid
- Related to [[pytest-basics]] — pytest can drive functional tests via fixtures and Selenium integration
- Benchmark source: [[sources/tdd-python-percival]] — Percival's functional testing with Django and Selenium
