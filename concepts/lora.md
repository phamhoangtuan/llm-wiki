---
title: "LoRA"
type: concept
tags: [llm, fine-tuning, peft, optimization, training]
created: 2026-07-13
updated: 2026-07-13
sources: [hands-on-large-language-models]
aliases: [low-rank-adaptation, qlora]
---

## Summary

**LoRA (Low-Rank Adaptation)** is a parameter-efficient fine-tuning (PEFT) technique that injects small, trainable rank-decomposition matrices into the layers of a pre-trained model. Instead of updating all billions of original parameters, LoRA trains only these tiny adapter matrices, reducing trainable parameters by **orders of magnitude** while preserving near full-fine-tuning quality.

## How LoRA Works

Traditional fine-tuning updates the full weight matrix W:
```
W' = W + ΔW   (ΔW has same dimensions as W — billions of parameters)
```

LoRA decomposes the update into two low-rank matrices:
```
ΔW = A × B    (A and B are much smaller than W)
```

| Component | Size (Full FT) | Size (LoRA) |
|-----------|---------------|-------------|
| Trainable parameters | 150,000,000 | 197,000 (per transformer block) |
| GPU VRAM required | 60+ GB | ~12 GB |

## QLoRA: LoRA + Quantization

**QLoRA** combines LoRA with 4-bit quantization of the base model:

- The base model is quantized to 4-bit (NF4 — Normal Float 4) for memory efficiency
- LoRA adapters are trained in higher precision (FP16/BF16)
- **Result**: Fine-tune a 65B model on a single RTX 4090 (24 GB VRAM)

> QLoRA is the key enabler for "GPU-poor" fine-tuning — high-quality domain adaptation without data-center hardware.

## Why Low-Rank Works

Pre-trained models have **intrinsic low-dimensional structure** — most of the variation during fine-tuning happens in a low-rank subspace. LoRA exploits this by only updating along the most impactful directions, leaving the rest of the weight matrix frozen.

## Key Takeaways

1. LoRA reduces trainable parameters by ~10,000× compared to full fine-tuning.
2. QLoRA makes fine-tuning accessible on a single consumer GPU.
3. The frozen base + trainable adapter architecture allows swapping adapters without reloading the base model.
4. LoRA is the standard PEFT method — supported across Hugging Face, PyTorch, and most LLM frameworks.

---

- Core technique of [[peft]] — LoRA is the most widely used PEFT method
- Complements [[model-quantization]] — QLoRA stacks LoRA on top of 4-bit quantization for maximum GPU efficiency
- Related to [[fine-tuning]] — LoRA is the practical path to fine-tuning for engineers without data-center GPUs
- Powers [[retrieval-augmented-generation]] systems — LoRA adapters can specialize LLMs for retrieval-augmented tasks
- Benchmark source: [[sources/hands-on-large-language-models]] — Jay Alammar's coverage of GPU-poor optimization
