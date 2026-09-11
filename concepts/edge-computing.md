---
title: "Edge Computing"
type: concept
tags: [iot, distributed, latency, streaming, analytics]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [edge-analytics, edge-processing]
---

## Summary

**Edge Computing** is the paradigm of processing data near its source — at the "edge" of the network — rather than sending all data to a centralized cloud or data center. By analyzing data locally (on IoT devices, routers, or local servers), edge computing reduces network bandwidth, minimizes latency, and enables real-time decisions even when cloud connectivity is intermittent.

## Why Edge Computing Matters

| Problem | Edge Solution |
|---------|-------------|
| Network latency | Process locally; decisions in milliseconds without round-trips to cloud |
| Bandwidth costs | Send only aggregated insights, not raw data streams |
| Connectivity gaps | Continue operating when cloud link is down |
| Data sovereignty | Keep sensitive data local; comply with geographic regulations |
| Scale | Distribute computation across millions of edge nodes |

## Edge vs Cloud vs Fog

| Layer | Location | Role |
|-------|----------|------|
| **Edge** | Device itself (sensor, camera, phone) | Ultra-low latency, immediate action |
| **Fog** | Local gateway, on-premise server | Aggregation, filtering, local coordination |
| **Cloud** | Centralized data center | Deep analytics, long-term storage, training |

## Edge Analytics Use Cases

- **Autonomous vehicles** — Real-time obstacle detection can't wait for cloud round-trip
- **Smart manufacturing** — Detect equipment anomalies on the factory floor
- **Retail** — In-store cameras analyzing foot traffic without sending video to cloud
- **Healthcare** — Wearable devices monitoring vitals and alerting locally
- **Energy grids** — Real-time load balancing across distributed power sources

## Challenges

- **Limited compute** — Edge devices have constrained CPU, memory, and battery
- **Heterogeneity** — Thousands of device types with different capabilities
- **Management at scale** — Deploying, updating, and monitoring millions of edge nodes
- **[[model-quantization|Model quantization]]** — ML models must be compressed to run on edge hardware

## Key Takeaways

1. Edge computing moves computation closer to data sources to reduce latency and bandwidth.
2. It complements — not replaces — cloud analytics; most architectures use a tiered edge-fog-cloud model.
3. Model quantization and lightweight inference engines are essential for ML at the edge.

---

- Related to [[real-time-analytics]] — edge analytics is a specialized form of RTA at the network edge
- Related to [[model-quantization]] — quantized models are required to fit ML on edge hardware
- Related to [[stream-processing]] — edge devices often run lightweight stream processors
- Related to [[apache-kafka]] — Kafka at the edge (Kafka on devices/gateways) is an emerging pattern
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham covers edge analytics as a future trend
