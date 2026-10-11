---
title: "Apache Pinot"
type: concept
tags: [olap, database, streaming, analytics, real-time, linkedin]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [pinot]
---

## Summary

**Apache Pinot** is an open-source, distributed OLAP datastore designed for low-latency, high-concurrency analytical queries on streaming and batch data. Originally built at LinkedIn to power real-time analytics at scale, Pinot is optimized for user-facing dashboards and metric monitoring where sub-second query response is required.

## Key Characteristics

- **Low-latency queries** — millisecond response even on billions of rows
- **High concurrency** — designed to serve thousands of simultaneous queries
- **Hybrid ingestion** — batch (Hadoop/S3) and real-time (Kafka/Kinesis) in the same table
- **Pluggable indexing** — sorted, inverted, star-tree, and bloom filter indexes
- **SQL interface** — Pinot SQL supports most ANSI SQL constructs

## Pinot vs Druid vs ClickHouse

| Aspect | Pinot | [[apache-druid|Druid]] | [[clickhouse|ClickHouse]] |
|--------|-------|----------------------|------------------------|
| Origin | LinkedIn | Metamarkets | Yandex |
| Focus | User-facing analytics | Streaming analytics | General OLAP |
| Multi-tenant | Built-in tenant isolation | Less emphasis | Via databases |
| Query latency | Sub-second | Sub-second | Sub-second to seconds |
| Best for | Product metrics, user dashboards | Monitoring, IoT | Ad-hoc analytics, logs |

## Architecture

Pinot uses a hybrid serving architecture:

- **Offline segments** — batch-processed historical data stored in deep storage (S3/HDFS)
- **Real-time segments** — streaming data consumed directly from Kafka, served from local disk
- **Broker** — Query router that distributes and aggregates queries across servers
- **Server** — Stores and serves segments; can be real-time or offline
- **Controller** — Manages cluster state, segment assignment, and ingestion

## When to Use Pinot

- User-facing analytics where every millisecond counts
- Need to unify batch historical data with real-time streams in one query
- Multi-tenant environments requiring query isolation
- LinkedIn-scale: thousands of concurrent users querying TBs of data

## Key Takeaways

1. Pinot is purpose-built for user-facing real-time analytics at LinkedIn scale.
2. Its hybrid offline+real-time architecture allows querying both historical and live data in a single SQL statement.
3. Druid and Pinot are the two primary event-oriented OLAP stores; ClickHouse is the more general-purpose alternative.

---

- Alternative to [[apache-druid]] — both are event-oriented OLAP stores from the Hadoop ecosystem
- Alternative to [[clickhouse]] — ClickHouse is more general-purpose; Pinot is tuned for user-facing dashboards
- Serves [[real-time-analytics]] — Pinot is a canonical serving layer in modern streaming stacks
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham covers Pinot as a serving layer option
