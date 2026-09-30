---
title: "Stream-Table Duality"
type: concept
tags: [streaming, data-modeling, kafka, tables, sql]
created: 2026-07-14
updated: 2026-07-14
sources: [streaming-systems]
aliases: [streams-and-tables, table-stream-duality]
---

## Summary

**Stream-Table Duality** is the principle that streams and tables are two sides of the same coin — every stream can be converted into a table, and every table can be converted into a stream. This is the foundational theory underlying modern [[stream-processing]] and the [[apache-kafka|Kafka]] ecosystem (source: [[sources/streaming-systems]]).

## The Two Abstractions

| | Stream | Table |
| --- | --- | --- |
| **Nature** | Data in motion (element-by-element) | Data at rest (holistic, bounded snapshot) |
| **Analogy** | A movie | A screenshot |
| **Operation** | Append-only log of events | Current state of each key |
| **Query** | Process each event as it arrives | Query the accumulated state |

## The Duality

### Stream → Table (Aggregation)

Applying an aggregation over a stream of updates yields a table:

```
Stream: INSERT user=1,action=click → INSERT user=1,action=buy → INSERT user=2,action=click
Table:  user=1: {click, buy}        →    user=2: {click}
```

This is `SELECT key, collect_list(event) FROM stream GROUP BY key`.

### Table → Stream (Change Data Capture)

Observing changes to a table over time yields a stream:

```
Table:  user=1,balance=100 → user=1,balance=150 (update)
Stream: UPDATE user=1,balance=100 → UPDATE user=1,balance=150
```

This is [[change-data-capture|CDC]] — the stream of row-level mutations.

## Practical Implications

| Implication | Example |
| ------------- | --------- |
| **Unified processing** | One system can handle both real-time and historical data |
| **Materialized views** | SQL queries on streams produce continuously updated tables |
| **Streaming SQL** | `SELECT ... FROM stream GROUP BY` is natural, not a special case |
| **Kafka's design** | Kafka topics are streams; compacted topics are tables; KTables in Kafka Streams are tables backed by compacted topics |

## Key Takeaways

1. Streams and tables are not competing paradigms — they are **dual** representations
2. The duality means streaming systems are a **strict superset** of batch (batch = bounded stream)
3. Understanding the duality is essential for designing correct streaming pipelines
4. SQL on streams is possible *because* of this duality — `GROUP BY` converts stream → table; any table can be replayed as a stream

---

- Foundation of [[stream-processing]] — the theoretical basis for stream-table unification
- Core to [[apache-kafka]] — Kafka's architecture (topics + compacted topics) embodies the duality
- Enables [[materialized-views]] — stream aggregation produces incrementally maintained views
- Related to [[change-data-capture]] — CDC is the practical mechanism for table → stream
- Benchmark source: [[sources/streaming-systems]] — Akidau's complete treatment of the duality
