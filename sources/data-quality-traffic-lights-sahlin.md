---
title: "Data Quality Traffic Lights — Robert Sahlin"
type: source
source_type: article
author: "Robert Sahlin (Nordnet Data Platform Engineering)"
url: "https://robertsahlin.substack.com/p/data-quality-traffic-lights"
source_date: 2026-06-17
ingested: 2026-06-17
tags: [data-quality, data-observability, lineage, dbt, looker, anomaly-detection, data-platform]
concepts: [data-quality-monitoring]
---

## Summary

Robert Sahlin, data platform engineer at Nordnet (Stockholm-based fintech), describes building a Data Quality Health Badge that surfaces real-time trust signals directly in Looker dashboards. The system rests on three pillars: detecting five failure modes (failed dbt tests, failed runs, source freshness violations, TimesFM-based volume anomalies, manual incident reports), building a lineage graph across dbt and Looker, and surfacing traffic-light trust signals (green/yellow/red) where users consume data.

## Core Message

> Trust in data rests on three pillars: detection (knowing what broke), context (knowing what's affected), and communication (telling the right people at the right time). Get these three right, and you create the infrastructure for programmatic trust.

## Key Takeaways

1. **Five failure modes**: failed dbt tests (with incident boundary detection via window functions), failed runs (including silent mid-execution crashes), source freshness violations, TimesFM-based volume anomaly detection, and manual incident overrides
2. **Incident lifecycle in SQL**: Four states — active, resolved, expired (30 days no execution), manually closed — implemented entirely via window functions and QUALIFY clauses, no external state management
3. **Lineage is the hard part**: Extract dbt manifest (full recursive dependency tree), parse LookML for explore-to-table mapping, stitch together for blast radius calculation
4. **TimesFM for anomaly detection**: BigQuery's foundation model for time series; handles seasonality automatically, minimal tuning, per-table sensitivity config with weekend/holiday suppression
5. **Beyond dashboards**: Incident status enriches GCP Knowledge Catalog, agents check health before generating SQL, ML retraining gates on data quality, operational services check before consuming data
6. **Batch lineage is sufficient**: Daily refresh of lineage graph (production DAG changes are rare); real-time not needed
7. **Build iteratively**: Start with test/run failures only, add volume anomalies later, manual overrides later, silent failure detection later — each iteration one new capability
8. **Actionability over accuracy**: Early versions showed "there's an incident" without context; adding team ownership, communication channels, and investigation links made it useful

## Companion Concept

→ [[data-quality-monitoring]]
