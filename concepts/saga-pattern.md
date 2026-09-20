---
title: "Saga Pattern"
type: concept
tags: [distributed-systems, transactions, microservices, patterns]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Saga Pattern

A pattern for managing distributed transactions across multiple services without relying on distributed ACID transactions. Central to *Software Architecture: The Hard Parts* for "putting things back together" after decomposition.

## The Problem

In a monolith, a business operation spanning multiple tables can use a single ACID transaction. After decomposition into services, each service owns its own database — no single transaction can span services without sacrificing availability (CAP theorem).

## How Sagas Work

A saga breaks a distributed transaction into a sequence of local transactions, each with a compensating action for rollback:

```
Step 1: Reserve inventory → Compensating: Release inventory
Step 2: Charge payment    → Compensating: Refund payment
Step 3: Schedule shipping → Compensating: Cancel shipment
```

If any step fails, previously completed steps are rolled back via their compensating actions.

## Two Coordination Styles

- **Orchestration**: A central coordinator tells each service what to do and handles failure
- **Choreography**: Each service listens for events and acts independently; no central controller

## Trade-offs

| Aspect | Saga | ACID (Monolith) |
| --- | --- | --- |
| Consistency | Eventually consistent | Immediately consistent |
| Isolation | No isolation between steps | Full isolation |
| Availability | High (no distributed locks) | Lower under contention |
| Complexity | Higher (compensating logic) | Lower |

## Key Insight

Sagas acknowledge that perfect consistency is impossible in distributed systems and provide *pragmatic* eventual consistency.

---

## Connections

- [[orchestration-vs-choreography]] — Two coordination styles for sagas
- [[microservices]] — The architecture that creates the need for sagas
- [[cap-theorem]] — Why distributed ACID is impossible
- [[message-delivery-semantics]] — At-least-once delivery for saga steps
