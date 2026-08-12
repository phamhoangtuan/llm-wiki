---
title: "Data Mesh"
type: concept
tags: [data-architecture, distributed-systems, domain-driven-design]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Data Mesh

A decentralized sociotechnical approach to data architecture that treats data as a product and aligns ownership with domain boundaries. Introduced by Zhamak Dehghani (co-author of *Software Architecture: The Hard Parts*).

## The Problem It Solves

Traditional centralized data platforms (data lakes, warehouses) create bottlenecks:

- Central data teams become overwhelmed
- Domain experts lose ownership of their data
- Data quality degrades as producers are disconnected from consumers

## Four Principles

1. **Domain Ownership**: Each domain owns and serves its own data
2. **Data as a Product**: Data is produced with the same quality standards as any product
3. **Self-Serve Data Platform**: Domain teams have tools to build and serve data products
4. **Federated Computational Governance**: Global standards enforced through automation, not central review

## Contrast with Traditional Architecture

| Traditional | Data Mesh |
| --- | --- |
| Centralized data lake | Distributed data products |
| One data pipeline team | Each domain owns its pipelines |
| Data is a byproduct | Data is a product |
| Manual governance | Automated fitness functions |

## Relationship to Domain-Driven Design

Data Mesh is DDD applied to data architecture: bounded contexts own their data, and data products cross context boundaries through well-defined contracts.

---

## Connections

- [[Domain-Driven Design]] — Bounded Contexts provide the organizational model for data ownership
- [[Data Product]] — The unit of delivery in a Data Mesh
- [[Architecture Fitness Functions]] — Governance mechanism for federated standards
- [[Data Sovereignty]] — Data ownership within domain boundaries
- [[Microservices]] — Service-aligned data ownership pattern
