---
title: "Model Quantization"
type: concept
tags: [llm, ml, optimization, compression, inference, production]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [quantization, weight-quantization, post-training-quantization]
---

## Summary

**Model Quantization** reduces the numerical precision of a model's weights and activations — for example, from 32-bit floating point (FP32) to 8-bit integers (INT8) or 4-bit formats. This shrinks model size, lowers memory bandwidth requirements, and accelerates inference on both GPUs and CPUs, enabling large models to run on consumer hardware.

## Why Quantize

| Precision | Size | VRAM for 7B Model | Typical Use |
|-----------|------|-------------------|-------------|
| FP32 | 100% | 28 GB | Training |
| FP16 | 50% | 14 GB | Standard inference |
| INT8 | 25% | 7 GB | High-throughput serving |
| INT4 / FP4 | 12.5% | 3.5 GB | Edge/consumer GPU inference |

## Quantization Methods

| Method | When Applied | Description |
|--------|------------|-------------|
| **Post-Training Quantization (PTQ)** | After training | Convert weights to lower precision without retraining; fastest but may lose accuracy |
| **Quantization-Aware Training (QAT)** | During training | Simulate low-precision arithmetic during training; higher accuracy but more expensive |
| **GPTQ / AWQ** | Post-training | Layer-wise quantization optimized for generative models; popular for LLMs |

## Notable Formats

- **GGML / GGUF** — File format for quantized LLMs used by llama.cpp; supports multiple quantization schemes per tensor.
- **NF4 (Normal Float 4)** — 4-bit format used in QLoRA; optimizes bit allocation for normally distributed weights.

## Accuracy Impact

- Modern 4-bit quantization (GPTQ, AWQ) retains **>95% of baseline accuracy** for most tasks.
- Quantization is more damaging to small models than large ones — larger models have redundant capacity that absorbs precision loss.
- Emerging techniques (e.g., QLoRA-style 4-bit adapters) allow training on quantized bases with minimal degradation.

## Key Takeaways

1. Quantization is the fastest way to reduce model size and inference cost — no architecture changes needed.
2. 4-bit quantization makes 70B-parameter models runnable on a single consumer GPU.
3. PTQ is sufficient for most deployment scenarios; QAT is reserved for extreme precision requirements.
4. Quantization + distillation + pruning are often stacked together for maximum compression.

---

- Complements [[model-distillation]] — distill to shrink architecture, then quantize to shrink precision
- Complements [[model-pruning]] — prune redundant weights, then quantize the survivors
- Related to [[fine-tuning]] — QLoRA enables fine-tuning on 4-bit quantized base models
- Related to [[in-process-olap]] — both optimize for query performance via low-level data representation changes
- Framework source: [[sources/building-llms-for-production]] — quantization as a deployment optimization pillar
