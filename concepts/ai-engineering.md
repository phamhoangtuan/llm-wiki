---
title: "AI Engineering"
type: concept
tags: [ai-engineering, foundation-models, ml-engineering, rag, evaluation]
created: 2026-08-15
updated: 2026-08-15
sources: [ai-engineering-chip-huyen]
aliases: [foundation-model-engineering, ai-app-development]
---

## Summary

**AI Engineering** is the discipline of building applications on top of readily available foundation models — large models trained by a few organizations and served via APIs — rather than training models from scratch. Coined and mapped by Chip Huyen, it reframes AI from an esoteric, specialized field into a general-purpose development tool accessible to engineers with no prior ML background (source: [[sources/ai-engineering-chip-huyen]]).

## AI Engineering vs ML Engineering

| Aspect | Traditional [[machine-learning-systems|ML Engineering]] | AI Engineering |
| ------ | --------------------------- | -------------- |
| Model origin | Build and train your own | Adapt pre-trained foundation models |
| Core work | Feature engineering, tabular annotation | Adaptation: [[prompt-engineering]], [[retrieval-augmented-generation|RAG]], [[fine-tuning]] |
| Product involvement | Often downstream | Engineers sit close to product, iterate faster |
| Investment order | Data/model first | Product first; invest in data/training only after the app shows promise |

The shift is from *developing* models to *adapting and evaluating* them.

## The Three-Layer Stack

| Layer | Responsibility |
| ----- | -------------- |
| **Application Development** | UI, prompt engineering, context construction (RAG), rigorous evaluation |
| **Model Development** | Modeling, training, dataset engineering, inference optimization (faster/cheaper) |
| **Infrastructure** | Model serving, compute and data management, system monitoring |

## Core Adaptation Techniques

1. **[[prompt-engineering|Prompt Engineering]]** — adapt the model without touching weights: instructions, personas, in-context examples.
2. **[[retrieval-augmented-generation|RAG]]** — connect responses to external data for query-specific context, mitigating hallucination.
3. **[[fine-tuning|Finetuning]]** — adjust actual weights to optimize behavior, style, or domain capability.

## Evaluation-Driven Development

Evaluation is the hardest problem in AI engineering because foundation models emit open-ended output with no single "ground truth." The discipline mandates defining evaluation criteria and pipelines **before** building — tracking domain capabilities, generation quality, instruction-following reliability, and operational cost/latency. See [[llm-evaluation-metrics]].

## Risks and Maintenance

- **Prompt attacks** — jailbreaking and indirect prompt injection exploit instruction-following to leak data or perform unauthorized actions.
- **Model obsolescence** — a model optimal today may be outperformed months later; [[compound-ai-systems|compound systems]] with swappable models hedge against this.

---

- Related to [[ai-native-engineering]] — AI engineering is the field; AI-native engineering is its agent-orchestration paradigm
- Succeeds [[machine-learning-systems]] — the foundation-model successor to Huyen's earlier ML-systems framing
- Builds on [[prompt-engineering]], [[retrieval-augmented-generation]], [[fine-tuning]] — the three adaptation techniques
- Depends on [[llm-evaluation-metrics]] — evaluation-driven development is the discipline's hardest challenge
- Related to [[compound-ai-systems]] — swappable, multi-component systems hedge against model drift
- Benchmark source: [[sources/ai-engineering-chip-huyen]] — Chip Huyen's canonical map of the discipline
