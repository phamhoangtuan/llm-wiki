---
title: "Decomposition Patterns"
type: concept
tags: [software-architecture, refactoring, microservices, monolith]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Decomposition Patterns

Strategies for breaking a monolithic system into distributed services. From *Software Architecture: The Hard Parts*, Part I: "Pulling Things Apart."

## The Challenge

Decomposition is not just about code — it involves untangling shared databases, synchronous calls, and transactional boundaries. The "hard parts" are: service granularity, data ownership, and transaction management.

## Key Patterns

### Tactical Forking

For unstructured monoliths: replicate the entire codebase and prune away what's not needed. Quick to start, but leaves duplicated code to reconcile later.

### Component-Based Decomposition

For structured monoliths with clear component boundaries: extract identified components into standalone services. Requires existing modularity to be effective.

### Service Granularity

Too fine-grained → excessive network chatter and distributed transactions. Too coarse → monolith by another name. The "right" size is determined by architecture quantum boundaries.

## Data Decomposition

The hardest part of decomposition is separating data:

- **Database per Service**: Each service owns its schema
- **Shared Database Anti-Pattern**: Multiple services sharing tables → tight coupling
- **Data Sovereignty**: Each service is the sole writer to its data

## Decision Framework

When to decompose:

1. Differing architectural characteristics (scalability, availability needs)
2. Different rates of change
3. Organizational boundaries (Conway's Law)
4. Independent deployment requirements

---

## Connections

- [[architecture-quantum]] — The unit that guides decomposition boundaries
- [[microservices]] — Target architecture for decomposition
- [[static-vs-dynamic-coupling]] — What decomposition reduces (static) and increases (dynamic)
- [[data-sovereignty]] — Each service owns its data post-decomposition
- [[refactoring-at-scale]] — Safe restructuring of large codebases
