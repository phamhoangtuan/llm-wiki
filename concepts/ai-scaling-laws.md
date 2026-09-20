---
title: "AI Scaling Laws"
type: concept
tags: [machine-learning, scaling, compute, performance]
created: 2026-07-13
updated: 2026-07-13
sources: [introduction-to-machine-learning-systems]
aliases: [scaling-laws, neural-scaling-laws]
---

## Summary

**AI Scaling Laws** describe predictable relationships between model performance and three key resources: **data size**, **model size** (parameters), and **compute** (FLOPs). They enable engineers to forecast training outcomes before investing resources, avoiding over-investment in diminishing returns.

## The Core Relationship

Performance improves as a power law with scale: more data, more parameters, and more compute all help — but with predictable diminishing returns. Understanding these curves tells you when doubling compute yields only a 0.1% accuracy gain, making optimization techniques (pruning, quantization) a better investment.

## Practical Applications

| Application | How Scaling Laws Help |
| --- | --- |
| **Budget planning** | Estimate compute cost for target accuracy before training |
| **Architecture decisions** | Choose model size based on available data, not just ambition |
| **Diminishing returns detection** | Know when to stop scaling and instead optimize elsewhere |
| **Transfer learning strategy** | Decide between training from scratch vs. fine-tuning based on data volume |

## Key Trade-offs

Scaling laws expose the tension between accuracy and efficiency. A 1% accuracy gain isn't worth a 10x latency increase in production — the laws help quantify exactly when the trade-off flips. Combined with [[sustainable-ai|carbon-aware engineering]], they guide decisions about when larger models are justified.

---

- Informs [[machine-learning-systems]] — scaling laws are a core tool in performance engineering (Part III of the framework)
- Related to [[model-distillation]] — when scaling laws show diminishing returns, distillation offers a better path
- Related to [[sustainable-ai]] — scaling laws help quantify the carbon cost of marginal accuracy gains
- Benchmark source: [[sources/introduction-to-machine-learning-systems]] — Reddi covers scaling laws in Part III (Performance Engineering)
