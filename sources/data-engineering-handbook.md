---
title: "Data Engineering — Data Engineering Handbook"
type: source
source_type: article
author: "Data Engineering Handbook (kythuatdulieu.github.io)"
url: "https://kythuatdulieu.github.io/concepts/foundation/data-engineering/"
source_date: 2026-06-07
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-08
tags: [data-engineering, foundation, best-practices, pipeline]
concepts: [data-engineer]
---

## Summary

A foundational overview of Data Engineering as a discipline from the Vietnamese Data Engineering Handbook. Defines DE as the intersection of Software Engineering and Data Management, explains its rise through Big Data's three Vs (Velocity, Volume, Variety), details the four core pillars (Ingestion, Storage, Processing/Transformation, Orchestration), walks through a 6-step data processing pipeline, and provides practical best practices (idempotency, IaC, automated testing, decoupled storage/compute), common mistakes, and trade-offs.

## Core Message

> Data Engineering opens a "highway" connecting raw data alleys, filtering and delivering clean information to a central warehouse for analysis. It guarantees data scalability, reliability, and security across the organization.

## Key Takeaways

1. **Four pillars of DE**: Ingestion (Batch/Streaming), Storage (DWH/Lake/Lakehouse), Processing & Transformation (ETL/ELT), Orchestration (Airflow)
2. **Idempotency is critical**: Design pipelines so re-runs produce identical results — prevents data duplication on retry
3. **IaC for data infra**: Terraform to version-control infrastructure, enabling disaster recovery and reproducibility
4. **Automated quality testing**: Great Expectations, dbt tests — don't wait for user complaints
5. **Decouple storage and compute**: Scale independently, optimize costs
6. **Common mistakes**: No alerting (silent failures), over-engineering (Kafka for simple cron jobs), ignoring data governance (data swamp)
7. **ETL vs ELT trade-off**: ETL for compliance/security; ELT for scale and speed — neither is universally better

## Companion Concept

→ [[data-engineer]]
