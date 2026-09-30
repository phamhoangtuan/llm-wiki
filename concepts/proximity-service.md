---
title: "Proximity Service"
type: concept
tags: [system-design, geospatial, scalability, architecture]
created: 2026-06-29
updated: 2026-06-29
sources: [system-design-interview-volume-2]
aliases: [location-based-service, nearby-search]
---

Proximity service architecture enables users to discover nearby points of interest (businesses, people, locations) based on their latitude/longitude. It's one of the canonical system design problems — powering Yelp, Google Maps, Uber, and Tinder. The core challenge is not a simple `SELECT * WHERE lat/long BETWEEN` query; it's the art of mapping 2D coordinates to a 1D index to find k-nearest neighbors at scale.

## Three Core Functions

| Function | Description | Requirements |
|----------|-------------|-------------|
| Location-Based Search | Find all businesses within a radius from a lat/long point | Low latency, geospatial indexing |
| Business Lifecycle (CRUD) | Create, update, delete business listings | Low QPS writes, data consistency |
| Metadata Retrieval | Read detailed business profiles (images, reviews, ratings) | High-frequency reads, cache optimization |

## Two-Service Architecture

```
┌────────────────────────────────────────────────────┐
│               Load Balancer (DNS)                   │
│         Path-based routing: /v1/* → Services        │
└──────────┬──────────────────────┬───────────────────┘
           ▼                      ▼
┌──────────────────────┐  ┌──────────────────────┐
│  Location-Based      │  │   Business Service   │
│  Service (LBS)       │  │                      │
│  • Read-heavy        │  │  • CRUD operations   │
│  • Stateless         │  │  • Low-QPS writes    │
│  • Geospatial queries│  │  • High-QPS reads    │
│  • Elastic scaling   │  │  • Metadata retrieval│
└──────────────────────┘  └──────────────────────┘
```

Separation benefits: resource isolation, independent scaling, specialized optimization, failure containment.

## Strategic Compromise: Data Freshness SLA

A key architectural decision — relaxing data freshness from real-time to **next-day SLA** dramatically simplifies the system:

| Trade-off | Benefit |
|-----------|---------|
| Accept 24-hour staleness | Nightly batch jobs for index/cache rebuilds |
| Skip real-time cache invalidation | Avoid thundering herd problem |
| No instant update propagation | Simpler write path, no real-time sync |

## Scale Estimation

**QPS Formula** (using `10^5` = 100,000 seconds/day shortcut):
```
QPS = (DAU × Average Actions) / 10^5
```

Example: 100M DAU × 5 searches/user/day → 500M queries/day → **5,000 QPS baseline**.

This dictates the architecture: stateless services, database replicas, caching layers.

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Stateless LBS | Elastic scaling, simple load balancing, no sticky sessions |
| Primary-Secondary DB cluster | Read >> Write workload, horizontal read scaling |
| In-memory Quadtree + DB Geohash | Speed (cache) + persistence (DB) hybrid approach |
| Next-day freshness SLA | Simpler write path, avoids cache stampede risk |
| Incremental rollouts | Prevents database overload when rebuilding in-memory index |

---

- Core to [[geospatial-indexing]] — the indexing strategy that makes proximity search scalable
- Foundation for [[geohash]] — database-level geospatial encoding with prefix matching
- Foundation for [[quadtree]] — in-memory adaptive spatial subdivision
- Uses [[database-replication]] — Primary-Secondary clustering for read-optimized workloads
- Uses [[stateless-architecture]] — stateless LBS enables elastic scaling
- Uses [[cache-strategy]] — cache stampede mitigation for nightly index rebuilds
- Uses [[deployment-strategies]] — incremental rollout over Blue/Green for index initialization
- Part of [[system-design-interview]] — a canonical system design interview problem
- Related to [[scalable-architecture]] — QPS estimation drives architecture decisions
