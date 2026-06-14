---
title: "Data Governance"
type: concept
tags: [data-governance, compliance, security, metadata, data-quality]
created: 2026-06-14
updated: 2026-06-14
sources: [data-lifecycle-handbook, data-engineering-handbook]
aliases: [governance]
---

## Summary

**Data Governance** is the framework of policies, standards, and accountability structures that ensures data is managed as a strategic organizational asset. It defines who can take what action, on what data, under what circumstances — covering access control, classification, retention, quality standards, lineage tracking, and regulatory compliance.

While Data Engineering builds the pipelines that move and transform data, Data Governance ensures those pipelines operate within legal, ethical, and business boundaries.

## Core Pillars

| Pillar | Description |
|---|---|
| **Access Control** | Who can read, write, or delete data — enforced via RBAC, ABAC |
| **Data Classification** | Labeling data by sensitivity (PII, confidential, public) |
| **Retention & Lifecycle** | How long data is kept, when it's archived or destroyed |
| **Data Quality Standards** | Rules for completeness, accuracy, timeliness, consistency |
| **Lineage & Metadata** | Tracking where data came from, how it was transformed |
| **Compliance** | Meeting legal requirements: GDPR, CCPA, HIPAA, SOC2 |
| **Data Ownership** | Clear accountability: who owns each data domain |

## Why Governance Matters

Without governance:
- **Cost**: Uncontrolled data hoarding inflates storage bills; no one knows what's safe to delete.
- **Legal Risk**: GDPR "right to be forgotten" becomes nearly impossible without knowing where user data lives.
- **Trust Erosion**: Analysts make decisions on data they can't verify — lineage gaps destroy confidence.
- **Security**: Unclassified data means sensitive information may sit unprotected in dev environments.

## Governance in Practice

Data Engineers implement governance through:
- **Automated lifecycle policies** (e.g., S3 lifecycle rules, BigQuery partition expiration) — `(source: [[sources/data-lifecycle-handbook]])`
- **Data catalogs** (Unity Catalog, Apache Atlas, DataHub) for lineage and discovery
- **Schema enforcement** with contract testing
- **Audit logging** for all data access and mutations

---

- Core to [[data-lifecycle]] — Data Lifecycle Management operationalizes governance retention and archiving policies
- Related to [[data-engineer]] — DEs implement governance automation through pipeline design and infrastructure
- Related to [[dataops]] — DataOps applies software engineering discipline to governance enforcement
- Related to [[data-ingestion]] — Governance classification should begin at ingestion, not as an afterthought
- Related to [[unity-catalog]] — Unity Catalog is a catalog-centric governance implementation for Delta Lake
- Benchmark source: [[sources/data-lifecycle-handbook]] — Data Engineering Handbook (data lifecycle)
- Benchmark source: [[sources/data-engineering-handbook]] — Data Engineering Handbook (discipline overview)
