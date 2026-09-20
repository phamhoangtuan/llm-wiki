---
title: "Immutability of Essence"
type: concept
tags: [design-principles, immutability, domain-modeling, functional-programming]
created: 2026-05-23
updated: 2026-07-13
sources: [contieri-clean-code-cookbook, the-art-of-functional-programming]
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
- Implemented via [[python-standard-library]] — namedtuple provides immutable data structures in Python
- Core pillar of [[functional-programming]] — immutability is one of the 4 pillars of FP; pure functions require immutable data
- A form of [[architecture-hoisting]] — immutability is structural hoisting: the architecture guarantees no mutation, freeing developers from worrying about it
- Benchmark sources: [[sources/contieri-clean-code-cookbook]], [[sources/the-art-of-functional-programming]]
