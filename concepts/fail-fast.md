---
title: "Fail Fast"
type: concept
tags: [design-principles, error-handling, reliability, tdd]
created: 2026-05-23
updated: 2026-06-08
sources: [contieri-clean-code-cookbook, tdd-python-percival, good-code-bad-code]
---

## Summary

The system should stop execution immediately when an error is detected, rather than letting the error propagate silently. This makes debugging easier — the error occurs near its root cause.

## The Principle

> "The system should stop execution as soon as an error is detected, rather than letting the error continue to propagate."

## Benefits

- **Easier debugging**: Error occurs close to root cause
- **No silent corruption**: Errors don't manifest hours later in a batch job
- **Clear contracts**: Invalid input is rejected at the boundary

## Anti-pattern: Silent Failure

```
// ❌ Auto-corrects invalid data → hides the error
LocalDate date = LocalDate.of(2024, 11, 31); // Silently becomes Dec 1
```
## Correct: Fail Fast

```
// ✅ Throws exception immediately
LocalDate date = LocalDate.of(2024, 11, 31); // DateTimeException
```
---
- Enforced by [[immutability]] — immutable objects fail fast on invalid construction
- Prevents [[bijection]] violations — implicit transformations hide errors
- Related to [[rich-domain-model]] — rich objects validate their own state
- Related to [[essential-accidental-complexity]] — silent failures add accidental complexity
- Applied in [[harness-engineering]] — harnesses prevent AI agents from declaring victory before verification
- Embodied by [[tdd-methodology]] — write a failing test before code (Red phase) to fail fast on missing behavior
- Related to [[functional-testing]] — functional tests fail fast at the user level when integration breaks
- Embraced by [[code-quality-pillars]] — pillar 2 (no surprises) and pillar 3 (hard to misuse) both align with fail-fast philosophy
- Related to [[software-quality-dimensions]] — choosing robustness (fail fast) over silent efficiency is a deliberate trade-off
- Benchmark source: [[sources/contieri-clean-code-cookbook]] — Contieri's Clean Code Cookbook
