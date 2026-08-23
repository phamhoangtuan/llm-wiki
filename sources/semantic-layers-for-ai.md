---
title: "Semantic Layers Are Now for AI, Not Just Humans"
type: source
source_type: article
author: "Madison Mae"
url: "https://learnanalyticsengineering.substack.com/p/i-was-wrong-about-semantic-layers"
source_date: 2026-06-11
ingested: 2026-06-11
created: 2026-06-08
updated: 2026-06-15
tags: [semantic-layer, analytics-engineering, ai, dbt, data-modeling]
concepts: [semantic-layer]
---

## Summary

Madison Mae re-evaluates her stance on semantic layers — once dismissed as high-effort/low-reward, now seen as critical infrastructure for AI-enabled analytics. The key shift: semantic layers were built for human stakeholders who never used them; now they serve AI agents that will. She tests **ktx**, an open-source tool that builds context layers from dbt, query history, Notion, Slack, and BI tools, and shares her hands-on experience.

## Core Message

> Semantic layers aren't for humans anymore — they're for AI agents. And unlike humans, AI agents will actually use them. Without a unified context layer pulling from dbt, BI definitions, query patterns, and business docs, AI keeps guessing metric definitions wrong.

## Key Takeaways

1. **Old problem**: AI agents struggle with business questions because metric definitions live scattered across BI tools, dbt, docs, and tribal knowledge
2. **New user**: Semantic layers built for AI agents (not human stakeholders) — guaranteed adoption because the AI needs them to function
3. **Anthropic benchmark**: 95% accuracy by combining strong data foundations + sources of truth (semantic layer, lineage, business context) + validation
4. **ktx tool**: Open-source context layer ingesting from dbt, query history, Notion, Slack, BI tools — version-controlled via Git
5. **Beyond dbt alone**: Query pattern metadata (which tables join, common filters) and business docs (Notion) carry context lost in pure dbt documentation

## Companion Concept

→ [[semantic-layer]]
