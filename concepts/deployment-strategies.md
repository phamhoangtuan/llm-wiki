---
title: "Deployment Strategies"
type: concept
tags: [deployment, devops, system-design, reliability]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
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

## Rule of Thumb

> Stakes determine strategy tightness. Financial transactions → Blue-Green. Weekend hackathon → Multi-Service is fine.

---
- Builds on [[containerization]] — containers enable fast environment switching
- Foundation for [[scalable-architecture]] — zero-downtime deploys are prerequisite for scaling
- Foundation for [[system-design-interview]] — deployment architecture questions are common