---
title: "PEFT"
type: concept
tags: [llm, fine-tuning, training, optimization, ml]
created: 2026-07-13
updated: 2026-07-13
sources: [hands-on-large-language-models]
aliases: [parameter-efficient-fine-tuning, efficient-fine-tuning]
---

## Summary

**PEFT (Parameter-Efficient Fine-Tuning)** is a family of techniques that adapt pre-trained large language models to specific tasks by training only a small fraction of the model's parameters. Instead of updating billions of weights, PEFT methods add or modify a tiny number of parameters (typically 0.01%–1% of the total), achieving near full-fine-tuning quality at a fraction of the cost.

## PEFT Methods

| Method | Mechanism | Trainable Parameters | Key Characteristic |
|--------|-----------|---------------------|-------------------|
| **LoRA** | Low-Rank Adaptation — injects rank-decomposition matrices into attention layers | ~0.1%–1% | Most popular; proven across all model families |
| **QLoRA** | Quantized LoRA — LoRA adapters on a 4-bit quantized base model | ~0.1%–1% | Runs on a single consumer GPU |
| **Adapter Layers** | Bottleneck layers inserted between transformer blocks | ~1%–3% | Slightly slower inference due to added sequential computation |
| **Prefix Tuning** | Learnable continuous vectors prepended to the input | < 0.1% | Extremely parameter-efficient; harder to optimize |
| **Prompt Tuning** | Soft prompts — learnable embeddings at the input layer | < 0.01% | Minimal parameters; best for very large models |

## PEFT vs Full Fine-Tuning

| Aspect | Full Fine-Tuning | PEFT (LoRA/QLoRA) |
|--------|-----------------|-------------------|
| **Trainable parameters** | 100% (all weights) | 0.1%–1% |
| **GPU VRAM** | 60+ GB for 7B models | 8–24 GB for 7B models |
| **Storage per task** | Full model copy (~14 GB) | Adapter weights (~10 MB) |
| **Training time** | Hours to days | Minutes to hours |
| **Accuracy** | Baseline | 95%–99% of baseline |
| **Catastrophic forgetting** | Risk | Minimal (base weights frozen) |

## The "GPU-Poor" Enabler

PEFT democratizes LLM customization:

- Fine-tune a 7B model on a gaming GPU (RTX 3060)
- Store 100 domain-specific adapters on disk, swap them at runtime
- Iterate rapidly — experiment with 10 variants in the time it takes to run one full fine-tune

## Key Takeaways

1. PEFT reduces fine-tuning cost by **99% or more** in both compute and storage.
2. Frozen base + swappable adapters = one model serving multiple domains.
3. QLoRA is the practical PEFT implementation for engineers with limited hardware.
4. PEFT is not a compromise — for most use cases, it matches or exceeds full fine-tuning quality.

---

- Core PEFT method: [[lora]] — LoRA and QLoRA are the most widely adopted PEFT techniques
- Related to [[fine-tuning]] — PEFT is the practical approach to fine-tuning in resource-constrained environments
- Related to [[model-quantization]] — QLoRA combines PEFT with 4-bit quantization for maximum efficiency
- Related to [[retrieval-augmented-generation]] — PEFT adapters can specialize LLMs for specific RAG domains
- Benchmark source: [[sources/hands-on-large-language-models]] — PEFT as the cornerstone of GPU-efficient LLM customization
