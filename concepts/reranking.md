---
title: "Reranking"
type: concept
tags: [llm, rag, retrieval, search, optimization, pipeline]
created: 2026-07-13
updated: 2026-07-13
sources: [hands-on-large-language-models]
aliases: [two-stage-retrieval, re-ranking, retrieval-reranking]
---

## Summary

**Reranking** is a two-stage retrieval pattern where a fast, cheap retriever (e.g., keyword search, vector similarity) first produces a broad candidate set, and then a more expensive but more accurate model (e.g., cross-encoder, LLM) re-scores and filters that candidate set. It achieves near-expert retrieval quality at a fraction of the cost of running the expensive model on the full dataset.

## Two-Stage Architecture

```
Full Dataset → Stage 1: Fast Retriever → Top-K Candidates (100–1000) → Stage 2: Re-ranker → Final Results (5–20)
```

| Stage | Method | Cost per Document | Accuracy |
|-------|--------|-------------------|----------|
| **Stage 1 (Retrieval)** | BM25, vector similarity (bi-encoder) | Very low (microseconds) | Moderate — high recall, low precision |
| **Stage 2 (Reranking)** | Cross-encoder, LLM, Cohere Rerank | Low–Medium (milliseconds) | High — re-orders by true relevance |

## Why Reranking Works

The fast retriever prioritizes **recall** (don't miss anything relevant), even at the cost of precision (include some irrelevant results). The re-ranker then prioritizes **precision** (rank the truly relevant highest). Combined, they deliver both high recall and high precision without the linear cost of running the expensive model on every document.

## Reranking in RAG Pipelines

Reranking is critical for Retrieval-Augmented Generation:

1. **Vector search** retrieves 50–200 candidate passages
2. **Cross-encoder or LLM** re-ranks them to the top 5–10
3. Only the top-ranked passages are injected into the LLM context window

This ensures the LLM sees only the most relevant context, reducing hallucinations and improving answer quality.

## Reranking Beyond RAG

| Application | Fast Retriever | Re-ranker | Benefit |
|-------------|---------------|-----------|---------|
| **E-commerce search** | Elasticsearch/BM25 | Learning-to-rank model | Catalog-scale search with precise ranking |
| **Code search** | grep/ripgrep | Embedding similarity | Instant matches + semantic understanding |
| **Topic modeling (BERTopic)** | Document clustering | LLM for label generation | Millions of documents with only hundreds of LLM calls |

## Key Takeaways

1. Reranking is a cost-quality Pareto optimization — pay more for the last mile of precision.
2. The fast retriever handles scale; the re-ranker handles quality.
3. Essential for production RAG — without reranking, vector search alone injects noise into LLM prompts.
4. Same pattern applies beyond text: image search, recommendation, code search all benefit from two-stage pipelines.

---

- Essential for [[retrieval-augmented-generation]] — reranking improves RAG retrieval quality before context injection
- Related to [[prompt-engineering]] — clean, relevant context from reranking reduces prompt engineering burden
- Related to [[llm-evaluation-metrics]] — reranking directly improves retrieval metrics (Hit Rate, MRR) and downstream generation quality
- Related to [[semantic-layer]] — reranking bridges structured and unstructured data in agent-facing architectures
- Benchmark source: [[sources/hands-on-large-language-models]] — reranking as an efficiency pattern for LLM-powered systems
