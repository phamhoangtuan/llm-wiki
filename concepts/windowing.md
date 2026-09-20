---
title: "Windowing"
type: concept
tags: [stream-processing, time, aggregation, analytics, flink]
created: 2026-07-11
updated: 2026-07-11
sources: [stream-processing-apache-flink]
aliases: [windows, stream-windows]
---

## Summary

**Windowing** is the technique of dividing an infinite data stream into finite, manageable chunks ("windows") over which aggregations and computations can be performed. Because streams are unbounded, windowing is necessary to produce bounded results — sums, averages, counts, and joins that would otherwise be impossible to compute.

## Why Windows Are Needed

An unbounded stream never ends. You cannot compute:

- "The total revenue" (it grows forever)
- "The average temperature" (denominator is infinite)

Windows introduce artificial but meaningful boundaries:

- "The total revenue **per minute**"
- "The average temperature **over the last 5 minutes**"

## Window Types

| Window Type | Behavior | Use Case |
|-------------|----------|----------|
| **Tumbling** | Fixed-size, non-overlapping, contiguous | Hourly sales totals, daily active users |
| **Sliding** | Fixed-size, fixed slide interval (overlaps allowed) | 5-minute moving average computed every minute |
| **Session** | Dynamic, bounded by inactivity gap | User sessions (end after 30 min of no events) |
| **Global** | Single window over all time | Running total since system start (requires triggers) |
| **Count** | Triggered by number of events | Process every 100 events |

## Tumbling vs Sliding vs Session

```
Tumbling (1-min windows):
[0:00-0:01) [0:01-0:02) [0:02-0:03) ...

Sliding (5-min window, 1-min slide):
[0:00-0:05) [0:01-0:06) [0:02-0:07) ...

Session (gap = 2 min):
[A-A-A] ..gap.. [B-B] ..gap.. [C] ...
```

## Time-Based vs Count-Based

| Basis | Trigger | Best For |
|-------|---------|----------|
| **Time** | Clock (event time or processing time) | Periodic reporting, dashboards |
| **Count** | Number of events | Batch-like processing within streams |
| **Session** | Inactivity gap | User behavior, clickstream analysis |

## Late Data and Windows

When using [[event-time-processing]], events may arrive after their window has already closed. Strategies:

1. **Allowed Lateness** — Keep window open for an additional grace period (e.g., 5 minutes)
2. **Side Output** — Route late events to a separate stream
3. **Drop** — Discard late events (simplest, loses data)

## Key Takeaways

1. Windowing transforms infinite streams into finite computations.
2. Tumbling windows are the default for periodic reporting; sliding windows for moving averages; session windows for user behavior.
3. Window choice should match business semantics, not just implementation convenience.
4. In event-time systems, late data handling is a first-class concern.

---

- Core to [[stream-processing]] — windows are the primary abstraction for bounded computation on unbounded streams
- Expands [[event-time-processing]] — windows are evaluated using event time with watermark-triggered emission
- Expands [[stateful-stream-processing]] — windows accumulate state that must be checkpointed and recovered
- Expands [[apache-flink]] — Flink provides the most complete windowing implementation (tumbling, sliding, session, global)
- Related to [[real-time-analytics]] — RTA dashboards are powered by windowed aggregations
- Related to [[timely-dataflow]] — Naiad's timestamp-based notification model underpins modern windowing semantics
- Benchmark source: [[sources/stream-processing-apache-flink]] — Hueske covers Flink's window operators in depth
