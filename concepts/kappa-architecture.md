---
title: "Kappa Architecture"
type: concept
tags: [big-data, architecture, streaming, simplification, kafka]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [kappa]
---

## Summary

**Kappa Architecture** is a simplified data processing paradigm proposed by Jay Kreps (co-creator of Apache Kafka) that eliminates the batch layer entirely. All data is treated as a stream — even "batch" workloads are simply streaming jobs that read from the beginning of a log. This removes the code duplication and operational complexity of [[lambda-architecture]].

## Core Principle

> There is no batch layer. There is only a stream.

```
Raw Data → Streaming Platform (immutable log) → Stream Processor → Serving Layer → Query API
```

If you need to re-process historical data, you replay the log from the beginning through the same streaming job.

## How It Works

1. **All data enters as events** into an append-only log (e.g., Kafka)
2. **A single stream processor** (e.g., Flink, Kafka Streams) consumes the log
3. **To recompute history:** reset the consumer offset to the beginning of the log and re-run the same job
4. **No separate batch code path** — one codebase, one mental model

## Comparison with Lambda

| Aspect | Lambda | Kappa |
|--------|--------|-------|
| Code paths | 2 (batch + speed) | 1 (stream only) |
| Re-processing | Separate batch job | Replay log through same job |
| Operational load | High (maintain two systems) | Lower (one system) |
| Latency | Dual (slow batch + fast stream) | Unified (stream-native) |
| Requires mature streaming | No (batch compensates) | Yes (must handle late data, exactly-once) |

## Requirements for Kappa

Kappa only works when the streaming layer is sufficiently mature:

- **Exactly-once semantics** — no data loss or duplication on replay
- **Event time processing** — correctly handles out-of-order and late-arriving data
- **Durable, replayable log** — Kafka's retention must cover the full history window
- **Reprocessing scalability** — replaying months of data must finish in reasonable time

## When Kappa Fits

- Greenfield streaming systems with modern processors like [[apache-flink]]
- Organizations already using Kafka as their source of truth
- Workloads where batch and stream logic are identical (aggregations, filtering, joins)

## When Lambda Persists

- Legacy systems where the batch layer provides trusted, audited final results
- Organizations with immature streaming infrastructure
- Complex analytical workloads that streaming engines still struggle with (e.g., large-scale graph analytics)

## Key Takeaways

1. Kappa simplifies operations by unifying all processing into a single streaming path.
2. It requires a mature, replayable streaming platform and exactly-once semantics.
3. The concept is now mainstream — modern architectures rarely distinguish "batch" from "stream" at the infrastructure level.
4. [[apache-flink]] and [[apache-kafka]] together provide the technical foundation for Kappa architecture.

---

- Contrasts with [[lambda-architecture]] — Kappa removes the batch layer entirely
- Expands [[real-time-analytics]] — Kappa is the architectural philosophy behind modern RTA stacks
- Related to [[apache-kafka]] — Kafka's immutable, replayable log is the prerequisite for Kappa
- Related to [[apache-flink]] — Flink's exactly-once and event-time capabilities make Kappa viable in production
- Related to [[message-delivery-semantics]] — exactly-once delivery is a hard requirement for Kappa correctness
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham covers the Lambda-to-Kappa evolution
