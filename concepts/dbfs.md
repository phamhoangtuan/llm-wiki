---
title: "DBFS (Databricks File System)"
type: concept
tags: [databricks, storage, cloud, data-engineering]
created: 2026-06-23
updated: 2026-06-23
sources: [databricks-dea-study-guide]
aliases: [Databricks File System]
---

DBFS is an abstraction layer in the [[databricks-platform|Databricks platform]] that allows users to interact with cloud files using local filesystem syntax. It bridges the gap between ephemeral compute and durable storage.

## The Abstraction

| Before DBFS | After DBFS |
|-------------|------------|
| Navigate complex cloud APIs (AWS SDK, Azure SDK) | Interact as if it's a local file system |
| Manual, provider-specific path configurations | Standard file APIs (`/dbfs/my_folder/file.csv`) |
| Cloud-specific integration code for every task | No cloud-specific code needed |

## Persistence Mechanics

This is the most important concept to internalize:

- **Compute clusters are TEMPORARY (ephemeral)** — they can be terminated to optimize costs
- **The persistence layer is DURABLE** — data survives cluster shutdown

When files are saved via DBFS, they are written directly to underlying cloud storage:
- Azure workspace → persisted in **Azure Data Lake Storage (ADLS)**
- AWS workspace → persisted in **Amazon S3**
- GCP workspace → persisted in **Google Cloud Storage**

**Result**: Cluster terminated → data remains permanent → accessible in future sessions → no data loss.

## Key Insight

> You use local-style paths (`/dbfs/my_folder`) but data is persisted to cloud storage — best of both worlds: developer-friendly abstraction with cloud-scale durability.

## Usage Patterns

- **Data upload**: Upload CSV, JSON, Parquet files via DBFS for processing
- **Notebook access**: Read/write files from notebooks using standard file operations
- **Pipeline I/O**: Intermediate data staging between ETL steps
- **Library storage**: Store custom Python libraries and JARs for cluster initialization

---
- Builds on [[databricks-platform]] — DBFS is the filesystem layer within the Databricks platform
- Foundation for [[data-lakehouse]] — DBFS abstracts cloud storage to make Lakehouse architecture feel local