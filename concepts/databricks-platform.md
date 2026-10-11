---
title: "Databricks Platform"
type: concept
tags: [databricks, data-engineering, lakehouse, platform]
created: 2026-06-23
updated: 2026-06-23
sources: [databricks-dea-study-guide, big-book-data-engineering]
aliases: [Databricks]
---

Databricks is a unified Data Intelligence Platform built on a 4-layer architecture, delivering a Lakehouse experience for data engineers, scientists, and analysts across AWS, Azure, and GCP.

## Four-Layer Architecture

### Layer 1: Cloud Infrastructure

Provider-managed hardware, networking, and virtual machines on Azure, AWS, or GCP. The foundation layer — customer retains full control of cloud resources.

### Layer 2: Databricks Runtime

Pre-configured, optimized VM image integrating [[apache-spark]] with [[delta-lake]]. Delta Lake provides ACID transactions, reliability, and consistency — transforming standard data lakes into reliable storage. The runtime is the compute engine powering all workloads.

### Layer 3: Data Governance (Unity Catalog)

Centralized security and governance for all data and AI assets. Evolution from Hive Metastore (legacy, learning-friendly) to [[unity-catalog]] (centralized, fine-grained access control, multi-cloud, audit logging). Manages catalogs, schemas, tables, files, and ML models as a single source of truth.

### Layer 4: Workspace

Primary interface for data professionals supporting Python, SQL, R, Scala, and Java. Collaborative tools: notebooks, dashboards, automated workflows. AI-powered features: Databricks Assistant (code generation, query explanation) and AI Search (natural language asset discovery). [[delta-live-tables|Delta Live Tables]] provides declarative ETL with built-in data quality expectations. DatabricksIQ uses Unity Catalog metadata to power organization-specific AI models for code generation, debugging, and optimization.

## Control Plane vs Data Plane

Architectural "separation of powers" — a critical security and operational boundary:

| Dimension | Control Plane | Data Plane |
| ----------- | -------------- | ------------ |
| Managed By | Databricks | Customer |
| Resources | Web UI, Cluster Manager, Job Scheduler, Notebooks | Cluster VMs, Cloud Storage (ADLS/S3/GCS), DBFS |
| Location | Databricks Cloud Account | Customer Cloud Subscription |

### Why Separation Matters

- **Data Sovereignty**: Compute and storage remain in customer's account. Raw data never leaves the governed environment.
- **Maintenance Isolation**: Databricks updates the platform without touching customer data. Security patches applied without data exposure.

## SQL-First Strategy

Databricks DE Associate (V3) certification emphasizes SQL as the primary interface for ETL/ELT. Rationale: SQL is the most accessible language for data manipulation, lowers barrier for traditional analysts. Python remains indispensable for complex operations.

---

- Implements [[data-lakehouse]] — Databricks is the leading commercial Lakehouse platform
- Foundation for [[dbfs]] — DBFS is the filesystem abstraction within the Databricks platform
- Builds on [[apache-spark]] — Spark is the compute backbone of the Databricks Runtime
- Builds on [[delta-lake]] — Delta Lake provides ACID transactions in Layer 2
- Foundation for [[unity-catalog]] — Unity Catalog governs Layer 3 of the architecture
- Runs [[delta-live-tables]] — declarative ETL framework native to the platform
- Implements [[medallion-architecture]] — DLT pipelines are purpose-built for Bronze → Silver → Gold
