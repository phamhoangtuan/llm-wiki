---
title: "HTTP Evolution"
type: concept
tags: [http, networking, protocol, web, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [HTTP/3, QUIC, HTTP/2, HOL blocking]
---

HTTP has evolved across four major versions, each solving a specific performance bottleneck. The central problem has always been Head-of-Line (HOL) blocking.

## Head-of-Line Blocking

When one request is delayed, all subsequent requests behind it are also blocked — like a single slow car holding up an entire lane of traffic. Each HTTP version addresses HOL blocking at a different layer.

## Version Progression

| Version | Key Features | Problem Solved |
|---------|-------------|----------------|
| HTTP/1.0 | Separate TCP connection per request | — (baseline) |
| HTTP/1.1 | Persistent connections, pipelining | Connection establishment overhead |
| HTTP/2.0 | Streams, multiplexing, header compression (HPACK) | Application-layer HOL blocking |
| HTTP/3.0 (QUIC) | UDP-based transport, streams at transport layer, 0-RTT handshake | Transport-layer HOL blocking |

## Key Transitions

**HTTP/1.0 → 1.1**: Persistent connections keep TCP alive between requests. Pipelining sends multiple requests without waiting for responses — but responses must arrive in order (still subject to HOL).

**HTTP/1.1 → 2.0**: Multiplexing allows multiple concurrent streams over one TCP connection. Requests and responses can interleave. However, a single lost TCP packet blocks ALL streams (transport-layer HOL).

**HTTP/2.0 → 3.0**: QUIC replaces TCP with UDP. Each stream is independent at the transport layer — a lost packet only blocks its own stream, not others. Also enables 0-RTT connection establishment for returning clients.

## Practical Impact

- HTTP/1.1: 6 parallel connections per domain (browser hack to work around HOL)
- HTTP/2: 1 connection, multiplexed — reduces connection overhead
- HTTP/3: Same multiplexing, but resilient to packet loss — critical for mobile networks

---
- Foundation for [[api-architectural-styles]] — gRPC uses HTTP/2 for multiplexed streaming
- Foundation for [[system-design-interview]] — protocol choice affects system latency and reliability