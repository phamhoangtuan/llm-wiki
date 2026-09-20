---
title: "System Design: The Big Archive"
type: source
source_type: book
author: "Alex Xu"
url: ""
source_date: 2026-06-21
ingested: 2026-06-21
tags: [system-design, cloud, security, performance, databases, architecture]
concepts: [cloud-service-models, containerization, deployment-strategies, database-isolation, database-sharding, sso, password-storage, tls-https, redis, apache-kafka, orchestration-vs-choreography, api-architectural-styles, http-evolution, bloom-filter, snowflake-id, message-delivery-semantics, system-design-interview, cache-strategy, message-queue]
created: 2026-06-21
updated: 2026-06-21
---

# System Design: The Big Archive

**Author**: Alex Xu | **Type**: Ebook | **Pages**: 159 | **Finished**: 2026-06-21

Comprehensive system design guide covering cloud infrastructure, containerization, deployment strategies, database internals, security, performance optimization, and architecture patterns. Vietnamese notes with code examples.

---

## Key Sections

### 1. Cloud Infrastructure — IaaS, PaaS, SaaS
Three cloud service models representing increasing levels of abstraction: IaaS (infrastructure rental, you manage OS+), PaaS (platform for developer velocity, provider manages runtime), SaaS (zero operational overhead, provider manages everything). Core insight: each level trades control for operational simplicity.

### 2. Virtualization vs Containerization
Virtualization uses hypervisors to partition physical hardware into VMs with guest OSes. Containerization packages code with dependencies into isolated units that share the host OS kernel — no guest OS boot needed. Containers start in ~100ms vs ~30s for VMs. Modern production uses "Containerized on Virtualized" for security isolation + deployment agility.

### 3. Deployment Strategies
- **Blue-Green**: Two identical environments, switch traffic after verification. Best rollback safety, double infrastructure cost.
- **Canary**: Gradual rollout (5% → 20% → 100%). Cost-effective, early failure detection.
- **A/B Testing**: Run versions simultaneously, measure user response. For product experiments, not infrastructure stability.
- **Multi-Service**: Simultaneous changes. Simple but low rollback safety.

### 4. Database Systems
- **Isolation Levels**: Serializable (highest, sequential), Repeatable Read (consistent with tx start), Read Committed (post-commit visibility, PostgreSQL default), Read Uncommitted (dirty reads, rarely used).
- **Sharding**: Vertical (column split) vs Horizontal (row split). Hash-based (even distribution, hard range queries) vs Range-based (easy ranges, hotspot risk).
- **Optimistic Locking**: Version-number concurrency control — check version before update, retry on conflict. Best when conflicts are rare.

### 5. Security & Authentication
- **SSO**: 4-step workflow — intercept unauthenticated request, establish global session, token handover, cross-domain propagation. Neutralizes password fatigue.
- **Password Storage**: Salting mandatory — unique random string per user, hash(password + salt). Salt stored plaintext; not a secret, only prevents rainbow table attacks.
- **TLS/HTTPS**: 3-step handshake — negotiation (cipher suite), asymmetric encryption (key exchange via public key), symmetric encryption (fast, bidirectional data transmission).

### 6. Performance Optimization
- **Redis**: RAM-based (~1000× faster than disk), single-threaded event loop, IO multiplexing (epoll/kqueue), efficient data structures (SDS, Skip Lists).
- **Kafka**: Sequential I/O minimizes disk seek, Zero Copy (`sendfile()`) bypasses application context — 65% reduction in delivery time.
- **SSD vs HDD**: SSD ~5× faster reads/writes, ~100× faster seek time (0.1ms vs 10ms), supports parallelism via multiple flash particles.

### 7. Architecture Patterns
- **Orchestration vs Choreography**: Orchestration uses centralized coordinator (easy debug, single point of failure). Choreography is decentralized event-driven (resilient, harder to debug).
- **API Styles**: SOAP (XML, enterprise), REST (resource-driven, most modern apps), GraphQL (client-specified queries, mobile), gRPC (Protocol Buffers, internal microservices).
- **HTTP Evolution**: HTTP/1.0 (per-request TCP), HTTP/1.1 (persistent connections), HTTP/2.0 (multiplexing, header compression), HTTP/3.0 over QUIC (UDP-based, eliminates transport-layer HOL blocking).

### 8. Advanced Concepts
- **Bloom Filters**: Probabilistic set membership — "false" means definitely absent, "true" means probably present. Use cases: URL dedup at scale, cache miss prevention.
- **Snowflake ID**: 64-bit unique ID: 41-bit timestamp + 10-bit machine ID + 12-bit sequence. Roughly time-sorted, efficient indexing.
- **Message Delivery Semantics**: At-most once (may lose, never duplicate), At-least once (no loss, may duplicate), Exactly once (no loss, no duplicates — typically achieved via at-least-once + idempotent consumers).

---

## Core Message

> System design is not about finding "the right answer." It's the art of balancing trade-offs — between latency and consistency, complexity and scalability, security and usability.

---

## Connections

- Foundation for [[system-design-interview]] — shares the scalability framework from single server to millions of users
- Extends [[database-sharding]] — hash-based vs range-based sharding strategies
- Extends [[apache-kafka]] — zero copy, sequential I/O performance internals
- Extends [[message-queue]] — delivery semantics: at-most, at-least, exactly once
- Extends [[cache-strategy]] — Redis as high-performance caching layer
