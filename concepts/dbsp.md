---
title: "DBSP"
type: concept
tags: [stream-processing, incremental-computation, formal-methods]
created: 2026-05-24
updated: 2026-05-24
sources: [materialized-views-quick-insights]
aliases: [Database Stream Processor]
---

## Summary

**DBSP (Database Stream Processor)** is a computational model for incremental view maintenance that takes a fundamentally different approach from [[timely-dataflow|Timely Dataflow]] and [[differential-dataflow|Differential Dataflow]]. Rather than building upward from a dataflow substrate, DBSP borrows from **Digital Signal Processing (DSP)** — the mathematics of circuits and signals.

## Core Insight

A database is a **stream of snapshots**. Changes to the database are a **stream of deltas**. A view is a query applied to each snapshot. Maintaining the view incrementally means computing the stream of *view deltas* from the stream of *database deltas*.

## The Four Operators

DBSP formalizes incremental computation with four operators:

| Operator | Purpose |
|---|---|
| `lift` | Lifts a function from values to streams — converts a computation on individual values to one on streams of values |
| `delay` | Introduces a one-step time delay — allows reference to previous stream values |
| `recursive operator 1` | Supports recursive programs (fixed-point computation) |
| `recursive operator 2` | Supports recursive programs (convergence detection) |

## Key Properties

- **Functionally complete for SQL**: Any standard SQL query can be automatically converted into an incremental version using these four operators. No manual transformation needed.
- **DSP-based formalism**: By grounding in signal processing mathematics, DBSP provides rigorous correctness guarantees without requiring a distributed dataflow substrate.
- **Automatic incrementalization**: The `lift` operator converts any function to its stream version, making incremental maintenance systematic rather than ad-hoc.

## Contrast with TD/DD

| | Timely Dataflow | Differential Dataflow | DBSP |
|---|---|---|---|
| **Foundation** | Distributed dataflow | Built on TD | Digital Signal Processing |
| **Key mechanism** | Timestamp notifications | Versioned diffs on TD | Stream operators (lift, delay) |
| **SQL completeness** | General computation | General computation | Functionally complete for SQL |
| **Approach** | Bottom-up (substrate) | Mid-level (on TD) | Top-down (math formalism) |

## Reference

Original paper: *DBSP: A Language for Incremental View Maintenance* — [SIGMOD Record 2024](https://sigmodrecord.org/publications/sigmodRecord/2403/pdfs/20_dbsp-budiu.pdf)

---

- Contrasts with [[timely-dataflow]] — different foundation — DSP vs distributed dataflow
- Contrasts with [[differential-dataflow]] — different formalism — stream operators vs versioned diffs
- Supports [[incremental-view-maintenance]] — one of three theoretical IVM approaches
- Related to [[materialized-views]] — DBSP can automatically convert any SQL query to incremental form
- Related to [[materialized-views-quick-insights]] — Vu Trinh's article introducing DBSP as IVM approach
