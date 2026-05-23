---
title: "Fail Fast"
type: concept
tags: [design-principles, error-handling, reliability]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [fail fast principle, fail immediately]
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

```java
// ❌ Auto-corrects invalid data → hides the error
LocalDate date = LocalDate.of(2024, 11, 31); // Silently becomes Dec 1
```

## Correct: Fail Fast

```java
// ✅ Throws exception immediately
LocalDate date = LocalDate.of(2024, 11, 31); // DateTimeException
```

## Connections

- Enforced by [[immutability]] — immutable objects fail fast on invalid construction
- Prevents [[bijection]] violations — implicit transformations hide errors
- Related to [[rich-domain-model]] — rich objects validate their own state
- Related to [[essential-accidental-complexity]] — silent failures add accidental complexity
