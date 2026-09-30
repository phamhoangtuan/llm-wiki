---
title: "CDN"
type: concept
tags: [system-design, networking, performance, global-scale]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [content-delivery-network, edge-cache]
---

## Summary

A Content Delivery Network (CDN) is a geographically distributed network of servers that cache static content (images, CSS, JavaScript, videos) close to end users. By serving content from edge locations rather than origin servers, CDNs reduce latency, save bandwidth, and improve availability.

## How It Works

```
User request → CDN edge server (nearest location)
  ↓
Cache hit? → Serve immediately
Cache miss? → Fetch from origin → Cache locally → Serve
```

## Key Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **TTL (Time-to-Live)** | Origin server specifies how long assets can be cached before refetching |
| **Invalidation** | Purge cache before TTL expires via API or versioned URLs (`image.jpg?v=2`) |
| **Geo-distribution** | Edge servers located in major cities worldwide — reduces RTT from 200ms+ to <20ms |
| **Origin shield** | A single CDN server fetches from origin and distributes to other edges — reduces origin load |

## When to Use

| Use CDN For | Don't Use CDN For |
|-------------|-------------------|
| Static assets (images, CSS, JS, fonts) | Dynamic content that changes per user |
| Video streaming (HLS/DASH segments) | Personalized API responses |
| Software downloads | Real-time data (WebSockets) |
| Large file distribution | Content behind authentication walls |

---
- Related to [[cache-strategy]] — CDN is a specialized geographic cache
- Related to [[scalable-architecture]] — global distribution at scale
- Related to [[load-balancer]] — CDN also performs geo-based traffic routing
- Related to [[message-queue]] — can cache and distribute large payloads