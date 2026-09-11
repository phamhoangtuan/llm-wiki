---
title: "Differential Privacy"
type: concept
tags: [data-privacy, anonymization, mathematics, machine-learning, security]
created: 2026-06-27
updated: 2026-06-27
sources: [building-anonymization-pipeline]
aliases: [DP, epsilon-differential-privacy]
---

## Summary

**Differential Privacy** is a mathematical framework that provides formal guarantees about individual privacy in statistical data analysis. It ensures that an attacker cannot determine whether any specific individual's data was included in the dataset used to produce a result — regardless of what other information the attacker possesses.

## Core Mechanism

Differential privacy works by injecting calibrated **mathematical noise** into query results:

```
Query Result = True Result + Noise(ε)
```

Where **ε (epsilon)** — the privacy budget — controls the trade-off between privacy and accuracy:

| ε Value | Privacy | Accuracy | Use Case |
|---|---|---|---|
| **Small ε** (e.g., 0.1) | Strong privacy guarantee | Lower accuracy, more noise | Sensitive census data, medical statistics |
| **Large ε** (e.g., 10) | Weaker guarantee | Higher accuracy, less noise | Approximate analytics, non-sensitive aggregates |

## Why Differential Privacy Matters

Traditional anonymization techniques (generalization, suppression, k-anonymity) have known weaknesses:

- **Linkage attacks**: combining anonymized data with external datasets can re-identify individuals
- **Composition attacks**: running multiple queries on the same anonymized dataset can cumulatively reveal information
- **Auxiliary information**: attackers with side knowledge (e.g., knowing a specific person is in the dataset) can narrow down records

Differential privacy addresses these by providing a **provable mathematical guarantee**: the output of a differentially private mechanism is nearly the same whether or not any individual's data is included. No amount of external data or repeated querying breaks this guarantee — only the privacy budget (ε) is consumed.

> "Differential privacy ensures the attacker cannot know whether a specific individual is in the dataset — regardless of auxiliary information or repeated queries." (source: [[sources/building-anonymization-pipeline]])

## How It Works

### The Formal Definition

A randomized mechanism **M** satisfies ε-differential privacy if for any two datasets **D₁** and **D₂** that differ by only one record, and for any possible output **S**:

```
Pr[M(D₁) ∈ S] ≤ e^ε × Pr[M(D₂) ∈ S]
```

In plain English: the probability of any output changes by at most a factor of e^ε when a single individual's data is added or removed.

### Noise Mechanisms

| Mechanism | How It Works | Best For |
|---|---|---|
| **Laplace Mechanism** | Adds noise drawn from Laplace distribution scaled by sensitivity/ε | Numeric queries (counts, sums, averages) |
| **Gaussian Mechanism** | Adds Gaussian noise; satisfies (ε, δ)-differential privacy | Higher-dimensional queries, machine learning |
| **Exponential Mechanism** | Randomly selects output with probability proportional to utility score | Non-numeric outputs (best category, top-K items) |

### Sensitivity

The **sensitivity** of a query determines how much noise is needed: it's the maximum change in the query result when one individual's data is added or removed. A count query has sensitivity = 1 (adding one person changes count by at most 1). A sum query has sensitivity = max possible value (adding one person can change the sum by the largest possible value).

## Practical Applications

| Domain | Example |
|---|---|
| **Government census** | US Census Bureau uses DP to publish demographic statistics without revealing individual responses |
| **Tech companies** | Apple uses local differential privacy to collect usage statistics from iOS devices |
| **Machine learning** | DP-SGD (Differentially Private Stochastic Gradient Descent) trains models that don't memorize individual training examples |
| **Medical research** | Share aggregate health outcomes across hospitals without patient-level disclosure risk |

## Privacy Budget & Composition

Each query consumes a portion of the privacy budget (ε). Sequential composition: running two ε₁-differentially private queries yields (ε₁ + ε₂)-differential privacy. This is why a **privacy budget** must be managed — repeated queries on the same dataset erode the guarantee.

In a production anonymization pipeline, the privacy budget is tracked and queries are blocked when the budget is exhausted — preventing death-by-a-thousand-cuts re-identification.

## Trade-offs

| Benefit | Cost |
|---|---|
| Formal mathematical guarantee | Accuracy loss proportional to privacy level |
| Resistant to auxiliary information attacks | Tuning ε requires domain expertise |
| Immune to composition attacks (budget-managed) | Small datasets lose more utility than large ones |
| Applicable to any statistical output | Not suitable when individual-level precision is required |

---

- Enhanced by [[data-anonymization]] — differential privacy adds mathematical rigor to traditional anonymization pipelines
- Complements [[synthetic-data]] — synthetic data provides zero-risk alternative; DP provides formal guarantees on real data
- Governed by [[data-governance]] — Five Safes framework provides the policy layer above DP's mathematical guarantees
- Related to [[data-quality-monitoring]] — noise injection impacts data quality metrics; monitoring must account for DP-induced variance
- Benchmark source: [[sources/building-anonymization-pipeline]] — Arbuckle & El Emam's coverage of emerging PETs
