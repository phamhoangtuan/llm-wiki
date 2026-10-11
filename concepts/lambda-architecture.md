---
title: "Lambda Architecture"
type: concept
tags: [big-data, architecture, batch, streaming, historical]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [lambda]
---

## Summary

**Lambda Architecture** is a big data processing paradigm that maintains two parallel data paths — a **batch layer** for comprehensive, accurate historical processing and a **speed layer** for real-time, approximate stream processing. Results from both paths are merged in a **serving layer** to provide a unified query interface.

## The Three Layers

```
         ┌─────────────────┐
         │   Serving Layer │ ← Merges batch views + real-time views
         │   (Query API)   │
         └────────┬────────┘
                  │
    ┌─────────────┴─────────────┐
    │                           │
    ▼                           ▼
┌──────────┐              ┌──────────┐
│  Batch   │              │  Speed   │
│  Layer   │              │  Layer   │
│(accurate,│              │(approx., │
│ complete)│             │  fast)   │
└────┬─────┘              └────┬─────┘
     │                         │
     ▼                         ▼
┌──────────┐              ┌──────────┐
│ Raw Data │              │ Raw Data │
│ (immutable│             │ (stream) │
│  master) │              │          │
└──────────┘              └──────────┘
```

### Batch Layer

- Processes the full dataset (all historical data)
- Emits pre-computed views (e.g., daily aggregations)
- High latency (hours) but **100% accurate and complete**
- Tools: Hadoop MapReduce, Apache Spark

### Speed Layer

- Processes only recent data (the delta since last batch run)
- Compensates for batch latency with **approximate, real-time views**
- Lower latency (seconds) but may use estimation or partial data
- Tools: Apache Storm, Apache Flink, Spark Streaming

### Serving Layer

- Stores and indexes both batch and speed views
- Queries merge results: batch view (complete but stale) + speed view (fresh but incomplete)
- Tools: Apache Druid, Elasticsearch, HBase

## Why Lambda Emerged

In the early 2010s, stream processing frameworks were immature — they couldn't guarantee accuracy or handle late-arriving data reliably. Lambda was a pragmatic compromise:

> "We'll do the best we can in real time, but trust the batch layer for the final answer."

## Criticisms & Decline

| Problem | Cause |
|---------|-------|
| **Code duplication** | Same business logic must be implemented twice (batch + stream) |
| **Operational complexity** | Two separate pipelines to maintain, monitor, and debug |
| **Merge complexity** | Serving layer must reconcile potentially divergent batch and speed views |
| **Delayed corrections** | If the speed layer is wrong, corrections only arrive with the next batch run |

Modern stream processors like [[apache-flink]] can now achieve both accuracy and low latency in a single path, making Lambda largely obsolete for new systems.

## Key Takeaways

1. Lambda was a pragmatic solution for an era when stream processing couldn't be trusted for accuracy.
2. It requires writing and maintaining the same logic twice — a heavy operational burden.
3. Modern streaming frameworks (Flink, Kafka Streams) have made Lambda architecture unnecessary for most use cases.
4. Legacy Lambda systems are gradually being migrated to [[kappa-architecture]] or unified streaming pipelines.

---

- Contrasts with [[kappa-architecture]] — the simplified single-path streaming alternative
- Contrasts with [[real-time-analytics]] — modern RTA typically uses unified streaming, not dual paths
- Related to [[apache-spark]] — Spark powers the batch layer; Spark Streaming historically powered the speed layer
- Related to [[apache-flink]] — Flink's exactly-once guarantees eliminated the need for a separate batch reconciliation path
- Related to [[data-lakehouse]] — lakehouses provide unified storage that reduces the need for separate batch/speed storage
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham discusses the evolution away from Lambda
