# Using llm-wiki with Obsidian

This wiki uses a **dual format**: markdown (`.md`) is the canonical source, HTML (`.html`) is auto-generated for GitHub Pages. Obsidian reads the `.md` files natively.

## Setup

1. **Open as vault**: In Obsidian, go to *Open another vault → Open folder as vault* and select this repo's root.
2. **Trust the vault**: On first open, Obsidian asks if you trust this vault. Select *Trust* to enable plugins.
3. **Install recommended plugins** (optional):
   - **[Dataview](obsidian://show-plugin?id=dataview)** — SQL-like queries over frontmatter
   - **[Obsidian Git](obsidian://show-plugin?id=obsidian-git)** — commit/push from within Obsidian

## Features

### Graph View

Click the graph icon in the left ribbon (or `Cmd+P` → "Open graph view"). The graph is pre-configured with color groups:

| Color | Group | Pages |
|---|---|---|
| Gold | pytest | All pytest-* concepts |
| Orange | Clean Code | MAPPER, bijection, domain model, etc. |
| Blue | Databases | DuckDB, MVs, vectorized execution |
| Red | Stream Processing | Timely Dataflow, Differential Dataflow, DBSP |

Use the **Local Graph** (`Cmd+P` → "Open local graph") to see connections within one or two hops of the current page — less noise than the full graph.

### Backlinks Panel

Open it from the right sidebar (link icon) or via `Cmd+P` → "Backlinks: Open backlinks for the current note".

The backlinks panel shows:
- **Linked mentions** — pages that explicitly `[[link]]` to this page
- **Unlinked mentions** — pages that mention the text without `[[brackets]]` (click to convert to an actual link)

### Quick Switcher

`Cmd+P` (or `Ctrl+P` on Windows/Linux) opens the command palette. Start typing a page name to fuzzy-search. Hit Enter to open.

This is the fastest way to navigate when you know what you're looking for.

### Dataview Queries

With the [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) plugin installed, you can run queries across your vault:

```dataview
TABLE tags, created
FROM "concepts"
WHERE contains(tags, "streaming")
SORT created DESC
```

```dataview
LIST
FROM "concepts"
WHERE length(sources) > 1
SORT updated DESC
```

These render as live-updating tables and lists in Obsidian.

### Canvas

Create a new Canvas via `Cmd+P` → "Canvas: New canvas". Drag notes onto the canvas to arrange them spatially, draw connections, add sticky notes.

Great for sense-making during complex ingests: layout the key concepts from a source, then the LLM synthesizes the permanent pages.

### Web Clipper

The [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension saves web pages as markdown files. Configure it to save into `raw/articles/`.

## Navigation Tips

| Goal | How |
|---|---|
| Find a page | `Cmd+P` → type name |
| Follow a link | Click `[[wikilink]]` (Cmd+click on Mac) |
| See what links here | Open Backlinks in right sidebar |
| See related pages | Local Graph (one or two hops) |
| Browse all | Graph View or File Explorer panel |
| Search all content | `Cmd+Shift+F` |

## How Editing Works

1. Edit `.md` files in Obsidian — add content, update frontmatter, create `[[wikilinks]]`
2. The LLM (OpenCode / Claude Code) handles content creation via AI
3. On push to `main`, GitHub Actions automatically runs `convert-to-html.py` to regenerate `.html` files
4. GitHub Pages serves the `.html` files at `phamhoangtuan.github.io/llm-wiki/`

## Rules

- **Edit `.md` files only.** Never hand-edit `.html` files — they're auto-generated.
- **Use `[[wikilinks]]`** for cross-references. This works in both Obsidian and the HTML output.
- Use `[[slug|Display Text]]` for display text: `[[timely-dataflow|Timely Dataflow]]`.
- Use `##` headings in markdown (not `#`).

## Troubleshooting

**Q: Graph view looks empty.**
A: Make sure you have `.md` files in `concepts/` and `sources/`. Obsidian only reads `.md` files.

**Q: `[[wikilinks]]` show as unresolved (dashed).**
A: The target page probably doesn't exist yet. Create it, or the link will still work — Obsidian just shows it as unresolved until you create the page.

**Q: My edits aren't showing on GitHub Pages.**
A: The CI build runs on push. Make sure to commit and push. If you're editing locally, run `uv run scripts/convert-to-html.py` manually first to verify the build works.

**Q: Dataview queries show no results.**
A: Make sure the Dataview plugin is installed and enabled (`Settings → Community Plugins → Dataview → Enable`).
