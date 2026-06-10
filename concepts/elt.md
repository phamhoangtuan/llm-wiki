---
title: "ELT (Extract-Load-Transform)"
type: concept
tags: [data-engineering, elt, etl, data-warehouse, architecture]
created: 2026-05-28
updated: 2026-05-28
sources: [unlocking-dbt-design-deploy-transformations, data-engineering-with-dbt]
aliases: [Extract-Load-Transform]
---

## Summary

**ELT** (Extract-Load-Transform) is a data integration paradigm where raw data is extracted from source systems, loaded directly into the data warehouse (or data lake) with minimal processing, and then transformed in-place using the warehouse's compute power. This inverts the traditional ETL (Extract-Transform-Load) model where transformation happens before loading. ELT is the architectural foundation that [[dbt|dbt]] was built to serve.

## ELT vs ETL

```
ETL:  Source → [Transform on external server] → Load to Warehouse → Analytics
ELT:  Source → Load Raw to Warehouse → [Transform IN warehouse] → Analytics
```

| Dimension | Traditional ETL | ELT (with dbt) |
|---|---|---|
| **When to transform** | Before loading | After loading (in-warehouse) |
| **Where compute happens** | External ETL server | Cloud data warehouse |
| **Iteration speed** | Slow — must re-extract to fix logic | Fast — raw data already in warehouse; just re-run SQL |
| **Flexibility** | Schema locked at transform time | Schema decisions deferred; evolve incrementally |
| **Cost model** | Expensive compute + network transfer per iteration | Cheap storage; warehouse compute scales on demand |
| **Tool examples** | Informatica, Talend, SSIS | [[dbt|dbt]] + Fivetran/Airbyte/Stitch |

## Why ELT Wins in the Cloud Era

### 1. Storage is Cheap, Engineer Time is Expensive

Cloud storage (S3, GCS, BigQuery storage) costs fractions of a cent per GB/month. The real cost is **engineer time** spent waiting for data re-extraction.

> Example: Loading 100 GB from on-premise takes 5 hours.
> - ETL: Logic error → re-extract 100 GB → another 5 hours.
> - ELT + dbt: Raw data already in warehouse → fix SQL, re-run in 5 minutes.

### 2. Land Once, Transform Many Times

Raw data persists in the warehouse indefinitely. You can:
- Iterate on transformation logic without touching source systems
- Build multiple transformation pipelines from the same raw data
- Add new business logic without re-extracting historical data

### 3. Leverage Warehouse Compute

Modern cloud warehouses (Snowflake, BigQuery, Redshift) provide:
- **Elastic scaling** — scale compute up/down on demand
- **Separation of storage and compute** — pay only for what you use
- **Massive parallelism** — transform terabytes in minutes

By transforming in-warehouse, you use the same infrastructure that runs your queries — no separate ETL cluster to manage.

### 4. Deferred Schema Decisions

In traditional ETL, the schema must be defined at transform time — before data lands. In ELT:
- Raw data lands with minimal schema enforcement (or schema-on-read)
- Transformations build the final schema incrementally
- Schema evolution is handled in dbt, not at the extraction layer

## The ELT Stack

A typical modern ELT pipeline:

```
Sources (DBs, APIs, events)
    │
    ▼
[Extract + Load]  ← Fivetran, Airbyte, Stitch, Kafka Connect
    │
    ▼
[Raw Data]  ← Stored in warehouse/data lake (S3, BigQuery, Snowflake)
    │
    ▼
[Transform]  ← dbt: modular SQL, tests, docs, CI/CD
    │
    ▼
[Consume]  ← BI tools (Looker, Tableau), ML models, reverse ETL
```

## dbt's Role in ELT

dbt is the **canonical "T" tool** in the modern ELT stack:
- Transforms raw warehouse data into analytics-ready models
- Applies software engineering practices to SQL transformations
- Provides testing, documentation, and dependency management
- Integrates into CI/CD pipelines for data quality gates

→ See [[dbt]] for dbt's architecture and patterns.

## When ELT Makes Sense

| ✅ Use ELT | ❌ Stick with ETL |
|---|---|
| Cloud data warehouse in place | On-premise DB with limited compute |
| Raw data needed for multiple use cases | Single-purpose, fixed-schema pipeline |
| Team prefers SQL over proprietary tools | Highly regulated data requiring pre-load masking |
| Need fast iteration and experimentation | Simple, unchanging transformations |
---
- Powers [[dbt]] — dbt was designed specifically for the ELT paradigm's "Transform" step
- Defines [[analytics-engineer]] — the role that owns the transform layer in ELT
- Related to [[data-ingestion]] — ELT describes the full pipeline; ingestion handles the "EL" portion
- Benchmark source: [[sources/unlocking-dbt-design-deploy-transformations]] — Cyr & Dorsey's book explains why ELT beats ETL
