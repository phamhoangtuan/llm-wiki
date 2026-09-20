---
title: "MLOps"
type: concept
tags: [machine-learning, mlops, devops, deployment, monitoring]
created: 2026-07-13
updated: 2026-07-13
sources: [introduction-to-machine-learning-systems]
aliases: [ml-operations, machine-learning-operations]
---

## Summary

**MLOps** (Machine Learning Operations) is the discipline of automating deployment, monitoring, and retraining of ML models in production. It extends DevOps principles to ML systems, addressing the unique challenge that ML technical debt accumulates faster than in traditional software due to data drift, model staleness, and concept drift.

## Why MLOps Exists

ML systems have more failure modes than traditional software:

| Failure Mode | Traditional Software | ML Adds |
| --- | --- | --- |
| Code bugs | Yes | Yes |
| Dependency issues | Yes | Yes |
| **Data quality degradation** | Rare | **Constant** |
| **Model staleness** | N/A | **Inevitable** |
| **Concept drift** | N/A | **Silent** |
| **Training/serving skew** | N/A | **Common** |

MLOps addresses these by automating the entire lifecycle: data validation → training → evaluation → deployment → monitoring → retraining.

## Core Practices

- **Continuous Training (CT)**: Automatically retrain models when data distributions shift or performance degrades below thresholds
- **Model Versioning**: Track model artifacts, training data, hyperparameters, and evaluation metrics together
- **Deployment Strategies**: Canary deployments, shadow mode, A/B testing for models
- **Monitoring**: Track prediction drift, feature drift, latency, throughput, and business metrics
- **Feature Stores**: Centralized repositories for feature definitions, ensuring consistency between training and serving
- **Pipeline Orchestration**: Coordinate data extraction, feature engineering, training, evaluation, and deployment as a DAG

## Relationship to DevOps

MLOps inherits DevOps principles (CI/CD, infrastructure as code, observability) but extends them with:

- **Data versioning** (not just code)
- **Model registries** (not just container registries)
- **Experiment tracking** (not just build logs)
- **Fairness/bias monitoring** (not just performance monitoring)

---

- Built on [[machine-learning-systems]] — MLOps operationalizes the ML systems engineering discipline
- Related to [[dataops]] — DataOps applies similar DevOps principles to data pipelines
- Related to [[observability]] — metrics, logs, and traces extended to model behavior
- Related to [[ai-native-engineering]] — MLOps is a core practice for professional AI-native engineers
- Benchmark source: [[sources/introduction-to-machine-learning-systems]] — Reddi covers MLOps in Part IV (Robust Deployment)
