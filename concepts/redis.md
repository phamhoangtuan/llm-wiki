---
title: "Redis"
type: concept
tags: [caching, performance, databases, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: []
---

Redis is an in-memory data structure store that achieves extreme throughput (100K+ requests/second) through a combination of architectural choices.

## Why Redis Is Fast

**RAM-Based Storage**: Memory access is ~1000× faster than disk. All data lives in RAM with periodic persistence to disk.

**Single-Threaded Execution Loop**: One thread processes all commands — no context switching overhead, no locking, no contention. Simple and predictable.

**IO Multiplexing**: Uses `epoll` (Linux) / `kqueue` (macOS) to handle thousands of concurrent connections with a single thread. Non-blocking event loop checks which connections have data ready.

### Blocking vs Non-Blocking IO

```
❌ Traditional blocking I/O:
for request in requests:
    result = process(request)      # Blocks until done
    send_response(result)

✅ Redis-style IO multiplexing:
ready = select(requests, timeout=0)
for request in ready:
    result = process_non_blocking(request)
    if result_ready:
        send_response(result)
```

**Efficient Data Structures**: Simple Dynamic Strings (SDS), Skip List, and specialized structures optimized for in-memory access patterns.

## Key Use Cases

- **Caching**: Store frequent query results to reduce database load
- **Session Store**: Fast, TTL-supported session management
- **Rate Limiting**: Atomic increment operations with expiry
- **Message Broker**: Pub/sub and stream data structures (Redis Streams)

---
- Foundation for [[cache-strategy]] — Redis is the most common caching backend
- Contrast with [[apache-kafka]] — Redis for low-latency cache, Kafka for high-throughput event streaming
- Foundation for [[system-design-interview]] — caching layer questions almost always involve Redis