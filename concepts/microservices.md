---
title: "Microservices"
type: concept
tags: [architecture, microservices, cloud-native, distributed-systems, clean-code]
created: 2026-06-27
updated: 2026-06-27
sources: [clean-code-principles-patterns-silen]
aliases: [microservices-architecture, autopilot-microservices]
---

## Summary

**Microservices** is an architectural style where an application is composed of small, independent services — each with a single responsibility, running in its own process, and communicating via lightweight APIs. The goal is to create services that operate like "autopilot" vehicles: stateless, resilient, and highly available without manual intervention.

## Core Principles

### Single Responsibility at Every Level

SRP applies recursively across architectural layers:

| Level | Responsibility |
| --- | --- |
| **System** | One overarching purpose |
| **Application** | One core business domain |
| **Microservice** | One specific responsibility within its bounded context |

A service handling orders should not also manage inventory or send notifications — those are separate bounded contexts with their own services.

### Autopilot Microservices

Each service should operate like a self-driving car — no human babysitting:

- **Stateless**: No local state storage. State lives in external data stores. Enables horizontal scaling (spin up N instances, any can handle any request).
- **Resilient**: Self-healing on failure. Circuit breakers, retries with backoff, graceful degradation.
- **Highly Available**: Designed for continuous operation. Redundancy, failover, health checks.

### Reducing Coupling

Loose coupling is the architecture's primary defense against [[software-rot]]:

| Technique | Description |
| --- | --- |
| **Encapsulation** | Hide internal implementation; expose only public APIs. Database schemas are private to each service. |
| **Facade Pattern** | Aggregate multiple lower-level services behind a simplified interface for higher-level consumers |
| **[[domain-driven-design | Domain-Driven Design]]** | Partition the system into subdomains and bounded contexts. Code speaks the business's ubiquitous language. |

> Example: Service "Order" needs inventory data → calls Inventory API, never accesses Inventory's database directly. Schema changes in Inventory don't touch Order code.

## Communication Patterns

Microservices communicate via well-defined interfaces:

| Pattern | Use Case |
| --- | --- |
| **Synchronous (REST/gRPC)** | Request-response when caller needs immediate answer |
| **Asynchronous ([[message-queue]])** | Fire-and-forget; decouple producer from consumer timing and availability |
| **Event-driven** | Services emit events; interested services subscribe |

Synchronous creates temporal coupling (caller waits). Asynchronous and event-driven enable greater independence but add eventual consistency complexity. See [[orchestration-vs-choreography]] for coordination patterns.

## Trade-offs

| Benefit | Cost |
| --- | --- |
| Independent deployability | Network latency between services |
| Technology diversity (right tool per service) | Operational complexity (more moving parts) |
| Fault isolation (one service down ≠ system down) | Distributed debugging (traces span services) |
| Team autonomy (small teams own services) | Data consistency challenges (no cross-service transactions) |

Microservices are not a default choice — they solve organizational scaling problems. A monolith is often the right starting point until team size or independent scaling demands emerge.

## Relationship to Other Patterns

- **[[stateless-architecture]]**: Microservices must be stateless to scale horizontally
- **[[middleware-pattern]]**: Cross-cutting concerns (auth, logging, rate limiting) applied consistently across services
- **[[deployment-strategies]]**: Independent deployability enables blue-green, canary, and rolling deployments per service
- **[[containerization]]**: Docker provides the isolation boundary for microservice processes
- **[[orchestration-vs-choreography]]**: Two competing patterns for coordinating microservice workflows
- **[[api-architectural-styles]]**: REST, gRPC, and GraphQL are the communication protocols that connect microservices
- **[[observability]]**: Distributed tracing across services is mandatory for debugging microservice systems

---

- Enabled by [[stateless-architecture]] — horizontal scaling demands stateless design
- Uses [[middleware-pattern]] — consistent cross-cutting concerns across all services
- Requires [[observability]] — distributed tracing essential for debugging multi-service systems
- Benefits from [[deployment-strategies]] — independent deployability enables risk-managed releases
- Implemented via [[containerization]] — Docker isolates each service's runtime
- Coordinates via [[orchestration-vs-choreography]] — two patterns for service workflow management
- Communicates through [[api-architectural-styles]] — REST, gRPC, GraphQL as inter-service protocols
- Uses [[message-queue]] — asynchronous decoupling between services
- Grounded in [[solid-principles]] — SRP at the service level is the architectural translation of class-level SRP
- Informed by [[domain-driven-design]] — bounded contexts define service boundaries
- Countered by [[software-rot]] — loose coupling is the defense against degradation spreading across services
- Balances [[architectural-characteristics]] — scalability and deployability are the -ilities that justify microservices
- Benchmark source: [[sources/clean-code-principles-patterns-silen]] — Silén's microservices architecture chapter
