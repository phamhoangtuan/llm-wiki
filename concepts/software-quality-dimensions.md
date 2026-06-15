---
title: "Software Quality Dimensions"
type: concept
tags: [design-principles, architecture, engineering, optimization]
created: 2026-06-08
updated: 2026-06-15
sources: [seriously-good-software, practical-object-oriented-design]
aliases: [quality-spectrum, 2d-quality-model]
---

## Summary

Software quality is a multi-criteria optimization problem, not a binary toggle. Every line of code is a trade-off between competing dimensions. There is no "perfect" implementation in a vacuum — only code optimized correctly for a specific context: balancing machine performance against developer sanity.

## The 2D Quality Spectrum

Quality is measured across two independent axes:

### Axis 1: Internal vs External

| Dimension | Who Experiences It | Examples |
|---|---|---|
| **External** | End users interacting with the system | Correctness, Robustness, Efficiency (speed), Usability |
| **Internal** | Developers inspecting source code | Readability, Maintainability, Testability, Analyzability |

### Axis 2: Functional vs Non-functional

| Dimension | Question It Answers | Note |
|---|---|---|
| **Functional** | What does the software do? | All functional qualities are External by definition |
| **Non-functional** | How does the software do it? | Can be Internal (Readability) or External (Efficiency) |

> **Critical insight**: "Internal Functional" is an oxymoron. If software "does something" (functional), its effects are ultimately visible to users (external).

### The Trap

Focusing exclusively on "External Functional" (does it work?) while ignoring "Internal Non-functional" (is it maintainable?) accumulates technical debt that eventually harms users through slow bug fixes and fragile releases.

## The Four Core Trade-offs

| Trade-off | Description | Example |
|---|---|---|
| **Time vs Space** | Faster computation often uses more memory | Doubly linked list enables O(1) deletion but stores extra "previous" pointer |
| **Efficiency vs Readability** | Optimized code is often harder to understand | Using primitive types instead of objects saves RAM but becomes low-level and unmaintainable |
| **Robustness vs Efficiency** | Thorough input validation slows programs | Validating every input → CPU overhead. Skipping it → fast but crash-prone |
| **Development Time vs Quality** | Business wants speed, quality needs time | "Less haste, more speed" — doing it right the first time avoids costly rewrites |

## YAGNI: You Ain't Gonna Need It

Don't store data or add features "just in case." Every unnecessary field is technical debt from birth — it must be tested, documented, and maintained.

**Example**: If the spec doesn't require `disconnectFrom()` on water containers, don't store individual pipe connections. Over-engineering breeds subtle bugs.

> YAGNI is protection, not laziness.

## Analyzability: Beyond Readability

The ISO standard calls it **Analyzability** — the ability to analyze code for maintenance purposes.

- A professional doesn't name a group `g` if a mafia boss gave them 60 seconds to hack into a system
- Meaningful naming is rule #1 of analyzability
- Magic numbers are the enemy of analyzability

## The Hidden Cost of Abstractions (The 108-Byte Tax)

In a 64-bit JVM, a single container object using `HashSet` for grouping costs ~108 bytes:

| Component | Size |
|---|---|
| Object Header (GC, reflection) | 12 bytes |
| Data field (`double amount`) | 8 bytes |
| Reference to `Set` (compressed OOPs) | 4 bytes |
| `HashSet` instance overhead | 52 bytes |
| `HashMap$Node` entry | 32 bytes |
| **Total** | **108 bytes** |

> **Compressed OOPs caveat**: JVM uses 32-bit references on 64-bit machines to save RAM, but each address access requires a shift operation to map 32→64 bits. Saving bytes costs a small time penalty.

**Lesson**: Every abstraction has a tax. `HashSet`, objects, interfaces — all cost memory and performance. Calculate these costs when scaling to production.

## Programming to an Interface

Declare variables using the most abstract type that satisfies requirements:

```
// ✅ Professional: Program to interface
Set<Container> group = new HashSet<>();

// ❌ Novice: Lock into implementation
HashSet<Container> group = new HashSet<>();
```

This allows swapping implementations later without changing dependent code.

## Context is King

There is no "one best way" to write code — much like how the book *Exercises in Style* tells the same story 99 different ways. The best approach depends on project constraints:
- Need raw speed? Optimize for machine.
- Need maintainable code? Optimize for developer sanity.
- Need to scale to millions? Calculate memory footprints.

The architect's role: choose the right "style" for the context.

---

- Complementary to [[code-quality-pillars]] — dimensions (analytical framework) vs pillars (tactical checklist)
- Informs [[readability-vs-performance]] — the Efficiency/Readability trade-off is a core tension
- Related to [[essential-accidental-complexity]] — YAGNI prevents accidental complexity from over-engineering
- Embodied by [[immutability]] — immutable objects trade memory (new instances) for correctness and simplicity
- Related to [[fail-fast]] — choosing robustness over silent efficiency
- Enabled by [[dependency-injection]] — programming to interfaces enables context-appropriate implementations
- Related to [[rich-domain-model]] — rich objects encapsulate behavior that balances multiple quality dimensions
- Complements [[object-oriented-design]] — design as discovery embraces the context-driven, trade-off-aware philosophy of quality dimensions
- Benchmark source: [[sources/seriously-good-software]] — Marco Faella's 330-page guide
