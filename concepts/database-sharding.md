---
title: "Database Sharding"
type: concept
tags: [system-design, databases, scalability, partitioning]
created: 2026-05-28
updated: 2026-05-28
sources: [system-design-interview-xu]
aliases: [sharding]
---

## Summary

**Database sharding** is a horizontal partitioning technique that splits a large database into smaller, independent "shards," each holding a subset of the data. Unlike [[database-replication|replication]] (which copies the same data to multiple servers), sharding distributes different data across servers — enabling write scalability beyond what a single database instance can handle.

## Sharding vs Replication

| Aspect | Replication | Sharding |
|---|---|---|
| **Data distribution** | Same data on every replica | Different data on each shard |
| **Write scaling** | ❌ All writes hit master | ✅ Writes distributed across shards |
| **Read scaling** | ✅ Reads from replicas | ✅ Reads from specific shards |
| **Complexity** | Moderate (read/write split) | High (cross-shard queries, rebalancing) |

## Sharding Strategies

| Strategy | How It Works | Example |
|---|---|---|
| **Key-based / Hash** | Hash the shard key → mod by shard count | `hash(user_id) % 4` |
| **Range-based** | Partition by key range | Users A–M on shard 1, N–Z on shard 2 |
| **Directory-based** | Lookup table maps keys → shards | External service routes queries |

## Key Challenges

- **Cross-shard joins** — data on different shards can't be joined with standard SQL
- **Resharding** — adding/removing shards requires data redistribution
- **Hotspots** — celebrity users can overload a single shard
- **Analytical queries** — aggregations across all shards require scatter-gather patterns

## When to Shard

| ✅ Shard | ❌ Don't Shard |
|---|---|
| Write throughput exceeds single DB | Read-heavy workloads (use replication + cache) |
| Data volume too large for one instance | Still growing — wait until necessary |
| Multi-tenancy with natural tenant isolation | Simple apps that don't need scale |
---
- Contrasts with [[database-replication]] — replication copies data; sharding partitions data
- Related to [[scalable-architecture]] — sharding is a horizontal scaling technique for databases
- Related to [[cache-strategy]] — caching reduces read load; sharding handles write load
- Benchmark source: [[sources/system-design-interview-xu]] — Alex Xu's system design guide
