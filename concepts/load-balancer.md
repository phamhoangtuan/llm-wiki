---
title: "Load Balancer"
type: concept
tags: [system-design, networking, high-availability, scalability]
created: 2026-05-24
updated: 2026-05-24
sources: [system-design-interview-xu]
aliases: [reverse-proxy, traffic-distributor]
---

## Summary

A load balancer is a reverse proxy that distributes incoming traffic across multiple backend servers. It acts as the "traffic cop" of a distributed system — ensuring no single server becomes a bottleneck while providing security and high availability.

## Benefits

| Benefit | Mechanism |
|---------|-----------|
| Traffic distribution | Routes requests evenly across healthy servers |
| Security | Exposes only the LB's public IP; backend servers use private IPs |
| High availability | Automatically redirects traffic away from failed servers |
| SSL termination | Offloads encryption/decryption from backend servers |
| Session persistence | Can route users to the same server (sticky sessions) if needed |

## Algorithms

| Algorithm | Behavior | Best For |
|-----------|----------|----------|
| Round Robin | Sequential distribution | Equal-capacity servers |
| Least Connections | Routes to server with fewest active connections | Variable request durations |
| IP Hash | Consistent hashing on client IP | Session affinity requirements |
| Weighted | Assigns different capacities to different servers | Heterogeneous hardware |

---
- Core to [[scalable-architecture]] — required for horizontal scaling
- Foundation for [[stateless-architecture]] — enables routing to any server
- Related to [[database-replication]] — routes reads to slave replicas
- Related to [[cache-strategy]] — sits in front of cache tier
- Related to [[cdn]] — CDN edge servers also perform geo-based routing