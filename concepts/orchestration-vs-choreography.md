---
title: "Orchestration vs Choreography"
type: concept
tags: [microservices, architecture, system-design, distributed-systems]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [microservice orchestration, microservice choreography]
---

Two competing patterns for coordinating interactions between microservices. Neither is universally better — the choice depends on the workflow's complexity and reliability requirements.

## Comparison

| Property | Orchestration 🎼 | Choreography 💃 |
|----------|-----------------|-----------------|
| Control | Centralized orchestrator manages all interactions | Decentralized — services react to events independently |
| Debugging | Easy — single place to trace workflow | Hard — events scattered across services |
| Transaction Boundaries | Clear — orchestrator defines scope | Fuzzy — eventual consistency |
| Latency | Higher — central coordinator adds hop | Lower — direct service-to-service communication |
| Resilience | Single point of failure (the orchestrator) | More resilient — no central dependency |
| Complexity | Centralized logic, simple services | Distributed logic, complex debugging |

## When to Use Each

**Orchestration**: Complex business workflows requiring explicit transaction boundaries, audit trails, and clear error handling (e.g., order processing with payment, inventory, shipping).

**Choreography**: Event-driven systems where services react independently, low latency matters, and eventual consistency is acceptable (e.g., real-time notifications, analytics pipelines).

## Real-World Example

An e-commerce checkout:
- **Orchestration**: A `CheckoutService` calls `PaymentService`, then `InventoryService`, then `ShippingService` — with compensation (rollback) on failure at any step.
- **Choreography**: `OrderPlaced` event triggers `PaymentService` and `InventoryService` independently; each emits its own completion events; `ShippingService` listens for both completions.

---
- Builds on [[message-queue]] — choreography often uses message queues for event propagation
- Contrast with [[apache-kafka]] — Kafka enables choreographed systems through event streaming
- Foundation for [[system-design-interview]] — microservice coordination is a core design question