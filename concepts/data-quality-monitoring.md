---
title: "Data Quality Monitoring"
type: concept
tags: [data-quality, data-observability, lineage, monitoring, dbt, data-platform]
created: 2026-06-17
updated: 2026-06-27
sources: [data-quality-traffic-lights-sahlin, building-anonymization-pipeline, big-book-data-engineering]
aliases: [Data Quality Health Badge, Data Quality Traffic Lights, DQ Monitoring]
---

**Data Quality Monitoring** is the practice of continuously detecting, tracking, and communicating data quality incidents across a data platform — going beyond simple test failures to provide end-to-end visibility into data trustworthiness (source: [[sources/data-quality-traffic-lights-sahlin]]).

Unlike traditional data testing (which catches violations at build time), data quality monitoring operates continuously, tracks incident lifecycles, calculates downstream impact (blast radius), and surfaces trust signals directly where users consume data — in dashboards, catalogs, and automated systems.

## The Three Pillars of Data Quality Monitoring

### 1. Detection: Knowing What Broke

Comprehensive monitoring detects multiple failure modes, not just explicit test failures:

| Failure Mode | Detection Method | Example |
| --- | --- | --- |
| **Failed tests** | dbt run results parsed into incident records with start/end boundaries via window functions | Uniqueness test fails Monday, passes Wednesday → single 3-day incident |
| **Failed runs** | Cross-reference planned models vs completed models in audit logs | Cloud Run crashes mid-execution; models planned but never executed |
| **Source freshness** | dbt source freshness checks flagging late-arriving external data | Upstream system stops delivering; freshness threshold exceeded |
| **Volume anomalies** | ML-based time series forecasting (BigQuery TimesFM) detecting silent drops | Daily 50K rows drops to 200; pipeline succeeds but data incomplete |
| **Manual incidents** | Human-reported issues via UI for known problems not caught by automation | Planned maintenance, known upstream outages, false positive overrides |

### 2. Lineage: Knowing What's Affected

Detection alone is insufficient — the critical question is *what else is impacted?*

**dbt lineage extraction**: Parse the dbt manifest (JSON artifact) to build a complete recursive dependency graph — every table's full downstream tree, not just immediate children.

**BI/semantic layer lineage**: Parse LookML (or equivalent) to map explores and dashboards back to their underlying warehouse tables.

**Blast radius calculation**: Join the two lineage graphs. When a core customer table breaks, instantly surface which downstream models, explores, and dashboards inherit that incident.

**Batch lineage refresh** (daily) is sufficient for most platforms — production DAG changes are infrequent.

### 3. Communication: Telling the Right People at the Right Time

Trust signals must appear where users actually work:

- **In-dashboard health badges**: Green (healthy), yellow (warnings), red (active errors) — visible when users load dashboards
- **Dashboard-specific filtering**: Health badge scoped to explores used on that specific dashboard, not platform-wide noise
- **Platform dashboard**: Centralized bird's-eye view sorted by severity, showing every explore's status
- **Data catalog enrichment**: Incident status attached as asset metadata for discovery-time awareness
- **Proactive notifications**: Push alerts to team channels for high-severity incidents affecting owned data

## Incident Lifecycle

Incidents progress through four states, managed entirely in SQL:

1. **Active** — end time is null or in the future; currently failing
2. **Resolved** — first successful run after a failure detected via window functions
3. **Expired** — no execution for 30 days (likely test renamed or removed); auto-closed
4. **Manually closed** — overridden by operations via incident management UI

The implementation uses `QUALIFY` and window functions to detect state transitions (first success after failure, 30-day expiration) without external state management.

## Volume Anomaly Detection

Silent failures — where pipelines succeed but data is incomplete — are caught via volume anomaly detection:

- **Foundation model approach**: BigQuery's TimesFM handles seasonality, trends, and patterns automatically
- **Per-table configuration**: User-driven tables (login events, searches) suppress weekend anomalies; system-driven tables (balances, positions) maintain consistent thresholds
- **Tuning is critical**: Holiday awareness, adjustable sensitivity, domain-specific thresholds
- **Auto-resolution**: Anomalies auto-close after 2 days to prevent stale warnings

Traditional statistical thresholds (standard deviation from mean) are simpler but produce more false positives than ML-based approaches for real-world data with complex seasonal patterns.

## Beyond Dashboards: Programmatic Trust

The incident status data becomes a foundational primitive for automated decision-making:

| Consumer | Quality-Aware Behavior |
| --- | --- |
| **Analytics agents (LLMs)** | Check incident status before generating SQL; warn users or suggest alternatives |
| **ML retraining pipelines** | Gate on data quality; abort retraining and keep previous model if training data has active incidents |
| **Operational services** | Pricing services check rate tables; report generators defer if source data compromised |
| **Data catalog** | Enrich asset metadata with health status for discovery-time awareness |
| **Self-service incident mgmt** | Data producers close/acknowledge incidents directly, decentralizing ownership |

## Anonymization Output Monitoring

In anonymization pipelines (source: [[sources/building-anonymization-pipeline]]), data quality monitoring takes on a privacy-specific dimension:

- **Output validation**: After anonymization transformation (generalization, suppression, randomization), monitor that outputs still satisfy the identifiability threshold
- **Continuous risk assessment**: Anonymization is not "set and forget" — ongoing monitoring detects when risk drifts above acceptable levels as new data arrives
- **Safe Outputs check**: Verify that aggregate analysis results don't inadvertently disclose information about individuals or small groups — the fifth dimension of the Five Safes framework

This extends traditional quality monitoring (detecting broken pipelines, missing data) to include privacy-preservation validation.

## Key Principles

1. **Actionability over accuracy** — showing context (team ownership, links, descriptions) matters more than perfect detection
2. **Automation is non-negotiable** — daily lineage, detection, and badge refreshes must run without human intervention
3. **Start simple, add gradually** — launch with test/run failures only; add volume anomalies, manual overrides, silent failure detection incrementally
4. **Tune relentlessly** — anomaly detection ships with false positives; expect continuous iteration based on real-world feedback
5. **Choose tools that reduce complexity** — TimesFM abstracted away ML infrastructure while delivering production-grade anomaly detection

---

## Connections

- [[dataops]] — DataOps applies software engineering practices to data; quality monitoring is a key DataOps practice
- [[data-governance]] — Governance frameworks that data quality monitoring enforces and validates
- [[dbt]] — dbt's testing framework and manifest are foundational to quality monitoring infrastructure
- [[cicd-data-pipelines]] — CI/CD practices that prevent quality regressions at build time; monitoring catches what CI/CD misses at runtime
- [[delta-live-tables|DLT Expectations]] — declarative quality rules enforced at each Medallion pipeline stage (warn, drop, or halt)
- Data observability — Monitoring, alerting, and lineage together form data observability; a natural next concept to formalize from this source
- Related to [[data-anonymization]] — output validation and continuous risk monitoring are quality dimensions specific to anonymization pipelines
