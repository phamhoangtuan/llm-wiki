---
title: "Database Replication"
type: concept
tags: [databases, system-design, scalability, data-consistency]
created: 2026-05-24
updated: 2026-06-29
sources: [system-design-interview-xu, system-design-interview-volume-2, site-reliability-engineering, the-accidental-cto]
aliases: [master-slave-replication, read-replicas]
---

## Summary

Database replication is the process of copying data from a primary database (master) to one or more secondary databases (slaves/replicas). The master-slave pattern separates write operations from read operations, enabling horizontal scaling of read-heavy workloads.

## Master-Slave Architecture

| Component | Responsibility | Benefit |
| ----------- | -------------- | --------- |
| Master | Handles all writes (INSERT, UPDATE, DELETE) | Single source of truth for data consistency |
| Slave(s) | Receive data copies from master; handle reads | Scale reads horizontally; parallel processing |

## Failover Scenarios

| Failure | Response |
|---------|----------|
| Slave dies | Reads redirect to master or another healthy slave |
| Master dies | Promote a slave to master (may require data recovery if slave hasn't synced) |

## Trade-offs

| Challenge | Description |
| ----------- | ------------- |
| **Replication lag** | Slave may not be fully up-to-date with master — application must handle eventual consistency |
| **Write bottleneck** | All writes go to a single master — master capacity is the write ceiling |
| **Split-brain** | If master and promoted slave both accept writes, data diverges |

## Primary-Secondary Cluster (Read-Optimized)

For read-heavy workloads (read >> write), the Primary-Secondary pattern scales reads horizontally:

```
┌────────────────────────────────────────┐
│           Primary (Master)              │
│      Handles ALL writes (CRUD)          │
└────────────┬───────────────────────────┘
             │ (Replication)
             ▼
┌─────────┬─────────┬─────────┬─────────┐
│Secondary│Secondary│Secondary│Secondary│
│(Replica)│(Replica)│(Replica)│(Replica)│
│Reads    │Reads    │Reads    │Reads    │
└─────────┴─────────┴─────────┴─────────┘
```

**When replication delay is acceptable**: If data freshness can tolerate hours of lag (e.g., next-day SLA), replication simplifies significantly — nightly batch jobs handle the sync, avoiding real-time complexity.

**Read-your-own-writes**: When a user writes to the primary and immediately reads, temporarily route that user's reads to the primary or wait until the replica catches up. This prevents an otherwise correct eventually consistent system from showing the user their own update as missing.

> **Rule of thumb**: Start with a single database. Add replication when read load exceeds what one server can handle.

---

- Core to [[scalable-architecture]] — scales the data tier
- Related to [[cache-strategy]] — cache sits in front of replicated reads for further scaling
- Related to [[load-balancer]] — routes reads to available slaves
- Contrasts with [[database-sharding]] — replication copies data; sharding partitions data
- Related to [[database-isolation]] — isolation levels affect read consistency across replicas
- Core to [[proximity-service]] — Primary-Secondary clustering handles read-heavy geospatial queries
- Related to [[site-reliability-engineering]] — replication improves availability, but backups and independent validation provide recoverability
- Benchmark sources: [[sources/the-accidental-cto]] and [[sources/site-reliability-engineering]]
