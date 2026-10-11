---
title: "Entity Resolution"
type: concept
tags: [knowledge-graph, nlp, data-quality, agents]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: [entity-deduplication, canonical-entity-mapping]
---

## Summary

**Entity Resolution** is the process of mapping surface forms (names, abbreviations, aliases, spelling variants, partial names) to canonical entities in a knowledge graph. In the context of [[knowledge-graph]] construction for agents, it is framed as a **reasoning task** rather than a string-matching problem — because simple similarity fails when labels differ substantially yet refer to the same entity.

## Why String Matching Fails

- "Edwin Aldrin" vs "Buzz Aldrin" — zero character overlap, same person
- "IBM" vs "International Business Machines" — same entity, different lengths
- Different people can share the same name — similarity incorrectly merges them

## Model-Based Resolution

Anthropic's cookbook approach:

1. **Group candidates by entity type** — all "Person" mentions, all "Organization" mentions
2. **Use descriptions as contextual evidence** — what does each surface form's context say about this entity?
3. **Ask a stronger model (Sonnet) to propose canonical clusters** — the model reasons about whether two surface forms refer to the same real-world entity
4. **At scale**: cheap blocking signals (shared words, type overlap) narrow the candidate set before model arbitration

## Resolution Must Be Reversible

A canonical entity should retain:

- Its aliases (all surface forms)
- Source documents
- Resolution rationale
- Confidence score
- The run that created the merge

This ensures incorrect merges can be reversed without reconstructing the entire pipeline. **A false merge is catastrophic** — if two people are collapsed into one node, every downstream query may combine their employers, projects, dates, and actions.

## Evaluation Metrics

- **Compression ratio**: raw surface forms / canonical entities (high is not automatically good — over-merging creates a connected but false graph)
- **Pairwise precision and recall**: did we correctly pair surface forms?
- **False merge rate**: how many distinct entities were incorrectly merged?
- **Missed merge rate**: how many aliases of the same entity were not merged?
- **Manual review rate**: how many decisions require human verification?

---

- Core operation in [[knowledge-graph]] construction — extracts produce surface forms, resolution produces canonical nodes
- Enables [[graph-grounding]] — resolution quality determines whether queries traverse correct or false paths
- Source: [[sources/graph-engineering-karpathy]]
