---
title: "Information Hiding"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [software-design, complexity, abstraction, encapsulation]
sources: [code-complete]
---

# Information Hiding

A core design heuristic: hide implementation secrets (data structures, algorithms, internal state) behind stable interfaces so that changes don't cascade through the system.

## What to Hide

- **Data representation**: How data is stored internally (array vs. hash table vs. tree)
- **Algorithms**: Which algorithm implements a behavior (quicksort vs. mergesort)
- **Internal state**: Private fields that shouldn't be directly manipulated
- **Dependencies**: Which external systems or libraries are used

## Why It Matters

The primary goal is **localizing change**. When implementation details change, only the module that owns them needs modification — clients using the public interface remain untouched.

## Information Hiding vs. Related Concepts

| Concept | Relationship |
| --------- | ------------- |
| Encapsulation | The *mechanism* (private fields, access modifiers) that enables information hiding |
| Abstraction | The *result* — clients think at a higher level, ignoring hidden details |
| Loose Coupling | Information hiding *produces* loose coupling by minimizing surface area between modules |

## In Practice

- Design class interfaces around "what," not "how"
- Ask: "What secret am I hiding from the rest of the system?"
- Change-prone areas (business rules, hardware dependencies, data formats) are prime candidates for hiding
- Reveal as little as possible in interfaces — expose only what callers genuinely need

---

- Core principle of [[software-construction]] — the key heuristic for managing complexity
- Enabled by [[solid-principles|SOLID]] — Interface Segregation and Dependency Inversion are information hiding in practice
- Produces [[bijection|loose coupling]] — hiding details minimizes module surface area
- Foundation of [[architecture-hoisting]] — turning manual conventions into structural constraints
