---
title: "Flash Attention"
type: concept
tags: [llm, attention, optimization, transformer, gpu]
created: 2026-07-13
updated: 2026-07-13
sources: [hands-on-large-language-models]
aliases: [io-aware-attention, flash-attention-2]
---

## Summary

**Flash Attention** is an IO-aware attention algorithm that dramatically speeds up the self-attention computation in transformer models by optimizing data movement between different levels of GPU memory (SRAM and HBM). Unlike approximate methods, Flash Attention is exact — it computes the same mathematical result as standard attention, just much faster.

## The Bottleneck: GPU Memory Hierarchy

| Memory Type | Speed | Capacity | Role |
|-------------|-------|----------|------|
| **SRAM** (on-chip) | ~19 TB/s | ~20 MB | Very fast but tiny — ideal for computation |
| **HBM** (High Bandwidth Memory) | ~1.5 TB/s | 40–80 GB | Large but slower — where model weights live |

Standard attention suffers because it must **repeatedly read/write the full attention matrix to HBM** — the matrix is O(n²) in sequence length, making memory bandwidth the bottleneck, not computation.

## How Flash Attention Works

1. **Tiling** — Break the attention matrix into small blocks that fit in SRAM
2. **Recomputation** — Avoid storing the full attention matrix in HBM; recompute softmax statistics on-the-fly
3. **IO-Aware Fusion** — Perform all operations (QK^T, softmax, V multiplication) within SRAM before writing results to HBM

Result: Dramatically fewer HBM reads/writes, making attention compute-bound instead of memory-bound.

## Impact

| Metric | Standard Attention | Flash Attention |
|--------|-------------------|-----------------|
| Memory Complexity | O(n²) | O(n) |
| Speed (training) | 1× | 2–4× faster |
| Mathematical Result | Exact | Exact (not approximate) |
| Wall-clock speedup for long sequences | 1× | 5–10× faster |

## Adoption

Flash Attention is now the default in most modern LLM frameworks:
- **PyTorch** — `scaled_dot_product_attention` with Flash Attention backend
- **Hugging Face Transformers** — Auto-detects and enables Flash Attention
- **GPT-4, Llama 3, Claude** — Flash Attention is standard in all major model implementations

## Key Takeaways

1. Flash Attention is an exact optimization — no trade-off between speed and accuracy.
2. It addresses the real bottleneck in transformers: memory bandwidth, not compute.
3. Critical for training and inference with long context windows (8K+ tokens).
4. Not a separate library you install — most modern frameworks auto-enable it.

---

- Accelerates [[kv-caching]] — Flash Attention and KV Caching are complementary inference optimizations
- Related to [[model-quantization]] — both are memory-centric optimizations; quantization shrinks weights, Flash Attention reduces activation memory
- Related to [[fine-tuning]] — Flash Attention accelerates fine-tuning by 2–4× during training forward/backward passes
- Benchmark source: [[sources/hands-on-large-language-models]] — Jay Alammar's coverage of attention optimization techniques
