---
title: "Stateless Architecture"
type: concept
tags: [system-design, scalability, sessions, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [stateless-web-tier, shared-nothing-architecture]
---

## Summary

A stateless architecture stores session data in a shared external store (Redis, database, or NoSQL) rather than on individual web servers. This enables any server to handle any request, which is a prerequisite for horizontal scaling, autoscaling, and simple failover.

## Stateful vs Stateless

| Aspect | Stateful | Stateless |
|--------|----------|-----------|
| Session storage | Local server memory | Shared external store (Redis, DB) |
| Routing requirement | Sticky sessions (user → same server) | Any server can handle any request |
| Scaling | Hard — must migrate sessions | Easy — just add/remove servers |
| Failover | Complex — session data may be lost | Simple — route to any healthy server |
| Autoscaling | Impractical | Native — add servers when load increases |

## Stateless Flow

```
User Request → Load Balancer → [Any Web Server]
  ↓
Fetch session from Redis → Process → Return
```

## Shared Session Store Options

| Store | Best For |
|-------|----------|
| Redis | In-memory speed; ideal for session caching |
| Memcached | Simple key-value; good for ephemeral data |
| Database | Durability requirements; slower but persistent |
| JWT (client-side) | No server storage; token contains session state |

> **Key insight**: Autoscaling becomes viable only with stateless architecture. The system automatically adds servers when traffic increases and removes them when it decreases — zero manual intervention.

---
- Foundation for [[scalable-architecture]] — enables horizontal scaling
- Related to [[load-balancer]] — any server can receive any request
- Related to [[cache-strategy]] — session data often stored in cache tier
- Related to [[database-replication]] — session store may itself be replicated