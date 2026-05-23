---
title: "Wiki Maintenance"
type: concept
tags: [meta, workflow, agents]
created: 2026-05-23
updated: 2026-05-23
sources: [sample-article]
aliases: [maintenance, wiki-ops]
---

## Summary

Wiki Maintenance describes the operational model of this LLM-maintained knowledge base. The core insight (from [[sources/sample-article]]) is that the LLM handles all bookkeeping — updating cross-references, integrating new sources, flagging contradictions — so the human can focus on curation and thinking.

## Key Ideas

- [[knowledge-graph|Lightweight Knowledge Graph]] — cross-references are compiled at write time via [[wikilinks]], not re-derived at query time
- **Three-layer architecture**: raw sources (immutable) → wiki (LLM-owned) → schema (co-evolved)
- **Compound knowledge**: query answers get filed as permanent synthesis pages

## Operations

- **Ingest** — Drop a source → LLM reads, summarizes, updates all related concept pages, logs
- **Query** — Ask → LLM reads index, synthesizes with citations, optionally files result
- **Lint** — Health check: contradictions, orphans, stale claims, gaps

## Connections

- Inspired by Vannevar Bush's [[Memex]] — personal knowledge store with associative trails
- Related to [[Zettelkasten]] — atomic notes with deliberate connections
- Contrasts with [[RAG|Retrieval-Augmented Generation]] — knowledge compiled once vs re-derived per query
