---
title: "Message Queue"
type: concept
tags: [system-design, messaging, async, decoupling, resilience]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [message-broker, event-queue, task-queue]
---

## Summary

A message queue is an asynchronous communication mechanism that decouples producers (services that create jobs) from consumers (services that process jobs). By introducing a buffer between components, message queues enable independent scaling, failure resilience, and load leveling.

## Architecture

```
Producer → [Message Queue] → Consumer 1
                         → Consumer 2
                         → Consumer 3
```

| Role | Responsibility |
|------|--------------|
| **Producer** | Publishes jobs into the queue (e.g., "process this image") |
| **Queue** | Durable buffer that holds jobs until consumed |
| **Consumer** | Worker nodes that pick up and process jobs |

## Benefits

| Benefit | Description |
|---------|-------------|
| **Independent scaling** | Add workers when queue is long; remove when empty |
| **Failure resilience** | If a worker dies, the job remains in queue — another worker picks it up |
| **Load leveling** | Producers aren't blocked waiting for jobs to finish; fast response times |
| **Temporal decoupling** | Producers and consumers don't need to be online simultaneously |

## Common Implementations

| Tool | Pattern | Best For |
|------|---------|----------|
| RabbitMQ | Traditional message broker | Complex routing, pub/sub |
| Kafka | Distributed log | High throughput, event sourcing |
| SQS | Managed cloud queue | AWS ecosystem, simple ops |
| Redis Streams | Lightweight queue | Low latency, simple use cases |

---
- Core to [[scalable-architecture]] — decouples components for independent scaling
- Related to [[stateless-architecture]] — async processing complements stateless design
- Related to [[observability]] — queue depth and consumer lag are critical metrics
- Related to [[load-balancer]] — workers scale independently from web tier