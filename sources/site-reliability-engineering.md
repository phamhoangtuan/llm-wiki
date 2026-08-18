---
title: "Site Reliability Engineering: How Google Runs Production Systems"
type: source
source_type: book
author: "Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy"
url: "https://sre.google/sre-book/table-of-contents/"
source_date: 2016
ingested: 2026-08-18
tags: [site-reliability-engineering, SRE, reliability, SLO, observability, distributed-systems]
concepts: [site-reliability-engineering, observability, scalable-architecture, load-balancer, database-replication, testing-strategy]
---

## Summary

Google's SRE book defines operations as a software engineering problem. Reliability is managed with measurable targets, automation, controlled failure, and learning systems rather than permanent heroics. The goal is to scale humans more slowly than machines.

## Core Ideas

### Measure Reliability with SLIs, SLOs, and Error Budgets

A **Service Level Indicator (SLI)** measures a user-visible property such as latency, throughput, or error rate. A **Service Level Objective (SLO)** states the target. The error budget is the allowed unreliability, commonly expressed as `1 - SLO`; it makes the trade-off between shipping and stability explicit.

### Scale Traffic and Data Paths

The notes describe hierarchical load balancing, deterministic subsetting, and weighted routing based on backend capability rather than request count alone. For critical pipelines, durable task state, leases, journaling, and uniquely named outputs provide recovery and effectively exactly-once behavior.

### Stop Cascading Failures

Load shedding, graceful degradation, randomized exponential backoff with jitter, and deadline propagation prevent overload from multiplying through a dependency graph. Retrying a request after its caller has already abandoned it is wasted work, so deadlines must travel through the RPC stack.

### Treat Recoverability as a Separate Property

Replication does not equal backup. Local snapshots, offsite copies, soft deletion, lazy deletion, and independent validation protect against operator mistakes, corrupted data, and site-wide failures.

### Test the Failure Modes

Stress tests find breaking points; canaries expose changes to a small traffic slice; negative results should be documented so future teams do not repeat failed experiments. Reliability is an empirical property, not an assumption.

### Reduce Toil and Learn Without Blame

Manual, repetitive operational work should remain below half of an engineer's time and be replaced with automation. Blameless postmortems focus on systemic causes and turn incidents into improvements.

## Connections

- Provides the operating model for [[observability]] and measurable reliability targets.
- Extends [[scalable-architecture]] and [[load-balancer]] with failure containment and capacity practices.
- Clarifies the difference between [[database-replication]] and recoverable backups.
- Complements [[testing-strategy]] with stress, canary, and negative-result testing.
