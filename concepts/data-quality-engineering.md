---
title: "Data Quality Engineering"
type: concept
tags: [data-quality, data-engineering, governance, manufacturing, specifications]
created: 2026-08-24
updated: 2026-08-24
sources: [data-quality-engineering-financial-services-buzzelli]
aliases: [DQ Engineering, Data Quality Specifications, DQS]
---

## Summary

**Data Quality Engineering** is the discipline of treating data like manufactured material — with inspection, tolerances, and control points at every stage of the pipeline. Pioneered by Brian Buzzelli in financial services, it replaces reactive firefighting with proactive quality contracts between data producers and consumers (source: [[sources/data-quality-engineering-financial-services-buzzelli]]).

## The Manufacturing Mindset

The core insight: stop treating data as passive. Map every pipeline as **materials flow** (source → process → output), define what "good" looks like for each material (a control spec per critical field), and move checks **left** so defects are caught at ingestion rather than found by downstream reconciliations.

Create simple sensors (volume checks, schema checks, latency monitors) that feed a short feedback loop to the owner/steward. Run a lightweight waste analysis — where are repeated fixes happening? — and automate the repetitive fixes first.

## Data Quality Specifications (DQS)

DQS is the **contract between producers and consumers**: for each data element, state:

| Zone | Meaning | Action |
| --- | --- | --- |
| **Valid** | Within acceptable range | Publish normally |
| **Suspect** | Warning zone | Flag + notify; consumers choose whether to accept |
| **Invalid** | Unacceptable | Block publish |

Tag each zone with business impact. Implement DQS as pipeline validation code (unit tests + runtime validators). Treat DQS as living — review quarterly with stakeholders to tune thresholds that produce too many false positives.

## Data Shape Matters

Data has form, and each shape demands different quality dimensions:

| Shape | Key Dimensions |
| --- | --- |
| Single values | Conformity, accuracy |
| Time series | Continuity, timeliness, precision |
| Panels | All of the above — panel math is unforgiving |
| Reference tables | Conformity, cohesion |

Specify the required shape first, then map only the relevant quality dimensions. This reduces noisy alerts and focuses engineering effort where it matters.

## Template Library

Build reusable check patterns for each dimension:

- **Completeness** — null counts, expected partitions
- **Timeliness** — max latency from source to destination
- **Accuracy** — sample comparison to authoritative source
- **Precision** — decimal scale validation
- **Conformity** — regex/enums for format compliance
- **Congruence** — cross-field expectations
- **Collection** — expected set of IDs present
- **Cohesion** — foreign key existence checks

Compose atomic checks into a **scorecard** per dataset outputting pass/suspect/invalid with recommended remediation.

## Operational Efficiency

The financial argument: measure the cost of late fixes (person-hours, business impact, delayed reports) versus the cost of building pre-use validations. Instrument incidents to capture person-hours and business cost. Prioritize automation for high-volume/high-impact pipelines first. Track **avoided costs** as a KPI to demonstrate value to governance and leadership.

## Scaling DQ Across the Enterprise

1. Prioritize by impact and volume using a heatmap
2. Deploy a minimal platform: catalog, validation engine, dashboards, alerting
3. Make DQS part of pipeline CI/CD — quality is gated automatically
4. Include DQ metrics in team KPIs
5. Train engineers and consumers on the DQS language
6. Run quarterly retrospectives to refine thresholds and tooling

> "Patterns are straightforward; the real work is consistent execution, governance, and culture."

---

- Related to [[data-quality-monitoring]] — DQS provides the specification framework; monitoring provides the detection and communication layer
- Related to [[data-governance]] — governance organizes the accountability that makes DQS scale
- Related to [[master-data-management]] — mastered entities eliminate many conformity and cohesion failures
- Related to [[fail-fast]] — "move checks left" is the data-quality expression of fail-fast
- Related to [[cicd-data-pipelines]] — DQS as CI gating for data pipelines
- Related to [[data-observability]] — DQS scorecards feed observability dashboards
- Benchmark source: [[sources/data-quality-engineering-financial-services-buzzelli]] — Buzzelli's manufacturing-lens DQ guide
- Benchmark source: [[sources/data-quality-traffic-lights-sahlin]] — complementary monitoring approach from Nordnet
