---
title: "Building Real-Time Analytics Systems"
type: source
source_type: book
author: "Mark Needham"
url: ""
source_date: ""
ingested: 2026-07-11
tags: [real-time-analytics, streaming, kafka, flink, clickhouse, architecture]
concepts: [real-time-analytics, batch-processing, lambda-architecture, kappa-architecture, change-data-capture, apache-kafka, stream-processing, apache-flink, apache-spark, clickhouse, apache-pinot, apache-druid, data-lakehouse, edge-computing]
---

# Building Real-Time Analytics Systems

**Author:** Mark Needham  
**Type:** Ebook (221 pages)  
**Finished:** 2026-04-26  
**Ingested:** 2026-07-11

---

## Core Thesis

Speed is no longer a competitive advantage — it is a survival requirement. Real-Time Analytics (RTA) eliminates the artificial time boundaries of batch processing to enable instantaneous decision-making.

## Real-Time Analytics Defined

RTA processes **unbounded data** — information that arrives continuously without end (IoT sensors, credit card transactions, clickstreams).

| Characteristic | Batch Processing (Traditional) | Real-Time Analytics (Modern) |
|----------------|-------------------------------|------------------------------|
| Time boundary | Artificial (e.g., once per day) | None — incremental processing on every event |
| Latency | High (hours/days) | Low (seconds/milliseconds) |
| Goal | Historical reporting | Instant decision-making |

## Four Core Business Benefits

1. **Faster Decision-Making** — Organizations that react quickly to events tend to become market leaders.
2. **New Revenue Streams** — Build data-powered products customers pay for (e.g., real-time user-facing dashboards).
3. **Reduced Infrastructure Costs** — Processing immediately avoids exponential cost growth from coupled storage and computation.
4. **Improved Customer Experience** — Proactively fix issues before customers report them.

## Modern Streaming Stack (5-Layer Architecture)

### 1. Event Producers

Detect state changes in source systems.

- **CDC (Change Data Capture):** Tools like Debezium capture database mutations.
- **Event Trackers:** Web/mobile behavior tracking (e.g., Snowplow).
- **SDKs:** Language-specific libraries to emit events.

### 2. Streaming Data Platform

The "source of truth" for event data — durably stored as append-only logs, partitioned for scalability.

- **Tools:** Apache Kafka, Amazon Kinesis

### 3. Stream Processing Layer

Transforms or enriches data while it flows. Can join or filter streams.

- **Limitation:** Tools like Kafka Streams struggle when serving thousands of concurrent analytical queries.
- **Tools:** Kafka Streams, Apache Flink, Spark Streaming

### 4. Serving Layer (Real-Time OLAP)

Serves queries with millisecond latency and high concurrency, optimized for multi-dimensional "slice and dice" analysis.

- **Tools:** Apache Pinot, Apache Druid, ClickHouse

> Processing layer "cooks" data; Serving layer "plates" it for fast user queries.

### 5. Frontend

User-facing interface for interacting with insights.

- Custom apps (React), Low-code (Streamlit), Visualization (Superset)

## Building & Scaling: Critical Factors

| Factor | Technical Consideration | Purpose |
|--------|------------------------|---------|
| **Data Partitioning** | Horizontally scale topics across brokers | Handle high throughput by splitting data |
| **Throughput (QPS)** | Calculate read/write queries per second | Determine required server cores |
| **Retention & Granularity** | Decide data lifetime (streaming vs serving) | Save space by rolling up old data |
| **Replication** | Maintain multiple copies (factor of 3 typical) | Ensure fault tolerance |

## Future Trends

1. **Edge Analytics** — Analyze data at the source to reduce network latency.
2. **Separation of Compute and Storage** — Scale compute and storage independently.
3. **Data Lakehouses** — Combine data lake flexibility with warehouse transactional integrity (e.g., Delta Lake).
4. **Streaming Databases** — Blur the line between stream processors and traditional databases for simpler architecture.

## Key Takeaways

1. Speed is king: RTA removes artificial time boundaries of batch processing.
2. Five-layer architecture: Event Producers → Streaming Platform → Processing → OLAP Serving → Frontend.
3. Don't confuse Processing and Serving: Kafka Streams for transformation, Pinot/Druid for fast queries.
4. Capacity planning is key: calculate QPS, partitioning, and retention before production.
5. Future is edge & lakehouse: the industry is shifting toward hybrid unified architectures.

---

- Foundation for [[real-time-analytics]] — processing unbounded data streams for instant decision-making
- Contrasts with [[batch-processing]] — traditional bounded, scheduled data processing
- Foundation for [[lambda-architecture]] — legacy dual-path batch + stream processing model
- Foundation for [[kappa-architecture]] — simplified streaming-first architecture
- Expands [[change-data-capture]] — capturing database changes as real-time event sources
- Expands [[apache-kafka]] — the persistent log streaming platform at the heart of RTA stacks
- Expands [[stream-processing]] — transforming and enriching data while it flows
- Expands [[apache-flink]] — advanced stream processing with exactly-once guarantees
- Expands [[apache-spark]] — micro-batch and continuous stream processing options
- Expands [[clickhouse]] — high-performance OLAP serving layer for real-time queries
- Foundation for [[apache-pinot]] — real-time OLAP datastore for low-latency analytics
- Foundation for [[apache-druid]] — column-oriented OLAP store for event-driven data
- Relates to [[data-lakehouse]] — the unified storage layer enabling modern streaming architectures
- Foundation for [[edge-computing]] — processing data at the network edge to reduce latency
