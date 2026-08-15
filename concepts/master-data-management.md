---
title: "Master Data Management"
type: concept
tags: [data-management, mdm, dama]
created: 2026-07-14
updated: 2026-07-14
sources: [dama-dmbok-2nd-edition]
---

# Master Data Management

Maintaining a single "version of truth" for shared business entities across the enterprise. One of DAMA's eleven Knowledge Areas, grouped with Reference Data.

## What is Master Data?

Master data describes the core business entities used across an organization: customers, products, suppliers, employees, locations. Unlike transactional data, master data is relatively stable and shared across multiple systems.

## Key Challenges

- **Duplication**: The same customer exists in CRM, billing, and support systems with different IDs
- **Inconsistency**: Different systems maintain conflicting attributes (addresses, statuses)
- **Synchronization**: Keeping all systems updated when master data changes

## MDM Architectural Styles

- **Registry**: Central index pointing to where data lives (lightweight, no data movement)
- **Consolidation**: Master data aggregated into a central hub (read-only to sources)
- **Coexistence**: Hub updates flow back to source systems (read-write)
- **Centralized**: All master data managed in a single system of record

## Role in DAMA Framework

Part of the **Enable & Maintain** lifecycle phase. MDM depends heavily on Data Governance for ownership decisions and Data Quality for trust.

---

## Connections

- [[data-governance]] — Decision rights and ownership for master data entities
- [[data-quality-monitoring]] — Ensuring master data is fit for use
- [[entity-resolution]] — Mapping surface forms to canonical entities
- [[data-modeling]] — Designing master data structures and relationships
- [[metadata-management]] — Tracking master data definitions and lineage
