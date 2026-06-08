---
title: "System Design Interview"
type: concept
tags: [system-design, interview, methodology, architecture]
created: 2026-05-24
updated: 2026-06-08
sources: [system-design-interview-xu]
aliases: [system-design-interview-framework]
---

## Summary

System design interviews are open-ended technical conversations where candidates design scalable distributed systems. Unlike coding interviews with right/wrong answers, system design is about navigating trade-offs — balancing performance, reliability, cost, and maintainability within constraints.

## The Framework

The canonical 4S framework for system design interviews:

1. **Scope (Clarify)** — Ask clarifying questions: scale, read/write ratio, latency requirements
2. **Sketch (Estimate)** — Back-of-the-envelope math: DAU → RPS → storage → bandwidth
3. **Structure (Design)** — Draw high-level architecture: clients, load balancers, web servers, databases, caches
4. **Scale (Optimize)** — Identify bottlenecks, propose incremental improvements, discuss trade-offs

## Why It's Hard

| Challenge | Description |
|-----------|-------------|
| Open-ended | No single correct answer — must define the problem space yourself |
| Vague requirements | "Design Twitter" — need to narrow scope with questions |
| Multi-dimensional | Must balance performance, reliability, cost, maintainability simultaneously |
| Collaborative | Interviewer acts as a colleague — must think out loud and incorporate feedback |

## Estimation Rules of Thumb

- 1M DAU ≈ 100 RPS peak (with 10:1 read/write ratio)
- 1KB per request × 1B requests/day ≈ 1TB/day
- 99.9% availability ≈ 8.76 hours downtime/year; 99.99% ≈ 52 minutes

---
- Foundation for [[scalable-architecture]] — the output of a system design interview
- Related to [[load-balancer]] — a component you must justify
- Related to [[database-replication]] — a scaling choice you must explain
- Related to [[cache-strategy]] — a performance optimization to discuss
- Related to [[observability]] — metrics to monitor the designed system
- Complementary to [[technical-interview]] — system design tests architecture/scale, technical interviews test algorithms/PoC