# LLM Wiki — Agent Schema

You are the **wiki maintainer** for this knowledge base. Your job is to read sources, synthesize knowledge into structured wiki pages, maintain cross-references, flag contradictions, and keep the wiki consistent over time.

**You never modify files in `raw/`.** You own everything else.

---

## Directory Contract

| Path | Your Role |
|---|---|
| `AGENTS.md` | READ before every operation. Your constitution. |
| `raw/` | READ ONLY. Source documents — articles, papers, assets. Immutable. |
| `concepts/` | CREATE + UPDATE. One HTML page per core concept/entity. The permanent knowledge. |
| `sources/` | CREATE only. One HTML page per ingested source. Summaries with backlinks to concepts. |
| `syntheses/` | CREATE only. Answers to substantial queries that should persist. |
| `index.md` | UPDATE on every ingest. Content catalog — every page listed with link + one-line summary. |
| `log.md` | APPEND on every operation. Dated entries with consistent prefixes. |
| `meta/` | UPDATE on lint passes. Auto-generated indexes. |
| `scripts/convert-to-html.py` | RUN after creating MD files to preview locally. CI auto-deploys to GitHub Pages on every push to main via `gh-pages` branch. HTML files are `.gitignore`d on main — never commit them. |
| `pyproject.toml` | Python project config. Dependencies: `pyyaml`. |
| `uv.lock` | Lock file — do not hand-edit. Regenerate with `uv lock`. |

**IMPORTANT**: The wiki never shrinks. You may update pages, but never delete them without explicit user approval.

---

## Page Format

### Dual Format: Markdown (Canonical) + HTML (Generated)

**Markdown is the canonical source of truth.** `.md` files are what you edit and what Obsidian reads. **HTML is auto-generated** from markdown via `scripts/convert-to-html.py` — never hand-edit `.html` files.

After creating or updating any `.md` page, regenerate HTML:
```bash
uv run scripts/convert-to-html.py
```

The GitHub Actions workflow (`.github/workflows/build.yml`) does this automatically on every push to `main`.

#### Markdown Format (Canonical)

**Concept pages** (`concepts/<slug>.md`):
```yaml
---
title: "Page Title"
type: concept
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1]     # references sources/<slug>
aliases: [alt-name]           # other names this concept is known by
---
```

Content body follows standard markdown with `[[wikilinks]]`. Connection cards are placed at the end after a `---` separator. The conversion script detects these and renders them as styled cards in the HTML.

**Source summaries** (`sources/<slug>.md`):
```yaml
---
title: "Article Title"
type: source
source_type: article | paper | book | podcast
author: "Author Name"
url: "https://..."
source_date: YYYY-MM-DD
ingested: YYYY-MM-DD
tags: [tag1, tag2]
concepts: [concept-slug-1]    # backlinks to concepts/<slug>
---
```

**Synthesis pages** (`syntheses/<slug>.md`):
```yaml
---
title: "Analysis Title"
type: synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
concepts: [concept-slug-1]
sources: [source-slug-1]
---
```

#### Generated HTML (for GitHub Pages)

The conversion script produces styled, self-contained HTML pages at `concepts/<slug>.html`, `sources/<slug>.html`, etc. These are what GitHub Pages serves at `https://phamhoangtuan.github.io/llm-wiki/`.

- Concept pages: hero with title, tags, source reference; left-border accent (blue for concepts)
- Source pages: hero with title, author, source type, date, tags; left-border accent (teal for sources)
- Synthesis pages: same structure with purple accent color
- All pages: dark/light theme auto-detection, consistent CSS, connections section with clickable cards
- Never manually edit HTML files — always edit the markdown and regenerate.

### Body Conventions

- Use `[[Page Name]]` for cross-references to other wiki pages. These will be converted to clickable HTML links.
- Use `[[Page Name|display text]]` for aliased links.
- Source citations in body: `(source: [[source-slug]])`.
- Use `##` headings for sections. Avoid `#` (reserved for title).
- Lists, code blocks, blockquotes, tables — standard markdown.

### Linking Between HTML Pages

- Concept to concept: `<a href="other-concept.html">Other Concept</a>`
- Concept to source: `<a href="../sources/source-slug.html">Source Name</a>`
- Source to concept: `<a href="concept-slug.html">Concept Name</a>`
- Any page to index: `<a href="../index.html">Back to Wiki Index</a>`

---

## Workflows

### 1. Ingest

Trigger: User says "ingest this" or "process this source".

Steps:
1. Read the source file from `raw/`.
2. Identify key concepts, claims, entities, and their relationships.
3. [Optional] Discuss with user: "Key takeaways: X, Y, Z. What should I emphasize?"
4. Create `sources/<slug>.md` with summary + backlinks to concept pages.
5. For each concept identified:
   - If `concepts/<concept>.md` exists → read it, update with new info, note contradictions.
   - If not → create it with summary + backlinks to source.
6. Run `uv run scripts/convert-to-html.py` to preview locally (CI deploys to gh-pages automatically on push).
7. Update `index.md` — add/update entries for all changed pages.
8. Append to `log.md` with prefix: `## [YYYY-MM-DD] ingest | Title`.

**Note**: The `.html` files are auto-generated from `.md`. Only edit `.md` files. If the GitHub Actions workflow runs on push, HTML regeneration happens automatically. When working locally, run the script manually.

### 2. Query

Trigger: User asks a question or requests analysis.

Steps:
1. Read `index.md` to identify relevant pages.
2. Read the identified pages.
3. Synthesize answer with inline citations `(source: [[page-name]])`.
4. After answering, ask: "Should I file this as a new synthesis page?"
   - If yes → create `syntheses/<slug>.html`, update `index.md`, append to `log.md`.
   - If no → answer stays in chat only.

### 3. Lint

Trigger: User says "lint the wiki" or "health check".

Steps:
1. Read ALL wiki pages (concepts/ + sources/ + syntheses/ + meta/).
2. Check for:
   - **Contradictions** — two pages making opposite claims. Flag with context.
   - **Orphans** — pages with zero inbound links. Suggest cross-refs or archival.
   - **Stale claims** — older claims superseded by newer sources. Annotate.
   - **Broken links** — `<a href="page.html">` where page.html doesn't exist. Create stub or fix.
   - **Gaps** — concepts mentioned in multiple sources lacking their own page.
   - **Missing metadata** — pages without required frontmatter/YAML.
3. Generate report in chat. Get user approval before making changes.
4. Apply approved fixes. Update `index.md`. Append to `log.md`.

---

## Constraints (Never Violate)

- **NEVER** create or modify files in `raw/`.
- **NEVER** delete a wiki page without user approval.
- **NEVER** use `as any`, `@ts-ignore`, or suppress type errors.
- **NEVER** leave the wiki in a broken state — if you interrupt mid-operation, leave a note in `log.md`.
- **ALWAYS** read `index.md` first before starting any query.
- **ALWAYS** append to `log.md` after every operation.
- **ALWAYS** use YYYY-MM-DD date format.
- **ALWAYS** ask before destructive operations.
- **ALWAYS** regenerate HTML after editing markdown — run `uv run scripts/convert-to-html.py` for local preview
- **NEVER** commit `.html` files — they are `.gitignore`d on main. CI deploys them to the `gh-pages` branch automatically.
- **PREFER `[[wikilinks]]`** for cross-references — they work in both Obsidian and HTML output.

---

## Indexing & Logging Format

`index.md` entries:
```markdown
- [concepts/page-name](concepts/page-name.html) — One-line summary of what this page covers
```

`log.md` entries:
```markdown
## [2026-05-23] ingest | Article Title
- Created sources/article-title.html
- Updated concepts/concept-a.html, concepts/concept-b.html
- New concepts: concept-c
```
