---
title: "Wiki Maintenance"
type: concept
tags: [meta, workflow, agents]
created: 2026-05-23
updated: 2026-06-15
sources: [sample-article]
---

## Summary

Wiki Maintenance describes the operational model of this LLM-maintained knowledge base. The core insight (from [[sources/sample-article|sample-article]]) is that the LLM handles all bookkeeping — updating cross-references, integrating new sources, flagging contradictions — so the human can focus on curation and thinking.

## Key Ideas

- [[knowledge-graph|Lightweight Knowledge Graph]] — cross-references are compiled at write time via wikilinks, not re-derived at query time
- **Three-layer architecture**: raw sources (immutable) → wiki (LLM-owned) → schema (co-evolved)
- **Compound knowledge**: query answers get filed as permanent synthesis pages

## Operations

- **Ingest** — Drop a source → LLM reads, summarizes, updates all related concept pages, logs
- **Query** — Ask → LLM reads index, synthesizes with citations, optionally files result
- **Lint** — Health check: contradictions, orphans, stale claims, gaps

---
- Related to [[knowledge-graph]] — cross-references compiled at write time, not re-derived at query time
- Benchmark source: [[sources/sample-article]] — the original article describing the LLM wiki maintenance pattern
