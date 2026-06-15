---
title: "Apache Kafka"
type: concept
tags: [streaming, messaging, kafka, data-engineering, event-driven]
created: 2026-05-26
updated: 2026-06-15
sources: [hugo-data-ingestion-platform-flink, databricks-zerobus]
---

## Summary

**Apache Kafka** is an open-source distributed event streaming platform used for high-throughput, low-latency data pipelines, streaming analytics, and event-driven architectures. Unlike traditional [[message-queue|message queues]], Kafka is a **distributed log** — messages are persisted, ordered, and replayable. Kafka is central to Grab's data platform as both a data source (Kafka topic ingestion) and historically as the intermediary in their CDC pipelines (now replaced by Flink CDC).

## Core Concepts

| Concept | Description |
|---|---|
| **Topic** | A named channel (category) to which records are published |
| **Partition** | Topics are split into partitions for parallelism; messages within a partition are strictly ordered |
| **Producer** | Application that publishes records to a Kafka topic |
| **Consumer** | Application that subscribes to topics and processes records |
| **Consumer Group** | Set of consumers that cooperatively consume from a topic; each partition is consumed by exactly one consumer in the group |
| **Broker** | A Kafka server; a cluster is a group of brokers |
| **Offset** | Unique sequential ID for each record within a partition; consumers track their position via offsets |
| **Retention** | Kafka retains messages for a configurable duration (hours to years), not just until consumed |

## Kafka vs Traditional Message Queues

| Aspect | Kafka | Traditional MQ (RabbitMQ, SQS) |
|---|---|---|
| Model | Distributed log | Queue |
| Message persistence | Long-term (retention-based) | Until consumed |
| Replay | Yes (reset offset) | No |
| Ordering | Within partition | Typically FIFO |
| Throughput | Millions of messages/sec | Thousands to tens of thousands |
| Consumer model | Pull-based | Push-based |
| Best for | Event streaming, data pipelines, CDC | Work distribution, RPC |

## In Data Ingestion Pipelines

### Kafka as Source (Hugo's Current Pattern)

```
Application → Kafka topic → Flink Consumer → S3 → Hive
```

Kafka serves as the ingestion source for application-generated events. Hugo's Flink pipelines consume from Kafka topics, resolve Protobuf schemas dynamically from Confluent Schema Registry, and write to the data lake.

### Kafka as CDC Intermediary (Hugo's Legacy Pattern)

```
MySQL binlog → Kafka Connect (Debezium) → Kafka topic → Consumer (Sprinkler) → S3
```

This was the previous architecture — Kafka acted as the buffer between the CDC connector and the S3 writer. Grab migrated away from this because it added operational complexity (more components to manage, coordinate, and debug). [[apache-flink|Flink CDC]] reads binlog directly, eliminating the Kafka hop.

## Schema Registry

**Confluent Schema Registry** is a critical companion to Kafka in data pipelines. It stores and versions schemas (Avro, Protobuf, JSON Schema) outside of Kafka topics:

- Producers register schemas before publishing
- Consumers fetch schemas at runtime by schema ID embedded in the message
- Enables **schema evolution** with compatibility checks (backward, forward, full)

In Hugo's Flink pipelines:
```
CI pipeline → updates Protobuf schema → Schema Registry → Flink fetches at startup
```
This eliminates the need for hardcoded DTOs (the legacy Sprinkler approach). Schema changes still require a manual Flink pipeline restart as of 2026-05.

## Kafka Connect (Legacy at Grab)

Kafka Connect is a framework for connecting Kafka with external systems via pre-built connectors (source and sink). It was used at Grab for MySQL CDC (Debezium connector) but was retired in favor of Flink CDC because:
- Added an extra component to manage and monitor
- Required users to configure jobs across multiple platforms (Kafka Connect + Hugo)
- Schema mapping between systems was manual and error-prone

## When to Use Kafka

| ✅ Use Kafka | ❌ Don't Use Kafka |
|---|---|
| High-throughput event streaming | Simple task queues (use RabbitMQ/SQS) |
| Data pipelines with replay needs | Request-response patterns (use REST/gRPC) |
| Event sourcing / CQRS | Small-scale messaging (overhead not worth it) |
| Decoupling microservices | Transient, fire-and-forget messages |
| Log aggregation, metrics | |
---
- Extends [[message-queue]] — Kafka is a specific distributed log implementation with persistence and replay
- Integrates with [[apache-flink]] — Flink is a first-class Kafka consumer/producer; replaces Kafka Connect
- Powers [[data-ingestion]] — Kafka is a primary source in Hugo's unified ingestion platform
- Related to [[change-data-capture]] — Kafka + Debezium was Grab's legacy CDC approach (now replaced by Flink CDC)
- Simplified by [[sources/databricks-zerobus]] — Databricks Zerobus is an API-based streaming alternative for Lake House use cases, removing Kafka's operational overhead
- Benchmark source: [[sources/hugo-data-ingestion-platform-flink]] — Grab's migration away from Kafka Connect toward Flink
