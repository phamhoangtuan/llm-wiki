---
title: "Apache Druid"
type: concept
tags: [olap, database, streaming, analytics, real-time]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [druid]
---

## Summary

**Apache Druid** is an open-source, column-oriented, distributed data store designed for high-performance real-time analytics on event-driven data. It is optimized for low-latency OLAP queries on streaming and batch data, making it a popular choice for the **serving layer** in [[real-time-analytics]] systems.

## Key Characteristics

- **Columnar storage** — data stored by column for efficient aggregation queries
- **Real-time ingestion** — can ingest streaming data directly from Kafka, Kinesis, etc.
- **Time-series optimized** — built around the concept of time-based segments
- **Sub-second queries** — pre-aggregated indexes enable millisecond response times
- **Horizontal scalability** — scales out by adding more nodes

## Druid vs Other OLAP Stores

| Aspect | Druid | [[clickhouse|ClickHouse]] | [[apache-pinot|Pinot]] |
|--------|-------|------------------------|-------------------|
| Data model | Event-oriented, time-series | General OLAP | Event-oriented, time-series |
| Ingestion | Native real-time streaming | Batch + streaming | Native real-time streaming |
| Query language | Druid SQL | ANSI SQL | Pinot SQL (ANSI-like) |
| Deployment | Cluster required | Single node or cluster | Cluster required |
| Best for | Streaming analytics, monitoring | General analytics, logs | User-facing analytics, metrics |

## When to Use Druid

- Real-time analytics dashboards (e.g., monitoring, A/B testing)
- Event-driven data (clickstreams, IoT, logs)
- Need sub-second query latency on TB-scale data
- Time-series aggregation is the primary query pattern

## Key Takeaways

1. Druid is purpose-built for real-time OLAP on streaming event data.
2. It sits in the serving layer of the modern streaming stack — between the stream processor and the frontend.
3. ClickHouse and Pinot are the primary alternatives; choose based on deployment simplicity and query patterns.

---

- Alternative to [[clickhouse]] — both serve the OLAP layer in RTA stacks
- Alternative to [[apache-pinot]] — similar event-oriented OLAP focus
- Serves [[real-time-analytics]] — Druid is a canonical OLAP serving layer choice
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham covers Druid as a serving layer option
