---
title: "Định lý CAP (CAP Theorem) — Data Engineering Handbook"
type: source
source_type: article
author: "Data Engineering Handbook (kythuatdulieu.github.io)"
url: "https://kythuatdulieu.github.io/concepts/1-distributed-systems-architecture/cap-theorem/"
source_date: 2026-06-16
ingested: 2026-06-17
tags: [distributed-systems, cap-theorem, consistency, availability, partition-tolerance, architecture]
concepts: [cap-theorem]
---

## Summary

A comprehensive exploration of the CAP Theorem from the Vietnamese Data Engineering Handbook, covering Brewer's 2000 conjecture and Gilbert & Lynch's 2002 proof. The article distinguishes CAP Consistency from ACID Consistency, maps CP and AP architectures to real database systems (MongoDB, Cassandra, HBase, DynamoDB), explains Quorum mechanics for split-brain resolution, introduces PACELC as CAP's extension, and provides practical architecture decision-making guidance for Data Engineers.

## Core Message

> In any distributed data system, you can guarantee at most two of three properties: Consistency (all nodes see the same data), Availability (every request gets a non-error response), and Partition Tolerance (system survives network splits). Since Partition Tolerance is mandatory in any real network, the true trade-off is CP vs AP.

## Key Takeaways

1. **CAP defined**: Consistency (all nodes return latest write), Availability (every request gets a response), Partition Tolerance (system operates through network breaks) — pick two
2. **P is mandatory**: Network partitions are inevitable in cloud/on-premise infrastructure; the real choice is CP (sacrifice availability for consistency) vs AP (sacrifice strong consistency for availability)
3. **CAP-C ≠ ACID-C**: ACID Consistency = data integrity (constraints, foreign keys); CAP Consistency = node synchronization (all replicas show identical state). A system can be ACID-compliant but CAP-inconsistent (e.g., async master-slave replication)
4. **CP systems** (HBase, MongoDB, Zookeeper, CockroachDB): Reject reads/writes during partitions to prevent stale data; used in financial ledgers, metadata stores, reconciliation
5. **AP systems** (Cassandra, DynamoDB, CouchDB): Continue serving reads/writes on live nodes, resolve conflicts later via eventual consistency; used in user-facing apps, CDNs, shopping carts
6. **Quorum mechanics**: `R + W > N` ensures strong consistency; `R + W ≤ N` allows eventual consistency with higher availability. Configurable per-operation in systems like Cassandra
7. **PACELC extension**: If Partition → trade Availability vs Consistency; Else (normal operation) → trade Latency vs Consistency. Modern systems often choose PC/EC (Cassandra) or PC/EL (DynamoDB)
8. **Split-brain resolution**: Quorum-based voting (`N/2 + 1`) prevents two partitions from both claiming to be the primary; Zookeeper uses this for leader election

## Companion Concept

→ [[cap-theorem]]
