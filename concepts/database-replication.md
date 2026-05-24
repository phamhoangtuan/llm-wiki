---
title: "Database Replication"
type: concept
tags: [databases, system-design, scalability, data-consistency]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [master-slave-replication, read-replicas]
---

## Summary

Database replication is the process of copying data from a primary database (master) to one or more secondary databases (slaves/replicas). The master-slave pattern separates write operations from read operations, enabling horizontal scaling of read-heavy workloads.

## Master-Slave Architecture

| Component | Responsibility | Benefit |
|-----------|--------------|---------|
| Master | Handles all writes (INSERT, UPDATE, DELETE) | Single source of truth for data consistency |
| Slave(s) | Receive data copies from master; handle reads | Scale reads horizontally; parallel processing |

## Failover Scenarios

| Failure | Response |
|---------|----------|
| Slave dies | Reads redirect to master or another healthy slave |
| Master dies | Promote a slave to master (may require data recovery if slave hasn't synced) |

## Trade-offs

| Challenge | Description |
|-----------|-------------|
| **Replication lag** | Slave may not be fully up-to-date with master — application must handle eventual consistency |
| **Write bottleneck** | All writes go to a single master — master capacity is the write ceiling |
| **Split-brain** | If master and promoted slave both accept writes, data diverges |

> **Rule of thumb**: Start with a single database. Add replication when read load exceeds what one server can handle.

---
- Core to [[scalable-architecture]] — scales the data tier
- Related to [[cache-strategy]] — cache sits in front of replicated reads for further scaling
- Related to [[load-balancer]] — routes reads to available slaves
- Contrasts with [[database-sharding]] — replication copies data; sharding partitions data