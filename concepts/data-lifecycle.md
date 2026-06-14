---
title: "Data Lifecycle"
type: concept
tags: [data-engineering, data-lifecycle, governance, infrastructure]
created: 2026-06-14
updated: 2026-06-14
sources: [data-lifecycle-handbook, data-engineering-handbook]
aliases: [data-lifecycle-management, dlm]
---

## Summary

The **Data Lifecycle** is the sequence of stages data traverses from initial creation to final destruction. It is a core pillar of [[data-governance|Data Governance]] that ensures data is treated as a managed asset — not an infinite landfill. Effective Data Lifecycle Management (DLM) automates the movement of data through six stages, applying appropriate storage classes, retention policies, and access controls at each phase to optimize cost, ensure regulatory compliance, and reduce security risk.

Without lifecycle management, organizations suffer from data hoarding — keeping everything forever in expensive high-performance storage, turning data lakes into "data swamps" that drain budgets and expose the business to unnecessary legal liability.

## The Six Stages

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ 1. GEN   │──▶│ 2. STORE │──▶│ 3. PROC  │──▶│ 4. USE   │──▶│ 5. ARCH  │──▶│ 6. DEST  │
│ eration  │   │          │   │ essing   │   │ /Analyt. │   │ ival     │   │ ruction  │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
      💡             📦             ⚙️             📊             🧊             🗑️
```

| Stage | Description | Examples |
|---|---|---|
| **1. Generation** | Data originates from user actions, IoT devices, APIs, or partner feeds | User clicks on web app, sensor readings, API responses |
| **2. Storage** | Data lands in databases, object stores, or data lakes | S3 buckets, Postgres, Kafka, raw Data Lake |
| **3. Processing** | Cleaning, validation, ETL/ELT, normalization into queryable structures | Spark jobs, dbt models, deduplication |
| **4. Usage / Analytics** | Highest-value stage — BI dashboards, ad-hoc queries, ML model training | Looker reports, Data Scientist notebooks, building features |
| **5. Archival** | Data is rarely accessed; moved to cold-tier storage | AWS Glacier, infrequent-access storage classes |
| **6. Destruction** | Permanent deletion across ALL storage media including backups | GDPR right-to-be-forgotten purges, retention-expired deletion |

## Hot Data vs Cold Data

The lifecycle is fundamentally about managing the **temperature** of data — automatically migrating it from expensive, high-performance storage to cheap, low-access storage as it ages.

| Dimension | Hot Data | Cold Data |
|---|---|---|
| **Age** | Recent (minutes to weeks) | Old (months to years) |
| **Access frequency** | Constant reads/writes | Rarely or never accessed |
| **Storage medium** | SSD, in-memory cache, high-I/O DB | HDD, tape, object storage cold tiers |
| **Cost** | Expensive per GB | Cheap per GB (up to 90% less) |
| **Latency** | Sub-millisecond to seconds | Minutes to hours (retrieval penalties) |
| **Examples** | Today's transactions, active shopping cart, real-time dashboards | 3-year-old invoices, historical logs, archived compliance records |
| **Cloud service** | S3 Standard, BigQuery active storage | S3 Glacier Deep Archive, BigQuery long-term storage |

> **In essence**: Lifecycle management is the automated process of moving data from Hot → Warm → Cold → Deleted as it ages and becomes less valuable.

## Why Manage the Data Lifecycle?

### 1. Cost Optimization

An application error log from today is critical for debugging; the same log from 5 years ago is worthless. Lifecycle rules move aged data from expensive SSD storage to cheap archival tiers, often cutting storage costs by **50–90%**.

### 2. Regulatory Compliance (GDPR)

The GDPR "Right to be Forgotten" mandates that organizations must delete ALL personal data when a user requests it — across production databases, data warehouses, data lakes, AND backup copies. Without managed lifecycle policies, ensuring complete deletion across all systems is nearly impossible.

### 3. Security Attack Surface Reduction

Stale data that is no longer useful but still sitting in the system becomes a target for attackers. Scheduled destruction of expired data reduces the organization's attack surface — less data to steal, fewer compliance violations to expose.

## Automation & Lifecycle Rules

Manual lifecycle management does not scale. Cloud platforms provide declarative rules that automatically transition or expire data:

### AWS S3 Lifecycle Policy (JSON)

```json
{
    "Rules": [
        {
            "ID": "LogLifecycleRule",
            "Filter": { "Prefix": "app-logs/" },
            "Status": "Enabled",
            "Transitions": [
                {
                    "Days": 30,
                    "StorageClass": "STANDARD_IA"
                },
                {
                    "Days": 90,
                    "StorageClass": "GLACIER"
                }
            ],
            "Expiration": {
                "Days": 365
            }
        }
    ]
}
```

**What this does**: Objects under `app-logs/` automatically transition to cheaper storage at 30 and 90 days, then expire completely at 365 days.

### Other Cloud Automation Examples

| Platform | Feature | How It Works |
|---|---|---|
| **Google BigQuery** | `partition_expiration_days` | Set expiration on time-partitioned tables (e.g., 90 days); old partitions are auto-deleted |
| **Snowflake** | Time Travel + Fail-safe | Retention window for recovering data; combine with scheduled SQL tasks for archival/deletion |
| **GCP Cloud Storage** | Object Lifecycle Management | Similar to S3 — transition rules with conditions on age, storage class |
| **Azure Blob Storage** | Lifecycle Management Policies | Define rules to move blobs to cooler tiers or delete after configurable periods |

## Best Practices

1. **Classify data at the source**: Tag data as PII, sensitive, or regular immediately upon ingestion. Sensitive data gets stricter, shorter retention policies.
2. **Full automation, zero manual intervention**: Use cloud-native lifecycle rules — humans forget, miss edge cases, or skip steps. Rules are deterministic.
3. **Encrypt archived data**: Cold storage may be rarely accessed but must still be end-to-end encrypted with strict access controls to prevent silent data leaks.
4. **Define retention policies cross-functionally**: Involve legal, business, and engineering teams to agree on how long each data class must be kept — then encode those policies as automated rules.
5. **Test deletion completeness**: When a retention policy triggers, verify that data is gone from ALL copies — production, replicas, backups, and disaster-recovery sites.

## Common Pitfalls

1. **Data hoarding**: "Keep it all — might need it someday" transforms Data Lakes into Data Swamps. Storage costs balloon, query performance degrades, and finding useful data becomes harder.
2. **Forgetting backups during deletion**: The #1 GDPR compliance trap. Engineers delete data from the primary database but overlook backup snapshots, DR replicas, and log archives. This still constitutes a legal violation.
3. **Storage class confusion**: Failing to understand retrieval costs and latency of cold storage classes. Data moved to Glacier is cheap to store but expensive and slow (hours) to retrieve — a bad fit for data that may need ad-hoc re-analysis.

## Interview Insights

### Q1: Distinguish Hot Data from Cold Data in the Data Lifecycle

**Hot Data**: Recently created, accessed and updated continuously. Demands high I/O throughput (SSD, cache, primary DB). Expensive to store. Example: current shopping cart contents, today's transactions.

**Cold Data**: Old, rarely touched. Speed is not important — compression and cost efficiency are. Stored on HDD or cold cloud tiers (S3 Glacier). Cheap to store but slow/expensive to retrieve. Example: web access logs from 2 years ago.

**The lifecycle is the bridge**: Policies automatically transition data from Hot → Cold over time as value declines.

### Q2: How does GDPR "Right to be Forgotten" affect a Data Engineer?

When users request deletion of their account and personal data, DEs must locate and purge every trace across ALL systems — Data Warehouse, Data Lake, backups, replicas.

Two key techniques:

- **Anonymization**: Replace PII columns (name, email, phone) with random, meaningless strings. Preserves transaction records for aggregate reporting while destroying personal identity.
- **Crypto-shredding**: Encrypt each user's data with a unique key. To "delete" the user, simply destroy their encryption key — the data becomes permanently unreadable without physically touching backup media.

### Q3: How to automate partition lifecycle policies in BigQuery or Snowflake?

**BigQuery**: Configure `partition_expiration_days` on time-partitioned tables. Example: setting 90 days means BigQuery automatically drops partitions older than 90 days — no manual intervention needed.

**Snowflake**: Use Time Travel retention windows plus scheduled SQL tasks (cron-like) that run periodic archival or deletion commands on aged data. Time Travel provides a recovery safety net before permanent deletion via Fail-safe.

---

- Related to [[data-ingestion]] — Data ingestion is the Storage stage of the lifecycle (Stage 2), where data first enters managed systems
- Related to [[data-engineer]] — Data Engineers implement and automate lifecycle policies across cloud infrastructure
- Related to data pipeline operations — lifecycle management directly reduces cloud storage costs by migrating data to cheaper tiers
- Benchmark source: [[sources/data-lifecycle-handbook]] — Data Engineering Handbook (data lifecycle)
- Benchmark source: [[sources/data-engineering-handbook]] — Data Engineering Handbook (discipline overview)
