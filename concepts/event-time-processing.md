---
title: "Event Time Processing"
type: concept
tags: [stream-processing, time, distributed-systems, flink, correctness]
created: 2026-07-11
updated: 2026-07-11
sources: [stream-processing-apache-flink]
aliases: [event-time, stream-time-semantics]
---

## Summary

**Event Time Processing** is the practice of using the timestamp embedded in each data record (when the event actually occurred) rather than the time the system processes it. In distributed stream processing, event time is the only way to produce deterministic, reproducible results when data arrives out of order or with network delays.

## Three Time Concepts in Streaming

| Concept | Definition | Deterministic? | Best For |
|---------|-----------|----------------|----------|
| **Event Time** | Timestamp assigned by the source (e.g., sensor clock, log timestamp) | Yes | Correctness-critical analytics |
| **Processing Time** | Timestamp when the stream processor receives the record | No | Low-latency approximations, monitoring |
| **Ingestion Time** | Timestamp when the event enters the streaming platform (e.g., Kafka broker) | Partial | Simple systems without out-of-order handling |

## Why Event Time Matters

In distributed systems, events rarely arrive in order:

- Network congestion delays packet B behind packet A
- Mobile devices buffer events and send them in bursts
- Different sources have different clock skews

If you use **processing time**, the same dataset run twice may produce different results. Event time guarantees **result determinism**.

## Watermarks

**Watermarks** are the mechanism that makes event time processing practical. A watermark is a global progress marker that declares: *"I have processed all events up to timestamp T; no events older than T will arrive."*

```
Event stream:  [1] [3] [2] [5] [4] [7] [6] ...
Watermark:         W(2)     W(4)     W(6) ...
```

When a watermark of `W(4)` passes, the system can safely close the `[0–4)` window and emit its result.

### Watermark Strategies

| Strategy | Behavior | Trade-off |
|----------|----------|-----------|
| **Periodic** | Emit watermark at fixed intervals | Simple; may delay results if interval is long |
| **Bounded delay** | Assume events are at most X seconds late | Results emitted after X delay; may miss very late events |
| **Idle timeout** | Advance watermark past idle streams | Prevents one slow source from stalling all windows |

## Windowing with Event Time

Windows divide the infinite stream into finite chunks for aggregation:

| Window Type | Behavior | Example |
|-------------|----------|---------|
| **Tumbling** | Fixed, non-overlapping intervals | Sum every 1 minute |
| **Sliding** | Fixed interval, fixed slide (may overlap) | Average of last 5 minutes, computed every 1 minute |
| **Session** | Dynamic, based on activity gaps | User session ends after 30 minutes of inactivity |
| **Global** | Single window over all time | Running total since start |

## Late Data Handling

When an event arrives after its window has already been closed (behind the watermark):

1. **Drop** — Discard the late event (simple, loses data)
2. **Side output** — Route late events to a separate stream for manual inspection
3. **Update** — Recompute and emit corrected results (complex, requires downstream support)

## Key Takeaways

1. Event time is the only way to achieve deterministic results in distributed stream processing.
2. Watermarks balance correctness and latency — they tell the system when it's safe to conclude a window.
3. Window choice (tumbling, sliding, session) should match the business semantics, not just technical convenience.
4. Late data handling is a business decision, not just a technical one.

---

- Core to [[stream-processing]] — event time is one of the two fundamental challenges (alongside state)
- Expands [[apache-flink]] — Flink has the most mature event time and watermark implementation
- Related to [[real-time-analytics]] — RTA dashboards must choose between event-time correctness and processing-time speed
- Related to [[windowing]] — windows are the buckets into which event-time aggregations are grouped
- Related to [[stateful-stream-processing]] — state must be keyed and time-bounded for event time correctness
- Related to [[message-delivery-semantics]] — exactly-once delivery is prerequisite for correct event-time accounting
- Benchmark source: [[sources/stream-processing-apache-flink]] — Hueske's definitive coverage of Flink time semantics
