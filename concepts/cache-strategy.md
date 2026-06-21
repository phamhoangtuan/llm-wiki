---
title: "Cache Strategy"
type: concept
tags: [system-design, performance, caching, scalability]
created: 2026-05-24
updated: 2026-06-21
sources: [system-design-interview-xu, system-design-big-archive]
aliases: [caching, cache-tier, read-through-cache]
---

## Summary

A cache is temporary in-memory storage for frequently accessed data. Proper caching can reduce database load by 90%+ and cut response times from hundreds of milliseconds to single-digit milliseconds. But caching introduces complexity: stale data, invalidation, and consistency challenges.

## Read-Through Cache Pattern

```
1. Web server checks cache
2. Hit? → Return immediately
3. Miss? → Query database → Save result to cache → Return to client
```

## Key Considerations

| Concern | Solution |
|---------|----------|
| **Expiration** | Set TTL: too long → stale data; too short → constant DB load |
| **Consistency** | Hard to sync cache and DB, especially across multiple regions |
| **Eviction** | When cache is full: LRU (Least Recently Used), LFU (Least Frequently Used), or FIFO |
| **SPOF** | Use multiple cache servers across data centers; overprovision memory |

## Cache Invalidation Strategies

| Strategy | How It Works | Trade-off |
|----------|--------------|-----------|
| TTL expiration | Data expires after set time | Simple but may serve stale data |
| Active invalidation | Application deletes cache entry on write | More consistent but adds complexity |
| Versioned URLs | `image.jpg?v=2` forces fetch of new version | CDN-friendly but requires URL management |

> **Hard problems in computer science**: Cache invalidation, naming things, and off-by-one errors.

---
- Core to [[scalable-architecture]] — reduces database load dramatically
- Related to [[database-replication]] — cache + replication = massive read scaling
- Related to [[cdn]] — CDN is a specialized geographic cache for static content
- Related to [[load-balancer]] — cache deployed behind load balancer
- Foundation for [[redis]] — Redis is the most common high-performance caching backend
- Related to [[bloom-filter]] — bloom filters protect caches from miss storms by filtering non-existent keys