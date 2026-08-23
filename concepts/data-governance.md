---
title: "Data Governance"
type: concept
tags: [data-governance, compliance, security, metadata, data-quality]
created: 2026-06-14
updated: 2026-06-27
sources: [data-lifecycle-handbook, data-engineering-handbook, building-anonymization-pipeline]
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
- **Agent Sprawl** (2026): Without governance, AI agents produce minor data inconsistencies that compound into indecision and leadership pushback — the LLM-era equivalent of dashboard sprawl.

## The Five Safes Framework (Privacy Governance)

For data anonymization specifically, the Five Safes framework from Arbuckle & El Emam provides a holistic governance model (source: [[sources/building-anonymization-pipeline]]):

| Safe | Question |
|---|---|
| **Safe Projects** | Is this project legal and ethical? |
| **Safe People** | Who receives the data — what's their motivation and re-identification capability? |
| **Safe Settings** | Is the sharing environment technically secured? |
| **Safe Data** | Has identifiability been quantitatively reduced to an acceptable level? |
| **Safe Outputs** | Could aggregate analysis results inadvertently disclose individual information? |

The framework ensures governance evaluates the entire ecosystem — not just the data itself. See [[data-anonymization]] for the full anonymization workflow.

## Governance in Practice

Data Engineers implement governance through:
- **Automated lifecycle policies** (e.g., S3 lifecycle rules, BigQuery partition expiration) — `(source: [[sources/data-lifecycle-handbook]])`
- **Data catalogs** (Unity Catalog, Apache Atlas, DataHub) for lineage and discovery
- **Schema enforcement** with contract testing
- **Audit logging** for all data access and mutations

---

- Core to [[data-lifecycle]] — Data Lifecycle Management operationalizes governance retention and archiving policies
- Informs [[data-anonymization]] — Five Safes framework bridges governance policy and anonymization execution
- Related to [[data-engineer]] — DEs implement governance automation through pipeline design and infrastructure
- Related to [[dataops]] — DataOps applies software engineering discipline to governance enforcement
- Related to [[data-ingestion]] — Governance classification should begin at ingestion, not as an afterthought
- Related to [[unity-catalog]] — Unity Catalog is a catalog-centric governance implementation for Delta Lake
- Related to [[cicd-data-pipelines]] — CI/CD gates enforce governance rules (schema contracts, data quality thresholds) at deployment time
- Informed by [[data-engineering-fundamentals]] — the messy data reality (2026) makes governance more critical, not less
- Benchmark source: [[sources/data-lifecycle-handbook]] — Data Engineering Handbook (data lifecycle)
- Benchmark source: [[sources/data-engineering-handbook]] — Data Engineering Handbook (discipline overview)
- Benchmark source: [[sources/building-anonymization-pipeline]] — Arbuckle & El Emam on Five Safes, ethics committees, and trust-based governance
