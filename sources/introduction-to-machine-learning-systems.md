---
title: "Introduction to Machine Learning Systems"
type: source
source_type: book
author: "Vijay Janapa Reddi"
url: ""
source_date: 2024-01-01
ingested: 2026-07-13
tags: [machine-learning, ml-systems, mlops, ai-engineering, systems-design]
concepts: [machine-learning-systems, mlops, sustainable-ai, ai-scaling-laws, compound-ai-systems]
---

## Summary

Prof. Vijay Janapa Reddi's 2,020-page textbook bridges the gap between ML theory and production engineering. The book organizes ML systems engineering around the **AI Triangle** — Data, Algorithms, and Computing Infrastructure — structured as a six-part framework from foundations to frontiers.

## The AI Triangle

Success in modern AI requires mastery of all three pillars: **Data** (the fuel), **Algorithms** (the methods), and **Computing Infrastructure** (the engine). Ignoring any corner causes system failure.

## Six-Part Framework

| Part | Focus | Key Topics |
| --- | --- | --- |
| I: Systems Foundations | Deployment spectrum, DNN architectures | Cloud → TinyML, MLPs/CNNs/RNNs/Transformers as engineering decisions |
| II: Design Principles | AI workflow, data engineering, training | Iterative loops (not linear pipelines), 4 Pillars of data: Quality/Reliability/Scalability/Governance |
| III: Performance Engineering | Optimization, acceleration, benchmarking | Pruning, quantization, distillation (4-10x size reduction); GPU/TPU acceleration (10-100x speedups) |
| IV: Robust Deployment | MLOps, on-device learning, security | Managing ML technical debt, adversarial defense, model inversion prevention |
| V: Trustworthy Systems | Responsible AI, sustainable AI | Fairness audits, carbon footprint optimization, AI for Good under extreme constraints |
| VI: Frontiers | AGI systems, compound AI systems | Orchestrated ensembles (retrievers + reasoners + verifiers + tools); energy efficiency, cognitive reasoning |

## ML Workflow vs Traditional Software

ML systems are iterative, feedback-driven, and data-dependent — not linear "code → ship" pipelines. Expect constant looping: new data → retrain → re-evaluate → redeploy. Production isn't a finish line, it's a new set of challenges.

## Key Insight

> "Great AI isn't just smart — it's reliable, efficient, scalable, and trustworthy."

The bottleneck is shifting from "Can we build a smarter model?" to "Can we build a scalable, sustainable, safe system around it?"
