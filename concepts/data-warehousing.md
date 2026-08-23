---
title: "Data Warehousing"
type: concept
tags: [data-management, olap, analytics, dama]
created: 2026-07-14
updated: 2026-07-14
sources: [dama-dmbok-2nd-edition]
---

# Data Warehousing

Managing data for analysis and reporting. One of DAMA's eleven Knowledge Areas, grouped with Business Intelligence.

## Purpose

A data warehouse is a system designed for analytical queries (OLAP) rather than transactional processing (OLTP). It integrates data from multiple source systems into a unified, historical view optimized for decision support.

## Core Concepts

- **ETL/ELT**: Extracting, transforming, and loading data from operational systems
- **Dimensional Modeling**: Star and snowflake schemas organizing data into facts and dimensions
- **OLAP**: Online Analytical Processing — multi-dimensional analysis and aggregation
- **Data Marts**: Department-specific subsets of the warehouse
- **Historical tracking**: Slowly Changing Dimensions (SCDs) for tracking changes over time

## Modern Evolution

Traditional on-premise data warehouses have evolved into cloud-native solutions (Snowflake, BigQuery, Redshift) and the Data Lakehouse architecture, which combines warehouse governance with data lake flexibility.

## Role in DAMA Framework

Part of the **Use & Enhance** lifecycle phase. Data Warehousing sits atop Governance, Architecture, and Integration foundations per Geuens' dependency model.

---

## Connections

- [[data-lakehouse]] — Modern architecture combining lake economics with warehouse governance
- [[elt]] — Modern data loading paradigm
- [[medallion-architecture]] — Bronze/Silver/Gold progressive refinement
- [[snowflake-data-cloud]] — Cloud-native data platform with separated storage and compute
- [[dbt]] — SQL transformation framework for warehouse data
