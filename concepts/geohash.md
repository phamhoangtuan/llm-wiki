---
title: "Geohash"
type: concept
tags: [geospatial, indexing, databases, algorithms]
created: 2026-06-29
updated: 2026-06-29
sources: [system-design-interview-volume-2]
aliases: [geohashing, spatial-hash]
---

Geohash is a geospatial indexing system that recursively subdivides the world into grids and encodes each grid as a base32 string. Longer strings represent smaller, more precise grid cells. The key property: points that are geographically close share a common prefix — enabling 2D proximity search via string prefix matching on a standard database index.

## How It Works

```
World → 2 partitions → 4 → 8 → ... → Grid cell identified by base32 string
```

Example:
- Geohash `u000` = grid containing La Roche-Chalais, France
- Geohash `ezzz` = grid containing Pomerol, France (~30km away)

Longer shared prefix = greater geographic proximity. A query becomes `LIKE 'u000%'` — a simple, index-friendly string operation.

## Precision Mapping

| Length | Grid Width × Height | Use Case |
|--------|---------------------|----------|
| 1 | 5,009.4 km × 4,992.6 km | Continental |
| 2 | 1,252.3 km × 624.1 km | Country |
| 3 | 156.5 km × 156 km | Regional |
| 4 | 39.1 km × 19.5 km | City |
| 5 | 4.9 km × 4.9 km | Neighborhood |
| 6 | 1.2 km × 609.4 m | Street |

## Advantages

- **Simple implementation**: Just string prefix matching in SQL (`LIKE 'prefix%'`)
- **Database-native**: Works with any database that supports string indexes
- **No special infrastructure**: Stored as a regular string column
- **Intuitive precision**: Longer string = smaller area = more precise

## The Boundary Issue (Critical Weakness)

Two physically adjacent locations can share **no common prefix** at all:

```
La Roche-Chalais: u000
Pomerol (30km away): ezzz
→ Shared prefix = NONE
→ LIKE 'u000%' query would MISS nearby results in 'ezzz'
```

This happens because grid boundaries are fixed and arbitrary — two points on opposite sides of a high-level grid partition will have completely different hash prefixes, even if they're meters apart.

**Solution**: Search all 8 neighboring grids in addition to the target grid. This ensures comprehensive results but adds query complexity and latency (9 queries instead of 1).

## Best Used For

- **Database-level indexing**: Persistence, SQL compatibility
- **Read-optimized workloads**: String prefix queries are fast with B-tree indexes
- **Coarse-grain filtering**: Narrow down candidates before finer-grained processing

Complement with [[quadtree]] for in-memory cache layer — the hybrid approach gives both speed and persistence.

---

- Core to [[geospatial-indexing]] — the database-level strategy for 2D → 1D mapping
- Core to [[proximity-service]] — powers location-based search at database level
- Complementary to [[quadtree]] — Geohash (database, persistence) + Quadtree (in-memory, speed)
- Related to [[system-design-interview]] — a core algorithm discussed in interviews
