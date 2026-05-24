---
title: "Immutability of Essence"
type: concept
tags: [design-principles, immutability, domain-modeling]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
---

## Summary

Essential attributes of a domain object should never change. If a change is needed, create a new object instead. This prevents ripple effects and preserves the integrity of the simulation.

## Fred Brooks' Two Complexities

| Type | Definition | Example | Can Eliminate? |
| --- | --- | --- | --- |
| **Essential** | Inherent complexity of the real problem | Physics of landing a rover on Mars | ❌ No — must manage |
| **Accidental** | Complexity from bad design/implementation | Mutable Date auto-correcting Nov 31 → Dec 1 | ✅ Yes — better design |
---
- Protects [[bijection]] — mutable essence breaks the 1-1 mapping
- Supports [[fail-fast]] — immutable objects fail fast on invalid construction
- Related to [[essential-accidental-complexity]] — immutability eliminates accidental complexity
