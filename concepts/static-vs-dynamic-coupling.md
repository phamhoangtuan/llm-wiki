---
title: "Static vs Dynamic Coupling"
type: concept
tags: [software-architecture, coupling, distributed-systems]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Static vs Dynamic Coupling

Two dimensions of coupling in distributed architectures, introduced in *Software Architecture: The Hard Parts*.

## Static Coupling

How architectural parts are **wired together** — the structural dependencies:

- **Code dependencies**: Import/require relationships between modules
- **Framework coupling**: Shared frameworks that force version alignment
- **Operating system coupling**: Platform-specific dependencies
- **Database coupling**: Multiple services sharing the same database schema

> Static coupling determines how hard it is to change one part without breaking others.

## Dynamic Coupling

How architectural parts **communicate at runtime** — the behavioral dependencies:

- **Communication**: Synchronous (request-response) vs asynchronous (events)
- **Consistency**: Atomic (ACID transactions) vs eventual consistency
- **Coordination**: Orchestration (central controller) vs choreography (decentralized events)

> Dynamic coupling determines the system's behavior under load and failure.

## The Trade-off

Decomposition inevitably reduces static coupling (independent codebases) but increases dynamic coupling (network communication). The architect's job is to find the right balance.

## Key Insight

*Pulling things apart* addresses static coupling. *Putting things back together* addresses dynamic coupling. Both are "the hard parts."

---

## Connections

- [[architecture-quantum]] — The unit that encapsulates static coupling within its boundary
- [[orchestration-vs-choreography]] — The coordination dimension of dynamic coupling
- [[microservices]] — Architecture that maximizes static decoupling
- [[saga-pattern]] — Managing dynamic coupling for distributed transactions
