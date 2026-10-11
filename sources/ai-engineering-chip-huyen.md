---
title: "AI Engineering: Building Applications with Foundation Models"
type: source
source_type: book
author: "Chip Huyen"
url: "https://www.oreilly.com/library/view/ai-engineering/9781098166304/"
source_date: 2025
ingested: 2026-08-15
tags: [ai-engineering, foundation-models, rag, prompt-engineering, fine-tuning, evaluation]
concepts: [ai-engineering, ai-native-engineering, prompt-engineering, retrieval-augmented-generation, fine-tuning, llm-evaluation-metrics, compound-ai-systems]
---

## Summary

Chip Huyen defines **[[ai-engineering]]** as the discipline of building applications on top of readily available foundation models — transforming AI from an esoteric, specialized field into a general development tool accessible to anyone, including engineers with no prior ML experience. The book is the canonical map of the discipline: how it differs from ML engineering, the three-layer stack, the core adaptation techniques, and why evaluation (not generation) is the hardest problem.

---

## Key Claims

1. **AI Engineering ≠ ML Engineering**. Traditional ML engineering means building and training your own models (feature engineering, tabular annotation). AI engineering means *adapting* models already trained by a few large orgs and served via API. The focus shifts from training to adaptation — [[prompt-engineering|prompt engineering]], [[retrieval-augmented-generation|RAG]], and [[fine-tuning]] — and AI engineers are closer to product decisions, iterating faster and investing in data/training only after the app shows promise.

2. **The three-layer stack**:
   - **Application Development Layer** — UI, prompt engineering, context construction (RAG), rigorous evaluation.
   - **Model Development Layer** — tooling for modeling, training, dataset engineering, and inference optimization (faster/cheaper).
   - **Infrastructure Layer** — model serving, compute and data management, system monitoring.

3. **Three adaptation techniques** (in order of cost/effort): prompt engineering (no weight update — instructions, personas, examples), RAG (ground responses in external data to mitigate hallucination), and finetuning (adjust weights for behavior/style/domain).

4. **Evaluation-driven development**. Evaluation is the hardest challenge because foundation models produce open-ended outputs with no single "ground truth." Teams should define evaluation criteria and pipelines *before* building — tracking domain capabilities, generation quality, instruction-following reliability, and operational cost/latency. See [[llm-evaluation-metrics]].

5. **Risks and maintenance**. The landscape shifts constantly: models, benchmarks, and regulations. Applications must defend against prompt attacks — jailbreaking and indirect prompt injection that exploit instruction-following to leak data or perform unauthorized actions. A model optimal today may be outperformed by a new base model released months later, making [[compound-ai-systems|compound systems]] and swappable-model design essential.

---

## Connections

- Defines [[ai-engineering]] — the discipline of building on foundation models, distinct from training your own
- Complements [[ai-native-engineering]] — AI engineering is the field; AI-native engineering is its agent-orchestration paradigm
- Builds on [[prompt-engineering]], [[retrieval-augmented-generation]], [[fine-tuning]] — the three adaptation techniques
- Depends on [[llm-evaluation-metrics]] — evaluation-driven development is the discipline's hardest problem
- Extends [[machine-learning-systems]] — Huyen's earlier book on ML systems design; AI engineering is its foundation-model successor
- Related to [[compound-ai-systems]] — swappable models and multi-component systems hedge against model obsolescence
