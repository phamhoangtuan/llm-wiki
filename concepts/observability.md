---
title: "Observability"
type: concept
tags: [system-design, monitoring, metrics, reliability, devops]
created: 2026-05-24
updated: 2026-06-15
sources: [system-design-interview-xu]
aliases: [monitoring, telemetry, system-observability]
---

## Summary

Observability is the ability to understand a system's internal state by examining its outputs — metrics, logs, and traces. In distributed systems, observability is not optional: without it, you cannot detect failures, debug issues, or make informed scaling decisions.

## The Three Pillars

| Pillar | What It Captures | Example |
|--------|------------------|---------|
| **Metrics** | Numeric data over time | CPU usage, request latency, error rate |
| **Logs** | Discrete events | "User login failed: wrong password", "DB connection timeout" |
| **Traces** | Request path through services | `GET /api/users` → LB → Web → DB → Cache |

## Monitoring Levels

| Level | Metrics | Purpose |
|-------|---------|---------|
| **Host-level** | CPU, memory, disk I/O, network | Detect server overload or hardware failure |
| **Aggregated-level** | DB query latency, cache hit rate, queue length | Evaluate health of each tier |
| **Business-level** | DAU, conversion rate, revenue | Measure real-world system impact |

## Key Metrics to Track

| Metric | Why It Matters |
|--------|---------------|
| **Latency** | p50, p95, p99 response times — users feel p95, not average |
| **Throughput** | Requests per second — capacity planning |
| **Error rate** | 4xx/5xx percentage — reliability indicator |
| **Saturation** | How "full" a resource is (CPU > 80%? Queue depth?) |

> **Principle**: You can't scale what you can't measure. Manual operations don't scale — automate monitoring, alerting, and remediation.

---
- Core to [[scalable-architecture]] — essential for operating distributed systems
- Related to [[message-queue]] — queue depth and consumer lag are critical signals
- Related to [[cache-strategy]] — hit rate and eviction rate reveal cache health
- Related to [[database-replication]] — replication lag must be monitored
- Related to [[load-balancer]] — tracks backend health and traffic distribution
- Required by [[kubernetes-operator]] — production operators export Prometheus metrics, structured logs, and OpenTelemetry traces