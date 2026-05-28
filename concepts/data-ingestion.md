---
title: "Data Ingestion"
type: concept
tags: [data-engineering, ingestion, etl, streaming, data-lake]
created: 2026-05-26
updated: 2026-05-28
sources: [hugo-data-ingestion-platform-flink, unlocking-dbt-design-deploy-transformations]
aliases: [data-onboarding, data-pipeline-onboarding]
---

## Summary

**Data ingestion** is the process of moving data from source systems (databases, message queues, APIs, files) into a centralized destination (data lake, warehouse, or streaming platform) where it can be processed, analyzed, and served. In modern data platforms, ingestion is increasingly expected to be **self-service, near-real-time, and low-code** — as exemplified by Grab's Hugo platform.

## Ingestion Patterns

### Batch Ingestion

Data is extracted on a schedule (hourly, daily), typically as full snapshots or incremental dumps.

| Characteristic | Typical Values |
|---|---|
| Latency | Hours to days |
| Source impact | Full table scans can load the source DB |
| Complexity | Low (simple scheduled jobs) |
| Example | `mysqldump` → S3 → Spark → Hive (Hugo's original design) |

### Streaming (Real-Time) Ingestion

Data is captured continuously as it changes, using CDC or event streams.

| Characteristic | Typical Values |
|---|---|
| Latency | Seconds to minutes |
| Source impact | Minimal (reads transaction log, not source tables) |
| Complexity | Higher (stateful pipelines, checkpointing, schema evolution) |
| Example | MySQL binlog → [[apache-flink|Flink CDC]] → S3 → Hive (Hugo's evolved design) |

→ See [[change-data-capture]] for CDC specifically.

## Platform Maturity Model

Data ingestion platforms evolve through stages:

| Stage | Hallmarks | Onboarding Time |
|---|---|---|
| **Stage 1: Manual** | Engineers write custom scripts per pipeline; no platform | Days to weeks |
| **Stage 2: Siloed** | Multiple platforms (Kafka Connect, custom apps, Spark); users coordinate across systems | Days (multi-team tickets) |
| **Stage 3: Unified** | Single self-service platform; one-click onboarding; automated schema handling | Minutes |

Grab's Hugo evolved from Stage 2 (Kafka Connect + Sprinkler + Spark) to Stage 3 (Flink + automation layer + Spark compaction).

## Key Design Dimensions

### 1. Self-Service vs Central Team

| Self-Service | Central Team |
|---|---|
| Source teams configure their own pipelines via UI/API | Data platform team writes and maintains all pipelines |
| Faster onboarding (minutes) | Higher quality control |
| Requires validation guardrails | Bottleneck on team bandwidth |
| Hugo approach: self-service with **early validation** | |

### 2. Schema Handling

The hardest part of ingestion is schema evolution:
- **Hardcoded DTOs** — brittle; every schema change requires code change (Hugo's legacy Sprinkler)
- **Schema registry** — schemas versioned in Confluent Schema Registry; pipelines fetch at runtime (Hugo's Flink approach)
- **Automated inference** — connector reads schema from source at runtime (Flink CDC)
- **Zero-touch** — auto-detect, validate compatibility, apply changes (Hugo's future goal)

### 3. Validation Guardrails

Hugo's onboarding UI validates prerequisites **before** pipeline creation, preventing wasted attempts:
- For Kafka: topic ownership verification, non-zero message volume, no duplicate table names
- For MySQL CDC: credential setup, binlog user config, binlog format (ROW required), binlog expiration settings

## Hugo's Architecture (Case Study)

Hugo unified two previously siloed ingestion patterns under one platform:

```
┌─────────────────────────────────────────────────┐
│                  Hugo Platform                     │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Kafka    │  │  MySQL   │  │  Validation   │  │
│  │  Source   │  │  CDC     │  │  Guardrails   │  │
│  └────┬─────┘  └────┬─────┘  └───────────────┘  │
│       │             │                             │
│  ┌────▼─────────────▼─────┐                      │
│  │      Apache Flink       │  (streaming engine)  │
│  └───────────┬────────────┘                      │
│              │                                    │
│  ┌───────────▼────────────┐                      │
│  │    S3 (object store)    │                      │
│  └───────────┬────────────┘                      │
│              │                                    │
│  ┌───────────▼────────────┐                      │
│  │  Spark Compaction       │  (small-file merge)  │
│  └───────────┬────────────┘                      │
│              │                                    │
│  ┌───────────▼────────────┐                      │
│  │  Hive Tables (queryable)│                      │
│  └────────────────────────┘                      │
└─────────────────────────────────────────────────┘
```

## Tooling Landscape

| Category | Tools |
|---|---|
| **Streaming engines** | [[apache-flink|Apache Flink]], Spark Streaming, Kafka Streams |
| **CDC connectors** | Flink CDC, Debezium (Kafka Connect), AWS DMS |
| **Transformation (T in [[elt|ELT]])** | [[dbt|dbt (data build tool)]], Apache Spark, Dataform |
| **Message queues** | [[apache-kafka|Apache Kafka]], Amazon Kinesis, Google Pub/Sub |
| **Schema registry** | Confluent Schema Registry, AWS Glue Schema Registry |
| **Table formats** | Hive, [[apache-iceberg|Apache Iceberg]], Delta Lake, Hudi |
---
- Powered by [[apache-flink]] — Flink is the streaming engine in Hugo's unified ingestion platform
- Implements [[change-data-capture]] — CDC is the primary pattern for database ingestion
- Integrates with [[apache-kafka]] — Kafka is both a source (topic ingestion) and was the legacy intermediary (replaced by direct CDC)
- Related to [[apache-iceberg]] — Iceberg is Hugo's future table format for improved SLA and cost
- Benchmark source: [[hugo-data-ingestion-platform-flink]] — Grab's platform evolution case study
- Related to [[elt]] — data ingestion provides the "EL" (Extract-Load); dbt handles the "T" (Transform)
- Feeds [[dbt]] — ingested raw data is the input for dbt's transformation models
