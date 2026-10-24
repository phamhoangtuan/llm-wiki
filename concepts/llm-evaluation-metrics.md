---
title: "LLM Evaluation Metrics"
type: concept
tags: [llm, evaluation, metrics, production, reliability]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [llm-metrics, production-llm-evaluation]
---

## Summary

**LLM Evaluation Metrics** are quantitative measures used to assess the quality, reliability, and usefulness of Large Language Model outputs in production systems. Unlike academic benchmarks (e.g., MMLU, HellaSwag), production metrics focus on application-specific behavior: Is the answer faithful to the context? Is it relevant to the query? Is the retrieval system finding the right documents?

## Core Production Metrics

| Metric | Definition | What It Catches |
|--------|------------|-----------------|
| **Faithfulness** | Degree to which the answer is supported by the provided context | Hallucinations, fabricated facts |
| **Relevancy** | Degree to which the answer addresses the user's actual intent | Off-topic answers, generic responses |
| **Hit Rate** | Percentage of retrieval queries returning useful results | Poor retrieval, irrelevant document matches |
| **Context Precision** | Ratio of relevant retrieved chunks to total retrieved chunks | Noise in the context window |
| **Context Recall** | Ratio of relevant ground-truth chunks that were retrieved | Missing critical information |
| **Answer Correctness** | Factual accuracy compared to ground truth | Factual errors even when grounded |

## Evaluation Approaches

### Human Evaluation

- **Pros:** Captures nuance, tone, and subjective quality
- **Cons:** Expensive, slow, inconsistent between raters
- **Best for:** Initial model selection, adversarial case auditing

### Automated Metrics

- **Rule-based** — Regex, string matching, JSON schema validation (fast, brittle)
- **Model-based (LLM-as-Judge)** — Use a stronger model (e.g., GPT-4) to score outputs of a weaker model (e.g., Llama-3-8B)
  - Pros: Scalable, captures semantic nuance
  - Cons: Expensive, may inherit judge model biases
- **Embedding-based** — Cosine similarity between output and reference answer
  - Pros: Fast, language-agnostic
  - Cons: Misses semantic equivalence expressed differently

### RAG-Specific Metrics

| Metric | Measures |
|--------|----------|
| **Hit Rate** | Retrieval quality |
| **Mean Reciprocal Rank (MRR)** | Average rank of first relevant result |
| **Normalized Discounted Cumulative Gain (NDCG)** | Ranking quality of retrieved set |
| **Faithfulness** | Generation grounded in retrieved context |

## Observability Integration

Production evaluation is not a one-time test — it is continuous:

- **LangSmith** — Trace every request, log prompts/responses, score runs
- **Weights & Biases** — Track prompt versions, model variants, metric trends over time
- **Arize** — Drift detection, A/B testing of prompt/model changes

## Key Takeaways

1. Production LLM evaluation is distinct from academic benchmarking — focus on application behavior.
2. Faithfulness and Relevancy are the two most important metrics for grounded generation systems.
3. LLM-as-Judge is the most scalable automated approach, but requires careful prompt design and bias auditing.
4. Evaluation must be continuous, not a one-time report — integrate into the observability stack.

---

- Related to [[prompt-engineering]] — prompt changes are A/B tested using these metrics
- Related to [[retrieval-augmented-generation]] — RAG quality is measured by Hit Rate, Context Precision, and Faithfulness
- Related to [[observability]] — LLM evaluation is a specialized observability domain
- Related to [[data-quality-monitoring]] — both use automated validation to catch production issues early
- Related to [[testing-strategy]] — production LLM evaluation extends the testing pyramid into non-deterministic systems
- Benchmark source: [[sources/building-llms-for-production]] — Peters & Bouchard's coverage of production evaluation
