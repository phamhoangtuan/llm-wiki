---
title: "Model Pruning"
type: concept
tags: [llm, ml, optimization, compression, inference, production]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [pruning, weight-pruning, structured-pruning]
---

## Summary

**Model Pruning** is a neural network compression technique that removes weights, connections, or entire neurons that contribute minimally to the model's output. By eliminating redundancy, pruning reduces model size, memory footprint, and inference latency — often with minimal accuracy loss.

## Why Prune

| Goal | Pruning Benefit |
|------|----------------|
| Faster inference | Fewer weights → fewer multiply-accumulate operations |
| Smaller model size | Store and transfer fewer parameters |
| Lower energy consumption | Reduced compute per inference |
| Edge deployment | Fit large models into mobile/IoT memory constraints |

## Types of Pruning

| Type | What Is Removed | Granularity | Impact |
|------|-----------------|-------------|--------|
| **Unstructured** | Individual weight connections | Fine-grained | High compression, requires sparse kernels |
| **Structured** | Entire channels, filters, or neurons | Coarse-grained | Maintains dense tensor shapes; easier to deploy |
| **Semi-structured** | Blocks of weights (e.g., 2:4 sparsity) | Medium | Balanced compression and hardware efficiency |

## Pruning Methods

- **Magnitude-based** — Remove weights with smallest absolute values (simple, effective)
- **Gradient-based** — Remove weights with low gradient sensitivity (more accurate but slower)
- **Lottery Ticket Hypothesis** — Randomly initialized networks contain sparse subnetworks that train as well as the full network
- **Movement Pruning** — Gradually push weights toward zero during training; remove when threshold crossed

## Pruning vs Quantization vs Distillation

| Technique | What It Reduces | Typical Compression |
|-----------|-----------------|---------------------|
| **Pruning** | Number of parameters | 2–10× |
| **Quantization** | Precision per parameter | 2–4× (FP16→INT8) to 8× (FP32→INT4) |
| **Distillation** | Model architecture size | 10–100× (teacher → student) |

These techniques are **stackable** — prune first, then quantize the remaining weights, then optionally distill into a smaller architecture.

## Key Takeaways

1. Pruning removes redundant parameters, accelerating inference and reducing model size.
2. Structured pruning is easier to deploy than unstructured pruning on standard hardware.
3. Pruning is most effective on overparameterized models (large transformers have abundant redundancy).
4. Pruning + quantization + distillation together can compress models by 100× or more.

---

- Complements [[model-quantization]] — prune to remove weights, then quantize the survivors to lower precision
- Complements [[model-distillation]] — distillation trains a smaller model; pruning shrinks the existing one
- Related to [[fine-tuning]] — pruning can be applied to fine-tuned models for cheaper deployment
- Related to [[vectorized-execution]] — both optimize computational efficiency through structural changes
- Framework source: [[sources/building-llms-for-production]] — pruning as one of four deployment optimization techniques
