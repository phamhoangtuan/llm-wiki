# 🧠 LLM Wiki

**A persistent, LLM-maintained knowledge base that compounds over time.**

Instead of retrieving chunks at query time (RAG), the LLM incrementally builds and maintains a structured wiki — interlinked markdown files that sit between you and your raw sources. Knowledge is compiled once and kept current, not re-derived on every question.

> *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*
> — Andrej Karpathy

<div align="center">
  <a href="https://phamhoangtuan.github.io/llm-wiki/"><strong>🌐 Live Visualization → phamhoangtuan.github.io/llm-wiki</strong></a>
</div>

---

## Table of Contents

- [Why Not RAG?](#why-not-rag)
- [Architecture](#architecture)
- [Directory Structure](#directory-structure)
- [Quickstart](#quickstart)
- [Core Workflows](#core-workflows)
  - [Ingest](#ingest)
  - [Query](#query)
  - [Lint](#lint)
- [Page Formats](#page-formats)
- [The Compounding Cycle](#the-compounding-cycle)
- [Tips & Tricks](#tips--tricks)
- [Credits](#credits)

---

## Why Not RAG?

Most knowledge tools use **Retrieval-Augmented Generation**: chunk documents, index embeddings, retrieve relevant chunks at query time, and synthesize an answer on the fly. This works, but:

| RAG | LLM Wiki |
|---|---|
| Knowledge re-derived on every query | Knowledge compiled once, kept current |
| No accumulation between sessions | Wiki gets richer with every interaction |
| Chunks lack cross-references | Pages are explicitly interlinked via `[[wikilinks]]` |
| Needs vector DB infrastructure | Just markdown files in a git repo |
| Hard to spot contradictions | Lint workflow flags them explicitly |

**The wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

---

## Architecture

The system has three layers:

```
┌──────────────────────────────────────────────────┐
│                   RAW SOURCES                     │
│  Articles · Papers · Podcasts · Images            │
│  ────────────────────────────────────────         │
│  Immutable. You curate. LLM reads only.           │
├──────────────────────────────────────────────────┤
│                   THE WIKI                         │
│  concepts/ · sources/ · syntheses/                │
│  index.md · log.md                                │
│  ────────────────────────────────────────         │
│  Structured markdown. LLM writes & maintains.     │
├──────────────────────────────────────────────────┤
│                   THE SCHEMA                       │
│  AGENTS.md                                        │
│  ────────────────────────────────────────         │
│  Constitution that governs LLM behavior.          │
│  Co-evolved between you and the agent.            │
└──────────────────────────────────────────────────┘
```

**The human's job** is to curate sources, direct analysis, ask good questions, and think about what it all means. **The LLM's job** is everything else — summarizing, cross-referencing, filing, and bookkeeping.

---

## Directory Structure

```
llm-wiki/
├── AGENTS.md            # Schema — governs ALL LLM behavior
├── index.md             # Content catalog (auto-updated)
├── log.md               # Append-only chronological record
│
├── concepts/            # Entity/concept pages (the core knowledge)
│   ├── cap-theorem.md
│   ├── raft-consensus.md
│   └── ...
│
├── sources/             # Source summaries (one per ingested source)
│   ├── designing-data-intensive-apps.md
│   └── paper-mapreduce.md
│
├── syntheses/           # Query answers filed as permanent pages
│   ├── comparison-spark-vs-flink.md
│   └── streaming-vs-batch-tradeoffs.md
│
├── raw/                 # IMMUTABLE — LLM reads, never writes
│   ├── articles/
│   ├── papers/
│   ├── podcasts/
│   └── assets/          # Downloaded images/diagrams
│
├── meta/                # Auto-generated indexes (tags, orphans, etc.)
│
└── scripts/             # Optional CLI helpers (search, lint)
```

### Directory Contract

| Path | Who owns | LLM role |
|---|---|---|
| `raw/` | You | READ ONLY — source documents, never modified |
| `concepts/` | LLM | CREATE + UPDATE — one page per core concept |
| `sources/` | LLM | CREATE — one page per ingested source |
| `syntheses/` | LLM | CREATE — answers filed as permanent pages |
| `index.md` | LLM | UPDATE on every ingest — content catalog |
| `log.md` | LLM | APPEND on every operation |
| `meta/` | LLM | UPDATE on lint passes |
| `AGENTS.md` | Both | Schema — co-evolved over time |

---

## Quickstart

### 1. Clone the repo

```bash
git clone <repo-url> llm-wiki
cd llm-wiki
```

### 2. Configure your LLM agent

Point your agent (Claude Code, OpenCode, Codex, etc.) at this repo. The `AGENTS.md` file instructs it on how to behave as a disciplined wiki maintainer.

For **Claude Code** / **OpenCode**, the `AGENTS.md` is read automatically when you start a session in this directory.

### 3. Open in Obsidian (recommended)

The wiki uses Obsidian-flavored markdown — `[[wikilinks]]`, YAML frontmatter, image attachments. Open the repo folder as an Obsidian vault to get:

- **Graph view** — see connections between concepts
- **Backlinks** — see what links to a page
- **Dataview** — query pages by frontmatter
- **Web Clipper** — convert articles to markdown for `raw/`

### 4. Ingest your first source

Drop an article into `raw/articles/` and tell your agent:

> *"Ingest this."*

The LLM will:
1. Read the source
2. Discuss key takeaways with you
3. Write a summary in `sources/`
4. Create/update relevant `concepts/` pages
5. Update `index.md`
6. Append to `log.md`

### 5. Ask a question

Your first query synthesizes across the wiki. If the answer is substantial, file it as a synthesis page:

> *"Should I file this as a new synthesis?"*

The answer becomes a permanent page in `syntheses/` — the wiki just got richer.

---

## Core Workflows

### Ingest

Bring new knowledge into the wiki.

```
User drops source into raw/  →  LLM reads source
                                    │
                                    ▼
                            LLM identifies key concepts
                                    │
                                    ▼
                         [Optional] Discuss with user:
                         "Key takeaways. What to emphasize?"
                                    │
                                    ▼
                            Write sources/<slug>.md
                                    │
                                    ▼
                            For each concept touched:
                              ├─ Exists? → Update page + note contradictions
                              └─ Missing? → Create page + backlinks
                                    │
                                    ▼
                            Update index.md → Append to log.md
```

A single source typically touches **10–15 wiki pages**.

### Query

Ask questions against accumulated knowledge.

```
User asks a question  →  LLM reads index.md → finds relevant pages
                                    │
                                    ▼
                            Reads relevant pages
                                    │
                                    ▼
                            Synthesizes answer with citations
                                    │
                                    ▼
                            Offers to file as synthesis page:
                              ├─ Yes → creates syntheses/<slug>.md
                              └─ No  → answer stays in chat only
```

**Key insight**: Good answers become permanent pages. Knowledge compounds instead of disappearing into chat history.

### Lint

Keep the wiki healthy as it grows.

```
User: "Lint the wiki"  →  LLM reads every wiki page
                                    │
                ┌───────────────────┼───────────────────┐
                ▼                   ▼                   ▼
        Contradictions         Orphan pages        Stale claims
        Two pages saying       Pages with zero     Old claims
        opposite things        inbound links       superseded

                ▼                   ▼                   ▼
        Broken wikilinks     Knowledge gaps      Missing frontmatter
        [[Page]] where       Concepts mentioned  Pages without
        Page doesn't exist   but not documented  required YAML
                                    │
                                    ▼
                            Report findings → user approves → apply fixes
```

Run lint periodically (weekly or after several ingests) to keep the wiki coherent.

---

## Page Formats

### Concept Pages (`concepts/<slug>.md`)

```yaml
---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, consistency]
created: 2026-05-23
updated: 2026-05-23
sources: [designing-data-intensive-apps]
aliases: [Brewer's theorem]
---
```

Permanent knowledge about a concept or entity. Cross-referenced to sources and other concepts via `[[wikilinks]]`.

### Source Summaries (`sources/<slug>.md`)

```yaml
---
title: "Brewer's CAP Theorem"
type: source
source_type: paper
author: "Eric Brewer"
url: "https://..."
source_date: 2000-07-01
ingested: 2026-05-23
tags: [distributed-systems]
concepts: [cap-theorem]
---
```

One per ingested source. Summarizes key claims and quotes. Backlinks to concept pages.

### Synthesis Pages (`syntheses/<slug>.md`)

```yaml
---
title: "CAP vs PACELC"
type: synthesis
created: 2026-05-23
updated: 2026-05-23
tags: [distributed-systems]
concepts: [cap-theorem, pacelc]
sources: [paper-cap, paper-pacelc]
---
```

Cross-cutting analyses generated from queries. These are what make the wiki compound — every good question leaves a permanent artifact.

---

## The Compounding Cycle

```
        ┌─────────────┐
        │             │
        ▼             │
   ┌──────────┐       │
   │  Ingest  │       │
   │  source  │       │
   └────┬─────┘       │
        │             │
        ▼             │
   ┌──────────┐       │
   │  Query   ├───────┘
   │  wiki    │  (answer filed
   └────┬─────┘   as synthesis)
        │
        ▼
   ┌──────────┐
   │  Lint    │  → finds gaps
   └────┬─────┘
        │
        ▼
   ┌──────────┐
   │  Find    │  → new sources
   │  sources │     to ingest
   └──────────┘
```

Each cycle enriches the wiki. Knowledge doesn't leak — it accumulates.

---

## Tips & Tricks

- **Obsidian Web Clipper** — browser extension that converts web articles to markdown. Best way to get sources into `raw/`.
- **Download images locally** — in Obsidian, set an attachment folder and bind a hotkey to download all images. Lets the LLM reference diagrams.
- **Graph view** — best way to see the shape of your wiki: hub pages, orphans, clusters.
- **Marp** — markdown-based slide decks. Obsidian has a plugin. Generate presentations from wiki content.
- **Dataview** — Obsidian plugin that runs SQL-like queries over YAML frontmatter. Dynamic tables and lists.
- **Git** — the wiki is just markdown files. Version history, branching, collaboration for free.
- **qmd** — local search engine for markdown with hybrid BM25/vector search. Useful when the wiki outgrows `index.md`.
- **Ingest one at a time** — stay involved. Read the summaries, check updates, guide the LLM on emphasis.
- **Run lint weekly** — catch contradictions before they accumulate.

---

## Credits

This pattern was originally described by **Andrej Karpathy** in his gist: [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

The idea is related in spirit to **Vannevar Bush's Memex** (1945) — a personal, curated knowledge store with associative trails between documents. The part Bush couldn't solve was who does the maintenance. The LLM handles that.

---

*Built for compounding knowledge. All markdown. Zero lock-in.*
