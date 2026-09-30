---
title: "Message Delivery Semantics"
type: concept
tags: [distributed-systems, messaging, system-design, reliability]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [at-most-once, at-least-once, exactly-once]
---

Message delivery semantics define the guarantees a messaging system provides about whether messages are delivered, and whether they can be duplicated. The right choice depends on the business impact of data loss vs duplication.

## Three Semantics

| Semantic | Guarantee | Use Cases | Trade-offs |
|----------|-----------|-----------|------------|
| At-most once 📉 | Messages may be lost, never duplicated | Metrics, logging, non-critical analytics | ✅ Low overhead ❌ Data loss acceptable |
| At-least once 📈 | No messages lost, duplicates may occur | Order processing, user notifications | ✅ Reliable delivery ❌ Need deduplication logic |
| Exactly once 🎯 | No loss, no duplicates | Financial transactions, inventory updates | ✅ Perfect consistency ❌ Complex + expensive |

## The "Exactly Once" Illusion

True "exactly once" delivery is theoretically impossible in distributed systems (due to the Two Generals Problem). In practice, it's achieved through a design pattern:

> **at-least-once delivery + idempotent consumers = effectively exactly once**

The messaging system guarantees delivery (at-least-once), and the consumer ensures processing each message has the same effect whether executed once or multiple times (idempotency).

## Idempotency Strategies

- **Deduplication keys**: Consumer tracks processed message IDs, skips duplicates
- **Idempotent operations**: `SET balance = 100` (not `balance += 100`)
- **Transaction boundaries**: Process message + record dedup key in single DB transaction

## Choosing the Right Semantic

Ask: "What happens if this message is lost? What happens if it's processed twice?"

- Lost = acceptable, duplicate = bad → at-most once
- Lost = unacceptable, duplicate = manageable → at-least once + dedup
- Lost = unacceptable, duplicate = unacceptable → effectively exactly once (at-least-once + idempotent)

---
- Builds on [[message-queue]] — delivery semantics are configured at the queue level
- Foundation for [[orchestration-vs-choreography]] — choreographed systems depend on delivery guarantees for consistency
- Builds on [[apache-kafka]] — Kafka supports all three semantics through consumer configuration
- Foundation for [[system-design-interview]] — delivery semantics are central to distributed system reliability