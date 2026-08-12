---
title: "Data Sovereignty"
type: concept
tags: [software-architecture, data, microservices, distributed-systems]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Data Sovereignty

The principle that each service owns its data exclusively — it is the sole writer and the authority for its domain. A central concept in *Software Architecture: The Hard Parts*.

## The Shift

In monolithic architectures, a single database serves all concerns. After decomposition into services, data concerns move *within the service boundary*. Each service becomes the "system of record" for its domain.

## Core Rules

1. **Single Writer**: Only one service writes to a given data set
2. **API Access**: Other services read via the owning service's API, never directly from its database
3. **Shared Nothing**: No shared database tables between services

## Implications

- **Transactional integrity**: ACID transactions are limited to a single service's data
- **Cross-service operations**: Must use sagas or eventual consistency patterns
- **Data duplication**: Services may cache copies of other services' data for performance

## Distinction: Operational vs Analytical

- **Operational Data Sovereignty**: Services own their OLTP data
- **Analytical Data**: May be aggregated from multiple services via Data Mesh or centralized analytics

## Common Anti-Pattern

The **shared database** anti-pattern — multiple services reading/writing the same tables — undermines service independence. Schema changes in one service break others.

---

## Connections

- [[Architecture Quantum]] — The boundary within which data sovereignty applies
- [[Decomposition Patterns]] — How to achieve data sovereignty during monolith decomposition
- [[Data Mesh]] — Extends sovereignty to analytical data
- [[Microservices]] — Architecture pattern where data sovereignty is fundamental
- [[Saga Pattern]] — Managing transactions across sovereign data domains
