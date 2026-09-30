---
title: "Bloom Filter"
type: concept
tags: [data-structures, algorithms, caching, system-design, probabilistic]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: []
---

A Bloom filter is a space-efficient probabilistic data structure for set membership testing. Its defining characteristic: it can tell you something is **definitely not** in a set, but only **probably** in a set.

## How It Works

- Returns "false" → element is **definitely** NOT in the set ✅
- Returns "true" → element is **probably** in the set (false positives possible) ⚠️
- **No false negatives** — if something is in the set, it will never say it isn't

The filter uses multiple hash functions to set bits in a bit array. Adding an element sets k bits; checking involves verifying all k bits are set. If any bit is 0, the element was never added. If all bits are 1, the element may have been added (or other elements happened to set the same bits).

## Key Use Cases

### Cache Miss Prevention
```
bloom = BloomFilter(capacity=1000000, error_rate=0.01)

def get_from_cache(key):
    if not bloom.contains(key):
        return None              # Skip expensive DB query — definitely not there
    result = cache.get(key) or db.get(key)
    if result:
        bloom.add(key)
    return result
```

This prevents cache miss attacks where queries for non-existent keys hammer the database. The bloom filter acts as a cheap first line of defense.

### URL Deduplication
Google-scale web crawlers use bloom filters to avoid crawling the same URL twice. When processing billions of URLs, storing every seen URL in a set is infeasible — bloom filters trade a small false positive rate for massive space savings.

## Trade-off

- Space efficiency: a few bits per element vs storing full keys
- Configurable false positive rate: more bits = fewer false positives
- Cannot remove elements (standard variant) — use Counting Bloom Filter for deletions

---
- Foundation for [[cache-strategy]] — bloom filters protect caches from miss storms
- Foundation for [[system-design-interview]] — common advanced component in design questions