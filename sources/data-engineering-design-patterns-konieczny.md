---
title: "Data Engineering Design Patterns"
type: source
source_type: book
author: "Bartosz Konieczny"
url: ""
source_date: 2025-10-12
ingested: 2026-08-24
tags: [data-engineering, design-patterns, ingestion, error-handling, idempotency, data-quality, observability]
concepts: [data-ingestion, change-data-capture, fail-fast, data-quality-monitoring, data-observability, data-governance, data-engineering-fundamentals]
---

## Summary

Bartosz Konieczny's 150-page guide catalogs reusable data engineering patterns organized into 8 categories. The key principle: a great data platform isn't one giant pipeline — it's a collection of reusable, reliable patterns. Every pattern has trade-offs: simplicity vs flexibility, performance vs correctness, automation vs visibility.

## The 8 Pattern Categories

### 1. Ingestion Patterns

| Pattern | Description | Trade-off |
| --- | --- | --- |
| **Full Loader** | Copy everything each time | Simple but expensive for large data |
| **Incremental Loading** | Pull only new/changed data | Saves compute; must handle late arrivals |
| **Change Data Capture (CDC)** | Stream every insert/update/delete in real-time | Powerful but needs ordering guarantees |
| **Passthrough Replicator** | Copy data as-is for backup | Minimal effort; consumers handle cleaning |
| **Transformation Replicator** | Apply cleaning/enrichment during ingestion | Saves downstream time; adds complexity |
| **Compactor** | Merge small files into optimized ones | Essential for data lakes; needs scheduled compute |
| **Readiness Marker** | Producer writes "done" flag; consumers wait | Prevents partial reads; requires coordination |
| **External Triggers** | Pipelines start on file/event arrival | Saves cost; must handle noisy triggers |

### 2. Error Management Patterns

| Pattern | Description |
| --- | --- |
| **Dead-Letter Queue (DLQ)** | Isolate broken records; pipeline continues |
| **Fail-Fast** | Stop immediately on any error |
| **Retry** | Reattempt with exponential backoff |
| **Quarantine** | Move suspicious records to holding zone |
| **Alerting** | Notify engineers via Slack/email/monitoring |
| **Sampling & Monitoring** | Track health via subsets and summary metrics |

### 3. Idempotency Patterns

| Pattern | Description |
| --- | --- |
| **Output Check** | Verify what's already written before overwriting |
| **Checksum/Hash Comparison** | Compare file hashes to skip redundant processing |
| **Versioned Writes** | Create new versions instead of overwriting |
| **Upsert (Merge)** | Insert new rows, update existing in place |

### 4. Data Value Patterns

| Pattern | Description |
| --- | --- |
| **Join Enrichment** | Combine main data with lookup/reference datasets |
| **Aggregation** | Compute totals, counts, averages for reporting |
| **Deduplication** | Remove duplicates using a reliable key |

### 5. Data Flow Patterns

| Pattern | Description |
| --- | --- |
| **Fan-out** | Send same dataset to multiple consumers |
| **Fan-in** | Merge data from many sources into one destination |
| **Backpressure Handling** | Slow producers or buffer messages to prevent overload |

### 6. Data Security Patterns

| Pattern | Description |
| --- | --- |
| **Encryption** | At rest and in transit; key management is the challenge |
| **Masking/Tokenization** | Replace sensitive fields with safe placeholders |
| **Access Control & Least Privilege** | Give each service only the access it needs |

### 7. Data Quality Patterns

| Pattern | Description |
| --- | --- |
| **Validation Rules** | Check nulls, invalid types, out-of-range values |
| **Schema Enforcement** | Ensure datasets match defined structure |
| **Data Expectations & Automated Tests** | Continuous checks — unit tests for data |

### 8. Observability Patterns

| Pattern | Description |
| --- | --- |
| **Metrics Collection** | Row counts, processing times, error rates |
| **Logging** | Structured, searchable logs tracing data flow |
| **Data Lineage** | Show origin, transformations, and destination of each dataset |

## Design Decision Order

1. How does data arrive? → Ingestion pattern
2. What can fail? → Error handling and retries
3. Can this job rerun safely? → Idempotency
4. How to make data useful? → Transformation and value patterns
5. Who consumes it? → Flow and access
6. Is it secure and high-quality? → Security and validation
7. How will we monitor it? → Observability and alerts

---

- Related to [[data-ingestion]] — 8 ingestion patterns extend the existing batch/streaming framework
- Related to [[change-data-capture]] — CDC is one of the core ingestion patterns
- Related to [[fail-fast]] — Fail-Fast is one of the error management patterns
- Related to [[data-quality-monitoring]] — Quality patterns (validation, schema enforcement, expectations) complement monitoring
- Related to [[data-observability]] — Observability patterns (metrics, logging, lineage) are the DE-specific implementation
- Related to [[data-governance]] — Security patterns (encryption, masking, access control) enforce governance
- Related to [[data-engineering-fundamentals]] — the pattern catalog is a practical toolkit for the enduring DE skillset
- Benchmark source: [[sources/fundamentals-of-data-engineering]] — Reis & Housley's lifecycle framework
- Benchmark source: [[sources/big-book-data-engineering]] — Databricks' 3-pillar framework
