---
title: "Knowledge Graph"
type: concept
tags: [architecture, linking, index]
created: 2026-05-23
updated: 2026-08-06
sources: [sample-article, graph-engineering-karpathy]
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

## Agent Knowledge Graphs: Shared Memory and Grounding

Beyond static wikis, knowledge graphs serve as **infrastructure for agent systems** in [[graph-engineering]]. Three roles:

### Shared Memory

Workers write findings as structured graph updates. A synthesizer traverses the graph to combine findings even if no single worker saw all source documents. The graph persists across sessions — "the agent forgets, the graph does not."

### Grounding Layer

An evaluator checks claims against graph edges with provenance. A claim like "Vendor X supplied the component in Incident Y" can be verified by checking for edges `(Vendor X, supplied, Component Z)` and `(Component Z, involved_in, Incident Y)`. Missing edges produce structured, actionable feedback rather than free-form critique. See [[graph-grounding]].

### Construction Pipeline

Anthropic's cookbook replaces classical NLP with model calls: **Haiku** extracts typed entities and S-P-O relations against a Pydantic schema → **Sonnet** resolves surface forms (e.g., "Edwin Aldrin" → "Buzz Aldrin") into canonical entities → **NetworkX MultiDiGraph** assembly with provenance on every edge → **Sonnet** queries serialized subgraphs with edge-level citations. See [[entity-resolution]].

---

- Core to [[wiki-maintenance]] — the operational model
- Contrasts with embedding-based RAG — graph is explicit rather than statistical
- Extends naturally with tools like qmd (hybrid BM25/vector search for markdown)
- Infrastructure for [[graph-engineering]] — shared memory and grounding layer for agent systems
- Enables [[graph-grounding]] — constraining agent generation with graph facts
- Related to [[entity-resolution]] — mapping surface forms to canonical nodes
- Source: [[sources/graph-engineering-karpathy]] — Anthropic's KG Construction Cookbook
