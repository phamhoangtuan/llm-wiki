---
title: "Data Integration"
type: concept
tags: [data-management, etl, dama]
created: 2026-07-14
updated: 2026-07-14
sources: [dama-dmbok-2nd-edition]
---

# Data Integration

Movement and consolidation of data across systems. One of DAMA's eleven Knowledge Areas, also called "Data Integration and Interoperability."

## Core Functions

- **Extract-Transform-Load (ETL)** and **ELT** — moving data from sources to destinations
- **Change Data Capture (CDC)** — capturing incremental changes from source systems
- **API-based integration** — real-time data exchange via services
- **Data virtualization** — federated query without physical movement
- **Replication** — maintaining synchronized copies across systems

## Interoperability Dimension

Beyond simple movement, Data Integration addresses *interoperability* — ensuring data from different systems can be meaningfully combined. This requires shared semantics, common formats, and consistent encoding.

## Position in DAMA Framework

Part of the **Enable & Maintain** lifecycle phase. Data Integration implements the movement patterns defined by Data Architecture and governed by Data Governance.

## Relationship to Other KAs

- **Data Architecture** defines *what* moves and *where*
- **Data Quality** ensures *what arrives is fit for use*
- **Metadata Management** tracks lineage through integration paths

---

## Connections

- [[elt|ELT]] — Modern paradigm loading raw data first
- [[change-data-capture|Change Data Capture]] — Row-level change capture from transaction logs
- [[data-ingestion]] — Moving data from sources to data lake
- [[apache-kafka]] — Distributed event streaming platform for data movement
- [[data-ingestion]] — End-to-end flow from source to consumption
