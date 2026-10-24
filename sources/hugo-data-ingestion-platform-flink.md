---
title: "The Hugo Evolution: Engineering Grab's Unified, One-Click Data Ingestion Platform with Apache Flink"
type: source
source_type: article
author: "Shuguang Xiang, Hung Nguyen, Hung Tran Viet, Shi Kai Ng"
url: "https://engineering.grab.com/one-click-data-ingestion-platform-with-apache-flink"
source_date: 2026-05-22
ingested: 2026-05-26
created: 2026-05-26
updated: 2026-06-15
tags: [data-ingestion, apache-flink, cdc, kafka, data-lake, grab, data-engineering]
concepts: [apache-flink, change-data-capture, data-ingestion, apache-kafka, apache-iceberg]
---

## Summary

Grab Engineering's "Hugo" platform evolved from a siloed, multi-platform [[data-ingestion|ingestion]] workflow into a unified self-service platform powered by **[[apache-flink|Apache Flink]]**. The new architecture retired two in-house components ([[apache-kafka|Kafka]] Connect and Sprinkler) and collapsed what was a days-long, multi-team onboarding process into a one-click, minutes-long experience.

## Architecture Evolution

### Before (Siloed)

For MySQL [[change-data-capture|CDC]] pipelines:
```
MySQL binlog → Kafka Connect → Kafka topics → Sprinkler (Go S3 writer) → Spark → Hive table
```
**4 disparate components**, each with separate configuration, monitoring, and operational semantics.

For Kafka ingestion:
```
Kafka topic → Sprinkler (Go, hardcoded DTOs) → S3 → Spark → Hive table
```
Manual Protobuf-to-Avro conversion via hardcoded Go structs; fragile schema evolution.

### After (Unified with Flink)

For MySQL CDC:
```
MySQL binlog → Flink CDC (direct read) → S3 → Spark compaction → Hive table
```
**2 core components**, single control plane. No Kafka hop. Automated schema detection.

For Kafka ingestion:
```
Kafka topic → Flink (dynamic Protobuf fetch from Schema Registry) → S3 → Spark compaction → Hive table
```
No hardcoded DTOs. Schema updates via CI pipeline → Schema Registry.

## Key Engineering Decisions

1. **Flink CDC connector** reads MySQL binlog directly — eliminates Kafka intermediary hop and associated schema risk
2. **Dynamic schema fetching** from Confluent Schema Registry at pipeline startup — no hardcoded Protobuf/Avro mappings
3. **Spark retained for compaction** — Flink handles streaming ingest; Spark handles small-file compaction into query-optimized Hive tables
4. **Validation guardrails** built into onboarding UI — catches missing prerequisites (binlog config, topic ownership, credential setup) before pipeline creation
5. **Checkpoint-based recovery** — Flink pipelines detect schema updates and resume from latest checkpoint (manual restart still required)

## Impact Metrics

| Metric | Before | After |
|---|---|---|
| MySQL CDC onboarding | Days (multi-team, tickets) | ~3 minutes (self-service) |
| Kafka pipeline onboarding | Days | ~6 minutes |
| Adoption | Baseline (5 years) | Last year alone exceeded previous 5 years combined |
| Cognitive load | Cross-system config translation | One-click, guided workflow |

## Key Takeaways for Data Platform Teams

- **Automation layer as "intelligent chassis"** — the custom automation wrapping Flink (validation, orchestration, lifecycle management) is what made self-service possible, not Flink alone
- **Retire, don't accumulate** — Hugo retired Kafka Connect and Sprinkler rather than adding Flink on top; reduced operational surface area
- **Schema handling is the hard part** — dynamic Protobuf resolution and CDC schema detection were the biggest engineering wins; schema evolution remains partially manual (restart required)
- **Early validation reduces drop-off** — front-loading prerequisite checks (binlog config, topic ownership, credential setup) prevents wasted onboarding attempts

## Future Direction

- **[[apache-iceberg|Apache Iceberg]]** as the data lake table format (improve SLA, reduce costs)
- **Zero-touch schema evolution** — auto-detect schema changes, validate compatibility, update tables without manual intervention

## Links

- [Grab Engineering blog](https://engineering.grab.com/)
- [Apache Flink](https://flink.apache.org/)
- [Flink CDC Connectors](https://ververica.github.io/flink-cdc-connectors/)

---

- Related to [[apache-flink]] — Flink CDC connector reads MySQL binlog directly, enabling 3-minute CDC onboarding
- Related to [[change-data-capture]] — CDC is the core ingestion pattern that Hugo platform automates
- Related to [[data-ingestion]] — Hugo is a unified, one-click data ingestion platform for Grab's data lake
- Related to [[apache-kafka]] — Kafka Connect and Sprinkler were retired in favor of Flink-native ingestion
- Related to [[apache-iceberg]] — planned as the future data lake table format for improved SLA and reduced costs
