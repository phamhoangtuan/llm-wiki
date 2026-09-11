---
title: "Geospatial Indexing"
type: concept
tags: [databases, geospatial, indexing, system-design]
created: 2026-06-29
updated: 2026-06-29
sources: [system-design-interview-volume-2]
aliases: [spatial-indexing, 2d-to-1d-mapping]
---

Geospatial indexing solves a fundamental dimensionality mismatch: standard database indexes (B-trees, hash indexes) are 1-dimensional, but location data exists in 2-dimensional space (latitude + longitude). The solution is mapping 2D coordinates into a 1D representation that enables efficient single-index lookups.

## The Problem: Naive SQL Fails at Scale

```sql
-- BROKEN at scale:
SELECT business_id FROM business
WHERE latitude  BETWEEN {:lat} - radius AND {:lat} + radius
  AND longitude BETWEEN {:long} - radius AND {:long} + radius
```

Why this fails:
- Standard indexes are 1-dimensional — they sort by a single key
- A 2D search requires intersecting two massive datasets (latitude range ∩ longitude range)
- The database must scan millions of rows in memory to compute the intersection
- Query latency degrades linearly (or worse) with data volume

## The Solution: 2D → 1D Mapping

Map the 2D coordinate space onto a 1D line — enabling traditional index structures to work efficiently. Two main strategies:

| Strategy | Approach | Storage | Best For |
|----------|----------|---------|----------|
| [[geohash]] | Recursive grid subdivision → base32 string prefix match | Database | Persistence, SQL compatibility |
| [[quadtree]] | Adaptive tree subdivision into 4 quadrants | In-memory | Speed, cache layer |

## Key Insight

> Proximity service is not `SELECT * WHERE lat/long BETWEEN`. It's the art of mapping 2D coordinates into 1D index to find k-nearest neighbors at 200M+ scale with millisecond latency.

Recommended approach: **Hybrid** — Quadtree for in-memory cache (speed) + Geohash for database index (persistence). Each optimizes for its environment: Quadtree exploits RAM speed and adaptive density, Geohash leverages SQL string prefix matching and durability.

---

- Foundation for [[proximity-service]] — the architecture that depends on spatial indexing
- Implemented by [[geohash]] — database-level encoding via base32 string prefix matching
- Implemented by [[quadtree]] — in-memory adaptive tree structure for spatial subdivision
- Related to [[system-design-interview]] — a core design pattern in system design interviews
