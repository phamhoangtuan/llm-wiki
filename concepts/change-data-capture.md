---
title: "Change Data Capture (CDC)"
type: concept
tags: [data-engineering, cdc, streaming, databases, data-lake]
created: 2026-05-26
updated: 2026-05-26
sources: [hugo-data-ingestion-platform-flink]
aliases: [CDC]
---

## Summary

**Change Data Capture (CDC)** is a data integration pattern that captures row-level changes (inserts, updates, deletes) from a source database's transaction log and streams them to downstream systems in near real-time. Unlike batch ETL, which periodically snapshots the entire table, CDC propagates only the deltas — enabling low-latency, efficient data synchronization.

## How It Works

```
Source DB → Transaction Log → CDC Connector → Target System
              (binlog/WAL)      (reads log)     (data lake, cache, search index)
```

| Step | Description |
|---|---|
| 1. Transaction committed | Database writes change to its transaction log (MySQL binlog, PostgreSQL WAL) |
| 2. CDC connector reads log | Connector tails the log, parses row-level events |
| 3. Events streamed downstream | Each change becomes an event with before/after state |
| 4. Target applies changes | Sink applies inserts/updates/deletes to the target (data lake, cache, search index) |

## Key Concepts

### Transaction Logs

| Database | Log Mechanism | Format |
|---|---|---|
| MySQL | Binary log (binlog) | Row-based / statement-based / mixed |
| PostgreSQL | Write-Ahead Log (WAL) | Logical decoding |
| MongoDB | Oplog | BSON documents |
| Oracle | Redo log | LogMiner / XStream |

### Event Types

Each captured change carries a payload:
- **INSERT** → `{"op": "c", "after": {...}}`
- **UPDATE** → `{"op": "u", "before": {...}, "after": {...}}`
- **DELETE** → `{"op": "d", "before": {...}}`

### Schema Handling

CDC connectors must handle schema evolution:
- **Automated detection** — connector infers current schema from the database (used by Flink CDC at Grab)
- **Schema registry** — store schemas in a registry (Confluent Schema Registry); connector references by version
- **Manual DTO mapping** — brittle; requires code changes on schema update (legacy Sprinkler approach at Grab)

## Benefits

| Benefit | Description |
|---|---|
| **Low latency** | Changes propagate in seconds, not hours (batch) |
| **Minimal source impact** | Reading the transaction log doesn't add query load to the source DB |
| **Full fidelity** | Captures deletes and intermediate states that batch snapshots miss |
| **Exactly-once semantics** | When paired with checkpointing (Flink), ensures no duplicates or data loss |

## Implementations

### Flink CDC

Grab's Hugo platform uses Flink CDC connectors to read MySQL binlog directly → S3 → Hive. Key advantages:
- **No Kafka intermediary** — Flink reads binlog directly, eliminating Kafka Connect + Kafka broker + topics
- **Automated schema detection** — no manual DTO mapping
- **Exactly-once** — Flink checkpoints provide end-to-end guarantees
- **3-minute onboarding** — down from days with the previous Kafka Connect pipeline

→ See [[apache-flink]] for Flink details.

### Kafka Connect (Debezium)

The previous generation (and still widely used):
```
MySQL binlog → Debezium connector (Kafka Connect) → Kafka topic → Consumer
```
More moving parts but battle-tested. Grab migrated away from this.

### Other CDC Tools

| Tool | Approach | Best For |
|---|---|---|
| **Debezium** (Kafka Connect) | Kafka-native CDC | Kafka-centric ecosystems |
| **Flink CDC** | Stream processing engine | Low-latency, stateful pipelines |
| **AWS DMS** | Managed service | AWS ecosystems |
| **Airbyte** | Open-source ELT | SaaS/API sources |
| **Fivetran** | Managed SaaS | Hands-off CDC |
| **pglogical** | PostgreSQL-native | Pg-to-pg replication |

## Common Challenges

| Challenge | Mitigation |
|---|---|
| **Schema evolution** | Automated schema detection (Flink); schema registry with compatibility checks |
| **Initial snapshot** | Full table scan on first run; then switch to incremental CDC |
| **Binlog retention** | Configure sufficient binlog retention to survive connector downtime |
| **DDL changes** (ALTER TABLE) | Some connectors pause on DDL; require manual intervention |
| **Large transactions** | Batch large events to avoid overwhelming downstream sinks |
---
- Powered by [[apache-flink]] — Flink CDC connector is the production implementation at Grab
- Core to [[data-ingestion]] — CDC is one of the two primary ingestion patterns (alongside Kafka)
- Related to [[apache-kafka]] — Kafka + Debezium is the legacy CDC approach that Flink CDC replaces
- Related to [[materialized-views]] — CDC is a common mechanism to feed [[incremental-view-maintenance]]
- Benchmark source: [[hugo-data-ingestion-platform-flink]] — Grab's migration from Kafka Connect CDC to Flink CDC
