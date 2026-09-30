---
title: "CI/CD Tips — r/dataengineering Discussion"
type: source
source_type: article
author: "r/dataengineering community"
url: "https://www.reddit.com/r/dataengineering/comments/1tf2gbz/cicd_tips/"
created: 2026-06-15
updated: 2026-06-15
source_date: 2026-05-16
ingested: 2026-06-15
tags: [cicd, data-engineering, linting, testing, github-actions, fabric]
concepts: [cicd-data-pipelines, dataops, data-engineer]
---

## Summary

A discussion thread on r/dataengineering where a practitioner asks for [[cicd-data-pipelines|CI/CD]] best practices for their Microsoft Fabric environment (notebooks, lakehouse, semantic models, reports, pipelines). The community responds with concrete tool recommendations, debate around notebooks vs scripts in production, and pragmatic testing strategies for [[dataops|DataOps]] and the modern [[data-engineer]].

---

## Key Takeaways

### Recommended CI/CD Tools & Practices

| Area | Tools Recommended |
|---|---|
| **CI Platform** | GitHub Actions (on `pull_request` trigger) |
| **Python Linting** | Ruff — fast, comprehensive Python linter |
| **SQL Linting** | SQLFluff — though some find it tedious for pipelines |
| **Docker Linting** | Hadolint |
| **GitHub Actions Linting** | zizmor, actionlint |
| **Data Quality** | Great Expectations, Fabric built-in validations |
| **Transformation CI/CD** | SQLMesh — plan/compile pipeline with audits and tests on changed models |
| **Code Quality** | Pre-commit or prek hooks |

### The Notebooks vs Scripts Debate

A sharp divide emerged:

- **Against notebooks in production**: Notebooks are for exploration, not production boundaries. Production code should be tested, versioned, parameterized `.py` files with CI/CD, observability, and reproducible execution.
- **Fabric context**: Microsoft Fabric pushes notebooks heavily. Some practitioners mitigate by bundling `.py` packages and using notebooks only as a thin controller.
- **Calibrate to org size**: Smaller teams may be fine with notebooks; larger organizations need stricter engineering discipline.

### Testing Philosophy

- **Don't over-focus on unit tests** for pipeline code — start with smoke testing (code validity, DAG bag checks).
- **Type hints**: Worthwhile for code comprehension and IDE support, but strict type checking (mypy/pyright) may not be worth the overhead for pipeline code.
- **Integration testing**: SLA checks, lineage validation, schema drift detection. Start by gathering real production issues and building tests around them.
- **"Don't try to catch everything in CI"** — balance between necessity and over-engineering.

### SQLMesh Highlight

One commenter called SQLMesh "the closest DE can get to real CI/CD" — it compiles the entire pipeline, runs audits and tests only on changed models. The project was recently donated to the Linux Foundation by Fivetran and is being revitalized.

---

- Related to [[cicd-data-pipelines]] — concrete tool recommendations: Ruff, SQLFluff, SQLMesh, Great Expectations, GitHub Actions
- Related to [[dataops]] — applying CI/CD discipline (linting, testing, deployment automation) to data pipelines
- Related to [[data-engineer]] — the role that benefits from these CI/CD practices in production environments
