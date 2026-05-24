---
title: "Timely Dataflow"
type: concept
tags: [distributed-systems, stream-processing, incremental-computation]
created: 2026-05-24
updated: 2026-05-24
sources: [materialized-views-quick-insights]
---

## Summary

**Timely Dataflow (TD)** is a general computational model introduced in the **Naiad** paper (2013). It provides a low-level substrate where every message in the system carries a logical timestamp, and nodes can request notifications when a timestamp is "complete" — meaning no further messages for that timestamp can arrive. This mechanism enables correct, efficient incremental computation in distributed systems.

## Key Ideas

- **Timestamped messages**: Every piece of data flowing through the system is tagged with a logical timestamp, allowing the system to reason about ordering and completeness.
- **Notification mechanism**: A node tells the system "notify me when timestamp *t* is complete." The system tracks across the entire distributed cluster to ensure no more messages for *t* will arrive.
- **Three capabilities in one framework**: Before Naiad, applications needed separate systems for batch (high throughput), stream (low latency), and iterative computation. TD provides all three.

## The Four API Methods

| Method | Purpose |
| --- | --- |
| `send(message)` | Send a timestamped message to another node |
| `receive(message)` | Receive a timestamped message |
| `notify_at(t)` | Request notification when timestamp *t* is complete |
| `notification(t)` | Receive the notification — guaranteed no more messages for *t* |

## Relevance to Materialized Views

Most SQL MVs don't have loops, so TD's iterative computation support isn't the primary benefit. What matters for MVs is the **notification guarantee**: it tells the system when a given version of a view is complete and safe to emit. This is the correctness foundation that [[differential-dataflow|Differential Dataflow]] builds on.

## Historical Note

TD was designed for deeply nested iterative algorithms (e.g., graph processing). Its generality makes it a substrate for higher-level systems, including Differential Dataflow and, by extension, modern IVM implementations.

## Reference

Original paper: *The Naiad Project* — [ACM Digital Library](https://dl.acm.org/doi/epdf/10.1145/2517349.2522738)
---
- Foundation for [[differential-dataflow]] — versioned incremental computation built on TD's notification guarantee
- Supports [[incremental-view-maintenance]] — one of three theoretical IVM approaches
- Related to [[materialized-views]] — TD provides the completeness notification MV refresh needs
- Related to [[materialized-views-quick-insights]] — Vu Trinh's article introducing TD as an IVM approach
