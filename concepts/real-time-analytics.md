---
title: "Real-Time Analytics"
type: concept
tags: [analytics, streaming, real-time, data-engineering, decision-making]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [rta, streaming-analytics, live-analytics]
---

## Summary

**Real-Time Analytics (RTA)** is the paradigm of processing and analyzing data as it arrives — continuously, without waiting for batch windows to close. Unlike traditional batch processing which operates on bounded datasets with artificial time boundaries (e.g., "run once per day"), RTA treats data as an unbounded stream where insights are generated incrementally with sub-second to sub-minute latency.

## Batch vs Real-Time

| Dimension | Batch Processing | Real-Time Analytics |
|-----------|---------------|---------------------|
| Data boundary | Bounded (finite dataset) | Unbounded (infinite stream) |
| Trigger | Scheduled (cron, clock time) | Event-driven (every record) |
| Latency | Hours to days | Seconds to milliseconds |
| Use case | Historical reporting, reconciliation | Operational decisions, alerting |
| Example | Daily sales summary | Fraud detection on each transaction |

## The Modern Streaming Stack

A production RTA system typically has five layers:

```
Event Producers → Streaming Platform → Stream Processor → OLAP Serving Layer → Frontend
```

| Layer | Role | Examples |
|-------|------|----------|
| **Event Producers** | Detect and emit state changes | CDC (Debezium), SDKs, IoT sensors |
| **Streaming Platform** | Durable, partitioned event log | Apache Kafka, Amazon Kinesis |
| **Stream Processor** | Transform, enrich, aggregate | Apache Flink, Kafka Streams, Spark Streaming |
| **OLAP Serving Layer** | Low-latency query serving | ClickHouse, Apache Pinot, Apache Druid |
| **Frontend** | Dashboards, alerts, apps | React, Streamlit, Superset |

## Business Value

1. **Faster decisions** — React to events before competitors; automated trading, dynamic pricing
2. **New revenue streams** — Sell real-time data products (e.g., live user-facing dashboards)
3. **Cost reduction** — Process incrementally avoids the storage/computation coupling explosion of massive batch jobs
4. **Customer experience** — Detect and fix issues before customers report them

## Scaling Considerations

| Factor | Key Decision |
|--------|-------------|
| **Partitioning** | Horizontally scale topics across brokers for throughput |
| **Throughput (QPS)** | Size compute based on read/write queries per second |
| **Retention** | Balance cost vs. history; roll up old data to coarser granularity |
| **Replication** | Factor of 3 is the gold standard for fault tolerance |

## Future Trends

- **Edge Analytics** — Process at the source to reduce network latency and bandwidth
- **Compute-Storage Separation** — Scale each dimension independently (cloud-native OLAP)
- **Streaming Databases** — Unified systems that blur the processor/database boundary (e.g., RisingWave, Materialize)

## Key Takeaways

1. RTA eliminates artificial time boundaries — process every event as it happens.
2. The five-layer stack (Producers → Platform → Processor → OLAP → Frontend) is the modern standard.
3. Do not confuse stream processing (transformation) with serving (querying) — use the right tool for each.
4. Capacity planning (QPS, partitioning, retention) must be done before production deployment.

---

- Contrasts with [[batch-processing]] — the traditional paradigm RTA replaces
- Foundation for [[lambda-architecture]] — the legacy dual-path approach combining batch and speed layers
- Foundation for [[kappa-architecture]] — the simplified streaming-first architecture
- Expands [[apache-kafka]] — Kafka is the persistent log backbone of most RTA stacks
- Expands [[apache-flink]] — Flink is the advanced stream processor for stateful RTA workloads
- Expands [[clickhouse]] — ClickHouse is a high-performance OLAP serving layer for real-time queries
- Related to [[data-lakehouse]] — lakehouses unify batch and streaming storage under one format
- Related to [[edge-computing]] — edge analytics pushes RTA closer to data sources
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Mark Needham's guide to RTA architecture
