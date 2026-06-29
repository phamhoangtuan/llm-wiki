---
title: "Deployment Strategies"
type: concept
tags: [deployment, devops, system-design, reliability]
created: 2026-06-21
updated: 2026-06-29
sources: [system-design-big-archive, system-design-interview-volume-2]
aliases: [Blue-Green deployment, Canary deployment]
---

Deployment is the highest-risk phase of the software lifecycle. A small bug can cause outages for millions of users. Strategy choice should match the stakes.

## Four Strategies

| Strategy | How It Works | Pros | Cons | Use When |
|----------|-------------|------|------|----------|
| Blue-Green 🟦🟩 | Two identical environments: Blue (staging) + Green (production). Switch traffic after verification | ✅ Best rollback safety ✅ Minimal downtime | ❌ Double infrastructure cost ❌ Complex synchronization | Production-critical systems, financial apps |
| Canary 🐤 | Upgrade gradually for subset users (5% → 20% → 100%) | ✅ Cost-effective ✅ Early failure detection | ❌ Testing in production required ❌ Complex observability | Large user bases, feature flagging |
| A/B Testing 🧪 | Different versions run simultaneously to measure user response | ✅ Data-driven decisions ✅ Feature experimentation | ❌ Not for infrastructure stability ❌ Risk of feature leaks | Product experiments, UX optimization |
| Multi-Service 🔗 | Simultaneous changes to multiple services | ✅ Simple to implement ✅ Fast for small teams | ❌ Low rollback safety ❌ High dependency risk | Small projects, non-critical updates |

## Incremental Rollout (In-Memory Indexes)

When services maintain large in-memory data structures (e.g., a [[quadtree]] built from 200M database rows), deployment strategy becomes critical:

- **Problem**: Blue/Green deployment spins up an entire fresh cluster — every new instance simultaneously fetches 200M businesses from the database to build its in-memory index. This can crash the database.
- **Solution (Incremental Rollout)**: New instances initialize gradually, one or a few at a time. Existing instances maintain capacity while newcomers build their indexes. No database overload.

| Strategy | Risk for In-Memory Index Rebuild |
|----------|----------------------------------|
| Blue-Green | High — entire cluster fetches data simultaneously |
| Incremental Rollout | Low — gradual initialization, database protected |

## Rule of Thumb

> Stakes determine strategy tightness. Financial transactions → Blue-Green. Weekend hackathon → Multi-Service is fine.

---
- Builds on [[containerization]] — containers enable fast environment switching
- Foundation for [[scalable-architecture]] — zero-downtime deploys are prerequisite for scaling
- Foundation for [[system-design-interview]] — deployment architecture questions are common
- Related to [[quadtree]] — in-memory index rebuild requires incremental rollout