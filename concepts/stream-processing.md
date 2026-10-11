---
title: "Stream Processing"
type: concept
tags: [streaming, data-engineering, real-time, architecture, event-driven]
created: 2026-07-11
updated: 2026-07-14
sources: [building-real-time-analytics-systems, stream-processing-apache-flink, streaming-systems]
aliases: [streaming, event-stream-processing]
---

## Summary

**Stream Processing** is the paradigm of computing on data as it flows — processing each event incrementally rather than waiting for a batch to accumulate. It is the engine layer of [[real-time-analytics]] systems, transforming raw event streams into structured, queryable, and actionable outputs (source: [[sources/streaming-systems]]).

> **Modern streaming is a strict superset of batch**, not a fast-but-approximate alternative. One streaming system can deliver both low-latency real-time results and correct, repeatable historical analysis.

## Streaming ⊃ Batch

Modern streaming engines (Flink, Beam) handle bounded datasets as a special case of unbounded streams. This eliminates the [[lambda-architecture|Lambda Architecture]] — no need for separate batch and speed layers. The [[kappa-architecture|Kappa Architecture]] runs everything on a single streaming engine.

| Aspect | Batch | Stream |
| -------- | ------- | -------- |
| Data scope | Finite, bounded dataset | Infinite, unbounded stream |
| Computation trigger | Schedule (time-based) | Event (data arrives) |
| Output latency | Hours/days | Seconds/milliseconds |
| Error recovery | Restart whole job | Checkpoint and resume from offset |
| State model | Stateless or external | Stateful (windows, sessions, joins) |

## The 4 Questions (Akidau's Model)

Every streaming pipeline must define answers to four fundamental questions (source: [[sources/streaming-systems]]):

| Question | Concept | What It Defines |
| ---------- | --------- | ----------------- |
| **What** results are calculated? | Transformations | Sums, histograms, ML models — the business logic |
| **Where** in event time? | [[windowing]] | Fixed, Sliding, or Session windows partition data in time |
| **When** in processing time? | Triggers & [[watermarks]] | When to emit results; how to measure input completeness |
| **How** do refinements relate? | Accumulation Modes | Discarding (replace), Accumulating (add), or Retractions (correct) |

## Core Capabilities

### Transformations

- **Map / Filter / FlatMap** — 1-to-1, selective, or 1-to-many record processing
- **KeyBy / GroupBy** — Partition stream by key for keyed aggregations
- **Windowed Aggregations** — Compute over time-based or count-based windows (tumbling, sliding, session)
- **Stream Joins** — Join two streams by key and time (e.g., ads viewed → purchases)

### State Management

Stream processing often requires "memory" of past events:

- **Keyed State** — Per-key state (e.g., running count per user)
- **Operator State** — Per-task state (e.g., Kafka partition offset)
- **Checkpoints** — Periodic snapshots for fault tolerance

### Time Semantics

| Time Type | Definition | Accuracy | Use Case |
| ----------- | ----------- | ---------- | ---------- |
| **Event Time** | When the event actually occurred | Deterministic | Correct results despite network delays |
| **Processing Time** | When the system processes the event | Fast but inaccurate | Low-latency approximations |
| **Ingestion Time** | When the event enters the streaming platform | Medium | Simple systems without out-of-order handling |

## Major Stream Processors

| Engine | Model | Strengths |
| -------- | ------- | ----------- |
| **Apache Flink** | True streaming | Exactly-once, event time, stateful, SQL |
| **Spark Streaming** | Micro-batch | Unified batch+stream API, mature ecosystem |
| **Kafka Streams** | Embedded | Runs inside app, no separate cluster needed |
| **ksqlDB** | SQL on Kafka | Declarative stream processing for Kafka-only |

## When to Use Stream Processing

- Event-driven architectures (fraud detection, IoT alerts)
- Real-time ETL (CDC → clean → warehouse)
- Continuous monitoring and anomaly detection
- Sessionization and behavioral analytics
- Stream-to-stream joins (ad impressions + conversions)

## Stream-Table Duality

Streams and tables are two representations of the same data. Aggregating a stream yields a table; observing changes to a table yields a stream ([[change-data-capture|CDC]]). This [[stream-table-duality|duality]] is the theoretical foundation that makes SQL-on-streams possible.

## Key Takeaways

1. Stream processing is the compute layer of real-time data systems.
2. Modern streaming is a **strict superset of batch** — one engine for both.
3. State management and time semantics are the two hardest problems in stream processing.
4. Event time processing is essential for correctness; [[watermarks]] are the mechanism.
5. [[stream-table-duality]] makes SQL-on-streams a natural fit, not a special case.

---

- Core to [[real-time-analytics]] — stream processing is the transformation engine of RTA
- Expands [[apache-flink]] — Flink is the reference implementation of modern stream processing
- Expands [[apache-kafka]] — Kafka provides the durable log that stream processors consume
- Related to [[change-data-capture]] — CDC streams are a primary input to stream processing pipelines
- Related to [[event-time-processing]] — correct time handling is a stream processing sub-discipline
- Related to [[stateful-stream-processing]] — state management distinguishes simple from advanced stream processing
- Related to [[message-delivery-semantics]] — exactly-once delivery underpins reliable stream processing
- Benchmark source: [[sources/stream-processing-apache-flink]] — Hueske's definitive guide to stream processing with Flink
- Depends on [[watermarks]] — the mechanism for tracking event-time progress
- Built on [[stream-table-duality]] — the theoretical foundation for stream processing correctness
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham's architecture guide covering the stream processing layer
- Benchmark source: [[sources/streaming-systems]] — Akidau's definitive theoretical framework for streaming
