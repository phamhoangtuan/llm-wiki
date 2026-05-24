---
title: "Scalable Architecture"
type: concept
tags: [system-design, scalability, architecture, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [scaling-strategy, distributed-architecture]
---

## Summary

A scalable architecture is a system design that can handle growing load by adding resources rather than requiring complete redesign. The canonical evolution path: single server → separated tiers → vertical scaling → horizontal scaling with distributed components.

## The Evolution Path

### Stage 1: Single Server
```
User → DNS → [Web Server + Database + Cache] → Response
```
Everything runs on one machine. Simple, but has a hard ceiling.

### Stage 2: Separation of Tiers
Split web tier and data tier onto separate servers so each can scale independently.

### Stage 3: Vertical Scaling (Scale Up)
Add CPU/RAM to existing servers. Simple but hits hardware limits, creates SPOF, requires downtime.

### Stage 4: Horizontal Scaling (Scale Out)
Add more servers to a pool. Theoretically unlimited, enables high availability and fault tolerance — but requires load balancers, stateless design, and data consistency solutions.

## Scaling Strategies Compared

| Strategy | Definition | Pros | Cons |
|----------|-----------|------|------|
| Vertical | More CPU/RAM per server | Simple, no architecture changes | Hardware ceiling, SPOF, downtime |
| Horizontal | More servers in pool | Unlimited theoretically, HA, fault tolerance | Complex: LB, state, consistency |

> **Lesson**: Horizontal scaling is the only path to massive scale. But it demands solving new problems: load balancing, state management, and data consistency.

---
- Core to [[system-design-interview]] — the target output of the interview
- Foundation for [[load-balancer]] — required for horizontal scaling
- Foundation for [[database-replication]] — scales the data tier
- Foundation for [[stateless-architecture]] — prerequisite for horizontal scaling
- Related to [[cache-strategy]] — caching reduces backend load as you scale
- Related to [[cdn]] — global distribution at scale
- Related to [[message-queue]] — decouples components for independent scaling
- Related to [[observability]] — monitor everything as complexity grows