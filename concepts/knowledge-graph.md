---
title: "Knowledge Graph"
type: concept
tags: [architecture, linking, index]
created: 2026-05-23
updated: 2026-05-23
sources: [sample-article]
---

## Summary

A lightweight knowledge graph built from cross-linked markdown pages. Instead of a dedicated graph database or vector store, the wiki uses wikilinks, a content index (`index.md`), and consistent YAML frontmatter to achieve the same effect without infrastructure.

## How It Works

1. **Write-time linking** — when the LLM ingests a source, it creates/updates concept pages with explicit links (`<a href="...">`) to related pages. The connections are compiled once, not re-derived.

1. **Index as entry point** — `index.md` lists every page with a one-line summary. The LLM reads this first to find relevant pages, then drills in. This replaces vector search at moderate scale (~500 pages).

1. **Frontmatter as metadata layer** — YAML frontmatter stores tags, source backlinks, aliases, and dates. Tools like Obsidian Dataview can query this.

## Why This Works

- No infrastructure — just markdown files in folders
- Git-trackable — every link is explicit in the source
- LLM-maintainable — the LLM writes the links as a natural part of ingest
- Scales to hundreds of pages before needing search tooling

---
- Core to [[wiki-maintenance]] — the operational model
- Contrasts with embedding-based RAG — graph is explicit rather than statistical
- Extends naturally with tools like qmd (hybrid BM25/vector search for markdown)
