---
title: "Quadtree"
type: concept
tags: [geospatial, data-structures, in-memory, algorithms]
created: 2026-06-29
updated: 2026-06-29
sources: [system-design-interview-volume-2]
aliases: [quad-tree, spatial-tree]
---

A Quadtree is an in-memory tree data structure that recursively subdivides 2D space into four quadrants — but only when a grid's business density exceeds a threshold (e.g., 100 businesses). This adaptive behavior creates granular grids in dense urban centers and large, efficient grids in sparse areas.

## How It Works

```
World → 4 quadrants → recurse into each quadrant
         ↓ only if business count > threshold
      → Subdivide further → leaf nodes store businesses
```

Unlike [[geohash]]'s fixed grid, Quadtree subdivision is **data-driven** — it adapts to actual business distribution. Manhattan gets deep subdivisions; the Sahara gets a single large grid.

## Memory Footprint ("Mic Drop" Calculation)

For 200 million businesses with a threshold of 100 businesses per leaf:

| Component | Nodes | Bytes/Node | Total Memory |
|-----------|-------|------------|-------------|
| Leaf nodes | 2,000,000 | ~832 bytes | ~1.66 GB |
| Internal nodes | ~666,000 | ~64 bytes | ~0.05 GB |
| **Total** | | | **~1.71 GB** |

The entire global business index fits on a **single server's RAM**. No distributed sharding needed for the index itself. Read-replicas are still needed for high QPS traffic volume, but not for index size.

## Advantages over Geohash

| Criterion | Quadtree | Geohash |
|-----------|----------|---------|
| Boundary issues | None (adaptive subdivision) | Yes (fixed grid boundaries) |
| Density adaptation | Automatic in dense/sparse areas | Fixed grid, uniform precision |
| Query speed | Faster (in-memory) | Fast (database index) |
| Memory | ~1.71 GB in RAM | Stored in database (disk) |
| Implementation | More complex (tree structure) | Simple (string prefix match) |

## Operational Challenges

**Index Rebuild Time**: Building the Quadtree from scratch (scanning 200M DB rows) takes several minutes — a problem during deployments:

- **Risk**: Blue/Green deployment where an entire fresh cluster fetches 200M businesses simultaneously could crash the database
- **Solution**: **Incremental rollouts** — new instances initialize gradually while maintaining service capacity

**Radius Expansion**: When a search returns insufficient results, traverse upward from the current leaf to its parent node, gathering businesses from the other three sibling quadrants. This intelligently expands the search area without user intervention.

## Best Used For

- **In-memory cache layer**: Speed for high-QPS queries
- **Adaptive density areas**: Cities with highly uneven business distribution
- **Zero boundary issues**: Fixed-grid edge cases are eliminated

Complement with [[geohash]] for database persistence — the hybrid approach gives both speed and durability.

---

- Core to [[geospatial-indexing]] — the in-memory strategy for 2D → 1D mapping
- Core to [[proximity-service]] — powers location-based search at the cache layer
- Complementary to [[geohash]] — Quadtree (in-memory, speed) + Geohash (database, persistence)
- Related to [[deployment-strategies]] — incremental rollouts prevent DB overload during index rebuild
- Related to [[system-design-interview]] — a core data structure discussed in interviews
