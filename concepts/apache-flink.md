---
title: "Apache Flink"
type: concept
tags: [stream-processing, apache, flink, data-engineering, cdc]
created: 2026-05-26
updated: 2026-05-26
sources: [hugo-data-ingestion-platform-flink]
---

## Summary

**Apache Flink** is an open-source, distributed stream processing framework for stateful computations over data streams. It provides exactly-once semantics, low-latency processing, and a unified API for both streaming and batch workloads. Flink is the engine that powered Grab's Hugo platform migration, replacing Kafka Connect and Sprinkler for data ingestion into their data lake.

## Core Characteristics

- **Unified stream + batch** — one runtime for both streaming and batch; batch = bounded stream
- **Exactly-once state consistency** — checkpoints and savepoints guarantee no data loss or duplication even on failure
- **Low latency** — sub-second processing latency for real-time pipelines
- **Distributed** — scales horizontally across clusters
- **Rich connector ecosystem** — CDC connectors (MySQL, PostgreSQL, MongoDB), Kafka, S3, Hive, Iceberg, and more

## Key Primitives

| Primitive | Description |
|---|---|
| **DataStream API** | Low-level API for event-at-a-time processing; Java/Scala |
| **Table API / SQL** | Declarative relational API on top of streams |
| **State** | Flink manages application state (counts, windows, joins) in durable backends (RocksDB, heap) |
| **Checkpoints** | Periodic snapshots of state for failure recovery |
| **Savepoints** | Manually triggered snapshots for upgrades, migrations, debugging |

## CDC (Change Data Capture) with Flink

Flink CDC connectors read database transaction logs (e.g., MySQL binlog, PostgreSQL WAL) directly, capturing insert/update/delete events and streaming them to downstream sinks. This is a key use case:

```
MySQL binlog → Flink CDC connector → S3 / Hive / Kafka / Iceberg
```

Advantages of Flink CDC over Kafka Connect:
- **Fewer moving parts** — no intermediary Kafka broker/topic
- **Automated schema detection** — Flink infers schema from the source database
- **Single control plane** — pipeline lifecycle managed in one place
- **Exactly-once** — end-to-end guarantees from binlog to sink

→ See [[change-data-capture]] for the broader CDC pattern.

## Hugo Use Case (Grab)

In Grab's Hugo data ingestion platform, Flink replaced a fragmented architecture of 4 components (Kafka Connect → Kafka → Sprinkler → Spark) with 2 (Flink → Spark compaction):

1. **MySQL CDC**: Flink reads MySQL binlog directly, writes to S3, Spark compacts into Hive tables (~3 min onboarding)
2. **Kafka ingestion**: Flink fetches Protobuf schemas dynamically from Confluent Schema Registry, writes to S3, Spark compacts into Hive tables (~6 min onboarding)

## Comparison with Other Stream Processors

| Aspect | Flink | Spark Streaming | Kafka Streams |
|---|---|---|---|
| Processing model | True streaming (event-at-a-time) | Micro-batch | Event-at-a-time |
| Latency | Sub-second | Seconds (micro-batch) | Sub-second |
| State management | Built-in (RocksDB, checkpointing) | Stateful operations via DStream | Built-in (RocksDB) |
| SQL support | Table API + SQL (mature) | Structured Streaming SQL | KSQL / ksqlDB |
| Exactly-once | Yes (checkpoints + two-phase commit) | Yes (with idempotent sinks) | Yes (transactions) |
| Deployment complexity | High (JobManager + TaskManagers) | High (Spark cluster) | Low (embedded library) |

## When to Use Flink

| ✅ Use Flink | ❌ Don't Use Flink |
|---|---|
| Real-time CDC pipelines | Simple batch ETL (use Spark) |
| Low-latency streaming analytics | Lightweight stream processing (use Kafka Streams) |
| Stateful event processing (windows, joins) | Occasional data movement (use cron + script) |
| Large-scale, distributed streaming | Single-node processing (use embedded lib) |

## Ecosystem

- **Flink SQL** — ANSI SQL on streaming data with window functions, temporal joins
- **Flink CDC** — Connectors for MySQL, PostgreSQL, MongoDB, Oracle, TiDB
- **Ververica** — Commercial Flink platform (original creators)
- **Apache Iceberg** — Table format sink (future direction for Hugo)
- **Kubernetes** — Native K8s operator for Flink deployments
---
- Powers [[change-data-capture]] — Flink CDC is the primary production implementation of CDC at Grab
- Used in [[data-ingestion]] — Flink is the engine behind Hugo's unified ingestion platform
- Integrates with [[apache-kafka]] — Flink consumes and produces to Kafka topics; replaces Kafka Connect
- Related to [[apache-iceberg]] — Flink writes to Iceberg tables (Hugo's future direction)
- Benchmark source: [[hugo-data-ingestion-platform-flink]] — Grab's production migration from Kafka Connect+Sprinkler to Flink
