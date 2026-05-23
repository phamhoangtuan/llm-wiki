---
title: "Immutability of Essence"
type: concept
tags: [design-principles, immutability, domain-modeling]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [essential immutability, immutable essence]
---

## Summary

Essential attributes of a domain object should never change. If a change is needed, create a new object instead. This prevents ripple effects and preserves the integrity of the simulation.

## Fred Brooks' Two Complexities

| Type | Definition | Example | Can Eliminate? |
|---|---|---|---|
| **Essential** | Inherent complexity of the real problem | Physics of landing a rover on Mars | ❌ No — must manage |
| **Accidental** | Complexity from bad design/implementation | Mutable Date auto-correcting Nov 31 → Dec 1 | ✅ Yes — better design |

## Case Study: Mutable Date Object

```java
// ❌ Mutable Date: allows changing "essence"
LocalDate date = LocalDate.of(2024, 11, 31); // Invalid!
// Java "helps": auto-converts to Dec 1 → hides semantic error

// ✅ Immutable Date: Fail Fast
try {
    LocalDate date = LocalDate.of(2024, 11, 31); // Throws DateTimeException
} catch (DateTimeException e) {
    // Handle error immediately — don't let it propagate
}
```

## Key Rule

If you need to "change" an essential attribute, create a new object:

```java
// Instead of: order.setAmount(newAmount)
Order updatedOrder = order.withAmount(newAmount);  // Returns new Order
```

## Connections

- Protects [[bijection]] — mutable essence breaks the 1-1 mapping
- Enables [[rich-domain-model]] — rich objects manage their own state transitions
- Supports [[fail-fast]] — immutable objects fail fast on invalid construction
- Related to [[essential-accidental-complexity]] — immutability eliminates accidental complexity
