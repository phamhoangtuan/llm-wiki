---
title: "Watermarks"
type: concept
tags: [streaming, event-time, data-engineering, apache-flink, apache-beam]
created: 2026-07-14
updated: 2026-07-14
sources: [streaming-systems]
aliases: [event-time-watermark]
---

## Summary

A **Watermark** is a notion of input completeness in [[stream-processing|stream processing]] — a monotonically increasing timestamp that tells the system "all events with event time less than the watermark have been observed." It is the critical mechanism that allows streaming systems to produce correct results despite out-of-order data and late arrivals (source: [[sources/streaming-systems]]).

## Why Watermarks Exist

In distributed systems, [[event-time-processing|event time ≠ processing time]]. Events arrive out of order due to network lag, device clock skew, or partitioned sources. Without watermarks, the system can never know when a window is "complete" — it would either produce premature results or wait forever.

Watermarks provide a **heuristic** of completeness: the system can finalize windows earlier than the watermark while handling late data explicitly.

## How Watermarks Work

```
Processing Time:  |--- event1(t=10:01) --- event3(t=10:03) --- event2(t=10:02) --->
Event Time:       |--- 10:01 ------------ 10:03 ------------ 10:02 ------------->
Watermark:        |--- 10:00 ------------ 10:01 ------------ 10:02 ------------->
```

The watermark advances as the system observes events. At any point, windows with end times < watermark can be considered complete.

### Watermark Generation Strategies

| Strategy | How It Works | Trade-off |
| ---------- | ------------- | ----------- |
| **Perfect** | Knows all data — no late data | Impossible in practice |
| **Heuristic** | Estimates based on observed max event time minus allowed lateness | Balances completeness vs latency |
| **Idle source** | Marks a source as idle (no new data) | Prevents watermark stall when one partition is silent |

## Watermarks vs Triggers

Watermarks control **correctness** (when windows are complete). Triggers control **output timing** (when results are emitted). A system can emit speculative results via early triggers *before* the watermark, then refined results *at* the watermark, and corrections *after* for late data.

## Key Takeaways

1. Watermarks are heuristics, not guarantees — late data can and will arrive after the watermark
2. The watermark delay trades **latency** (wait for late data) vs **completeness** (close windows sooner)
3. Watermark propagation is essential for multi-stage pipelines — downstream stages inherit upstream watermarks
4. Idle source detection prevents watermark stalls when a partition produces no events

---

- Core to [[stream-processing]] — watermarks enable correct event-time computation
- Related to [[event-time-processing]] — watermarks are the mechanism that makes event-time processing practical
- Related to [[windowing]] — windows close based on watermark progress
- Core to [[apache-flink]] — Flink's watermark implementation is the production reference
- Benchmark source: [[sources/streaming-systems]] — Akidau's definitive treatment of watermarks
