---
title: "Snowflake ID"
type: concept
tags: [distributed-systems, databases, system-design, uuid]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [Twitter Snowflake, unique ID generation]
---

Snowflake is a distributed unique ID generation pattern created by Twitter. It produces 64-bit numeric IDs that are roughly time-ordered, efficient to store and index, and scalable without coordination.

## Design Requirements

- **64-bit numeric values**: Efficient storage (8 bytes) and B-tree indexing in databases
- **Roughly sorted by time**: Good for range queries and time-based partitioning
- **Highly scalable**: No central coordinator — each machine generates IDs independently

## 64-Bit Structure

```
[1 bit unused] [41 bits timestamp] [10 bits machine ID] [12 bits sequence]
```

- **41-bit timestamp**: Milliseconds since custom epoch (~69 years of IDs)
- **10-bit machine ID**: Supports 1,024 worker nodes
- **12-bit sequence number**: 4,096 IDs per millisecond per machine
- **1 reserved bit**: Always 0 (keeps IDs positive in signed 64-bit)

## Generation (Simplified)

```
def generate_id(machine_id, sequence):
    timestamp = current_time_millis()                    # 41 bits
    return (timestamp << 22) | (machine_id << 12) | sequence
```

The timestamp component ensures time-ordering at millisecond granularity. The sequence number handles multiple IDs within the same millisecond.

## Comparison with UUID

| Property | Snowflake | UUID v4 |
|----------|-----------|---------|
| Size | 8 bytes (64-bit) | 16 bytes (128-bit) |
| Sortability | Time-ordered (roughly) | Random |
| Index efficiency | Excellent (monotonic-ish) | Poor (random, causes B-tree fragmentation) |
| Central coordination | Machine ID assignment only | None |
| Human readability | Numeric | Hex string |

Snowflake IDs are preferred for primary keys in distributed databases where time-based range queries are common.

---
- Foundation for [[database-sharding]] — Snowflake IDs serve as natural shard keys with time locality
- Foundation for [[system-design-interview]] — "design a unique ID generator" is a classic interview question