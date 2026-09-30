---
title: "KV Caching"
type: concept
tags: [llm, inference, optimization, attention, transformer]
created: 2026-07-13
updated: 2026-07-13
sources: [hands-on-large-language-models]
aliases: [kv-cache, key-value-caching, attention-cache]
---

## Summary

**KV Caching** is an inference optimization technique for autoregressive transformer models that stores previously computed Key and Value vectors so they don't need to be recomputed for each new token generation. It eliminates redundant computation, making text generation dramatically faster without any change to model weights or output quality.

## The Problem It Solves

LLMs generate text **one token at a time** (autoregressive). Without caching, every new token forces a full recalculation of attention over all previous tokens:

```
Generate token #1: compute K,V for token #1
Generate token #2: compute K,V for token #1 + token #2
Generate token #3: compute K,V for token #1 + token #2 + token #3
...
```

This is **O(n²)** in compute — each new token redoes all prior work.

## How KV Caching Works

1. During the **first forward pass** (processing the prompt), compute and **store** all Key and Value vectors
2. For each **subsequent token**, retrieve cached K,V for all prior tokens and only compute K,V for the new token
3. The attention mechanism operates over `[cached K,V + new K,V]` without any recomputation

## Performance Impact

| Scenario | Time for 100 Tokens | Explanation |
|----------|---------------------|-------------|
| Without KV Cache | 21.8 seconds | Recomputes all K,V every token |
| With KV Cache | 4.5 seconds | Only computes K,V for the new token |

> **~5× speedup** for typical generation lengths. The longer the sequence, the bigger the win.

## Memory Trade-Off

The cache stores all K,V vectors for every layer and every attention head:

- **For a 7B model**: ~2 GB of KV cache for a 2048-token context
- **For a 70B model**: ~20 GB for the same context length

This is the main cost — VRAM consumption grows linearly with context length × batch size. Techniques like Multi-query Attention (MQA) and Grouped-query Attention (GQA) reduce KV cache size by sharing K,V across attention heads.

## Key Takeaways

1. KV Caching is the single highest-impact inference optimization — ~5× speedup with zero quality loss.
2. The trade-off is VRAM: longer contexts require larger caches.
3. MQA and GQA are architectural responses to KV cache memory pressure.
4. Always enable KV Caching in production inference — it's a solved problem with standard implementations.

---

- Enabled by [[flash-attention]] — Flash Attention's IO-aware design works in tandem with KV caching for maximum throughput
- Related to [[model-quantization]] — quantization shrinks model weights; KV caching addresses compute redundancy — complementary optimizations
- Related to [[lora]] — LoRA fine-tuned models benefit equally from KV caching at inference time
- Benchmark source: [[sources/hands-on-large-language-models]] — Jay Alammar's practical guide to LLM optimization
