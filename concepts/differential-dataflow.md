---
title: "Differential Dataflow"
type: concept
tags: [distributed-systems, stream-processing, incremental-computation]
created: 2026-05-24
updated: 2026-06-15
sources: [materialized-views-quick-insights]
---

## Summary

**Differential Dataflow (DD)** is a programming model built on top of [[timely-dataflow|Timely Dataflow]]. It answers the question: *given that we know when a computation is complete (via TD's notification mechanism), how do we compute as little as possible as the input changes?*

## Key Ideas

- **Versioned state tracking**: DD tracks data as multiple versions ordered by timestamps (from Timely Dataflow). Each version represents the state of the data at a point in logical time.
- **Incremental updates**: When input changes arrive, DD computes only the *difference* (the differential) between versions, rather than recomputing from scratch.
- **Reuse of computation**: Because versions are ordered and the system knows which are finalized (thanks to TD notifications), DD can safely reuse prior partial results.

## Relationship to Timely Dataflow

DD is a **higher-level abstraction** built directly on TD. TD provides the infrastructure for timestamp-ordered messaging and completion notifications. DD adds the computation model layer: tracking versioned collections, computing differences between them, and ensuring that incremental updates are correct and minimal.

## Relationship to Materialized Views

DD is one of the three theoretical foundations for [[incremental-view-maintenance|Incremental View Maintenance]]. Its contribution is showing how to efficiently compute only the changed portions of a view when the underlying data changes, while maintaining correctness guarantees via TD's notification system.

## Reference

Original paper: *Differential Dataflow* — [CIDR 2013](https://www.cidrdb.org/cidr2013/Papers/CIDR13_Paper111.pdf)
---
- Extends [[timely-dataflow]] — DD uses TD's timestamp and notification mechanism
- Supports [[incremental-view-maintenance]] — one of three theoretical IVM approaches
- Related to [[materialized-views]] — DD computes minimal diffs for MV refresh
- Alternative [[dbsp]] — a different IVM formalism based on signal processing
- Related to [[sources/materialized-views-quick-insights]] — Vu Trinh's article comparing IVM approaches
