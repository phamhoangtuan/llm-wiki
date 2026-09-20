---
title: "The LLM Wiki Pattern"
type: source
tags: [meta, architecture, llm, knowledge-management]
created: 2026-05-24
updated: 2026-06-15
author: "Andrej Karpathy"
source_type: article
source_date: 2026-04-04
ingested: 2026-05-23
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
concepts: [wiki-maintenance]
---

## Summary

Karpathy describes a pattern for building personal knowledge bases using LLMs. Instead of RAG (retrieving chunks at query time), the LLM incrementally builds and maintains a persistent wiki — structured, interlinked markdown files that sit between the user and raw sources.

## Key Takeaways

- **Three-layer architecture**: raw sources (immutable) → wiki (LLM-owned) → schema (co-evolved in AGENTS.md)
- **Three operations**: ingest (process sources), query (synthesize with citations), lint (health check)
- **Compounding knowledge**: answers to queries can be filed as permanent synthesis pages — the wiki gets richer with every interaction
- **Index + Log**: `index.md` (content catalog) and `log.md` (chronological record) replace vector search at moderate scale
- **Maintenance is free**: LLMs don't get bored updating cross-references — the cost of bookkeeping is near zero

## Quotes

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

---
- Inspired by Vannevar Bush's Memex (1945)
- Implemented in this wiki — see [[wiki-maintenance]] for the operational model
