---
title: "Data Storage and Operations"
type: concept
tags: [data-management, storage, infrastructure, dama]
created: 2026-07-14
updated: 2026-07-14
sources: [dama-dmbok-2nd-edition]
---

# Data Storage and Operations

Implementation and support of stored data assets throughout their lifecycle. One of DAMA's eleven Knowledge Areas.

## Scope

Data Storage and Operations covers the physical and logical management of data:

- **Database administration**: Installation, configuration, patching, backup, recovery
- **Storage technologies**: RDBMS, NoSQL, object storage, file systems
- **Performance tuning**: Indexing, partitioning, query optimization
- **Capacity planning**: Growth forecasting and resource provisioning
- **Disaster recovery**: High availability, failover, replication strategies

## Role in the DAMA Framework

Part of the **Enable & Maintain** lifecycle phase. This KA is the operational backbone — it executes the plans designed by Data Architecture and Data Modeling, governed by Data Governance policies.

## Position in Aiken's Pyramid

A Phase 1 foundational discipline. Without reliable storage and operational discipline, no higher-level data practice can function.

## Relationship to Other KAs

- **Data Architecture** defines *what* storage structures should exist
- **Data Security** specifies *how* access is controlled
- **Data Modeling** determines *what shape* data should take
- **Data Lifecycle** governs *when* data is archived or destroyed

---

## Connections

- [[database-replication]] — Master-slave and Primary-Secondary patterns
- [[database-sharding]] — Horizontal partitioning for write scalability
- [[containerization]] — Docker and the container-vs-VM abstraction
- [[data-lifecycle]] — Generation through destruction stages
- [[cloud-service-models]] — IaaS, PaaS, SaaS for storage infrastructure
