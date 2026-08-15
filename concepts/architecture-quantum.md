---
title: "Architecture Quantum"
type: concept
tags: [software-architecture, distributed-systems, coupling]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Architecture Quantum

An independently deployable artifact with high functional cohesion, high static coupling, and synchronous dynamic coupling. The fundamental unit of analysis in modern distributed architecture, introduced in *Software Architecture: The Hard Parts*.

## Definition

An architecture quantum is characterized by three properties:

1. **High functional cohesion**: Components within the quantum serve a unified purpose
2. **High static coupling**: Tight wiring through shared dependencies, frameworks, and OS
3. **Synchronous dynamic coupling**: Components communicate synchronously at runtime to fulfill workflows

## Why It Matters

The quantum is the atomic unit of architectural decision-making. When you decompose a system, you are partitioning quanta. The boundaries between quanta define:

- Where data sovereignty lies
- Where transactions can be ACID vs eventual
- Where communication is synchronous vs asynchronous
- What can be deployed independently

## Relationship to Microservices

In microservices architecture, each service is typically one quantum — but the concept generalizes beyond services. A monolith may contain multiple logical quanta that *should* be separated but are structurally entangled.

## Trade-offs

- **Smaller quanta**: More deployment independence, but more network communication and eventual consistency
- **Larger quanta**: Easier transactional integrity, but less deployment flexibility

---

## Connections

- [[static-vs-dynamic-coupling]] — The two dimensions that define quantum boundaries
- [[microservices]] — Autopilot architecture where each service is a quantum
- [[decomposition-patterns]] — Patterns for identifying quantum boundaries in monoliths
- [[data-sovereignty]] — Data ownership moves inside quantum boundaries
