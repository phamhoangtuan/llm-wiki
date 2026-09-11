---
title: "Architectural Characteristics"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [software-architecture, non-functional-requirements, -ilities]
sources: [head-first-software-architecture, architecture-of-open-source-applications-vol2]
---

# Architectural Characteristics

The non-functional "-ilities" that a system must exhibit — the quality attributes that define how a system behaves, not what it does. They form one of the 4 dimensions of software architecture (alongside Decisions, Components, and Styles).

## Common Architectural Characteristics

| Characteristic | What It Means |
| --------------- | --------------- |
| **Scalability** | Handle growing workload without degrading |
| **Availability** | Remain operational and accessible |
| **Reliability** | Produce correct results consistently |
| **Performance** | Respond within acceptable time bounds |
| **Security** | Protect data and access from threats |
| **Maintainability** | Allow efficient modification and debugging |
| **Observability** | Expose internal state for monitoring |
| **Testability** | Enable efficient verification of correctness |
| **Deployability** | Release frequently and safely |

## Why They Matter

Architectural characteristics are the **first dimension** of the 4D puzzle. They drive architectural decisions: if scalability is critical, the style might shift from monolith to [[microservices]]; if security is paramount, authentication lives at the architecture level, not as an afterthought.

## Characteristics as Trade-offs

Every architectural characteristic comes at a cost:

- **Scalability ↑** → Complexity ↑ (distributed systems are harder)
- **Availability ↑** → Cost ↑ (redundant infrastructure)
- **Security ↑** → Usability ↓ (more authentication steps)
- **Performance ↑** → Maintainability ↓ (optimized code is harder to read)

This is the First Law of Architecture: **everything is a trade-off** (source: [[sources/head-first-software-architecture|Head First Software Architecture]]).

## Architecture vs. Design Boundary

Architectural characteristics that are hard to change and require significant trade-off analysis belong to architecture. Those easily adjusted belong to design.

---

- Part of [[risk-driven-architecture]] — characteristics drive which architectural risks to address
- Encoded in [[architectural-decision-records|ADRs]] — each ADR explains which characteristics were prioritized
- Manifests in [[microservices]] — a style chosen when scalability and deployability are top characteristics
- Complements [[observability]] — observability itself is an architectural characteristic
