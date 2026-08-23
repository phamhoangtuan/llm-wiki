---
title: "Streaming Systems: The What, Where, When, and How of Large-Scale Data Processing"
type: source
source_type: book
author: "Tyler Akidau, Slava Chernyak, Reuven Lax"
url: "https://www.oreilly.com/"
source_date: 2018
ingested: 2026-07-14
tags: [streaming, data-engineering, real-time, apache-beam, apache-flink, watermarks]
concepts: [stream-processing, watermarks, stream-table-duality, event-time-processing, stateful-stream-processing, windowing]
---

## Summary

*Streaming Systems* is the definitive guide to modern stream processing, arguing that streaming is now a **strict superset of batch** — not a fast-but-approximate alternative. It provides the theoretical framework for processing infinite, out-of-order datasets with correctness, consistency, and repeatability.

## The 4-Question Model

Every pipeline must answer:

| Question | Concept |
| ---------- | --------- |
| **What** results are calculated? | Transformations (sums, histograms, ML models) |
| **Where** in event time? | Windowing (Fixed, Sliding, Session) |
| **When** in processing time? | Triggers & Watermarks |
| **How** do refinements relate? | Accumulation Modes (Discarding, Accumulating, Retractions) |

## Two Domains of Time

| Domain | Meaning |
|--------|---------|
| **Event Time** | When the event actually occurred — the Truth |
| **Processing Time** | When the system observed the event — the Observation |

> The challenge: Event Time ≠ Processing Time. Watermarks track event-time progress so the system knows when it's safe to close a window despite late arrivals.

## Streams & Tables Duality

- **Streams** → Tables: Aggregating updates yields a table (e.g., running count)
- **Tables** → Streams: Observing changes yields a stream (e.g., Change Data Capture)

Think of a stream as a movie and a table as a screenshot — you can derive either from the other.

## Historical Evolution

| Era | Technology | Contribution |
| ----- | ------------ | -------------- |
| Early | MapReduce/Hadoop | Scalability, simplicity (batch-only) |
| Gen 1 | Storm | Low-latency (at-least-once) |
| Gen 2 | Spark Streaming | Correctness via micro-batching |
| Gen 3 | MillWheel/Flink | Native streaming + watermarks, distributed snapshots |
| Storage | Kafka | Stream/Table duality, durable replayable transport |
| Unified | Apache Beam | Portability: one model for batch & streaming |

## Correctness Guarantees

- **Exactly-once processing**: No dropped or duplicated records during failures
- **Strong consistency**: Reliable state across distributed nodes
- **Watermarks**: Critical tool for reasoning about time and completeness
