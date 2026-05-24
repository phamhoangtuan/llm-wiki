# Activity Log

> Append-only record of wiki operations. Each entry starts with a date prefix.

---

## [2026-05-23] init | Wiki scaffolded

- Created repo structure: concepts/, sources/, syntheses/, raw/, meta/
- Created AGENTS.md (schema)
- Created index.md, log.md
- Created sample concept pages: [[concepts/wiki-maintenance]], [[concepts/knowledge-graph]]
- Created sample source: [[sources/sample-article]]
- No sources ingested yet. Ready for first ingest.

## [2026-05-23] ingest | Python Testing with pytest (Brian Okken)

- Source: Notion notes on "Python Testing with pytest (Second Edition)" by Brian Okken
- Copied to: raw/notes/okken-python-testing-pytest.html
- Created sources/okken-python-testing-pytest.md
- New concepts: pytest-basics, pytest-fixtures, pytest-parametrization, pytest-markers, pytest-mocking, pytest-plugins, pytest-configuration, pytest-assertions, pytest-test-results, testing-strategy
- Updated index.md: +12 concept entries, +1 source entry
- Total pages: 13

## [2026-05-23] ingest | Clean Code Cookbook (Maximiliano Contieri)

- Source: Notion notes on "Clean Code Cookbook" by Maximiliano Contieri
- Copied to: raw/notes/contieri-clean-code-cookbook.md
- Created sources/contieri-clean-code-cookbook.md
- New concepts: software-as-simulation, mapper-principles, bijection, rich-domain-model, tell-dont-ask, immutability, fail-fast, essential-accidental-complexity, technological-centaur, readability-vs-performance
- Updated index.md: +10 concept entries, +1 source entry
- Total pages: 23

## [2026-05-24] ingest | DuckDB: Up and Running (Wei-Meng Lee)

- Source: "DuckDB: Up and Running" by Wei-Meng Lee (ebook, 308 pages, finished 2026-05-24)
- Created sources/duckdb-up-and-running.html
- New concepts: duckdb, vectorized-execution, in-process-olap
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 35

## [2026-05-24] lint | Health check — fixed 15 broken links

- Broken links found: 15 across 5 files (wiki-maintenance, knowledge-graph, pytest-basics, software-as-simulation, sample-article)
- Fixed all by removing non-existent page references and rewriting surrounding text
- Orphans: 0 | Index coverage: complete | Stale claims: none
- Re-verified: all 36 pages link-clean

## [2026-05-24] ingest | Quick Insights on Materialized Views (Vu Trinh)

- Source: "Quick Insights on Materialized Views" by Vu Trinh (Substack, 2026-05-21)
- URL: https://vutr.substack.com/p/quick-insights-on-materialized-views
- Created sources/materialized-views-quick-insights.html
- New concepts: materialized-views, incremental-view-maintenance, timely-dataflow, differential-dataflow, dbsp
- Updated index.md: +5 concept entries, +1 source entry
- Total pages: 31

## [2026-05-23] migrate | Markdown → HTML conversion

- Converted all concept and source pages from .md to styled .html
- Created scripts/convert-to-html.py for automated conversion
- Updated AGENTS.md to prefer HTML output
- Updated index.md with clickable HTML links
- All pages now self-contained, styled, and interlinked
- Dark/light theme auto-detection on all pages

## [2026-05-24] review | Self-review — duplicate connection rendering

- Found: 12 .md files had `## Connections` section in body AND `---`-separated connection list, causing connections to render twice in HTML
- Root cause: html-to-md.py migration preserved original body connections as a heading+list, then converter also extracted the same connections from after `---`
- Fixed: Removed `## Connections` heading and body-duplicated connection list items from all 12 files, keeping only the `---`-separated list
- Affected: fail-fast, pytest-assertions, pytest-mocking, pytest-parametrization, readability-vs-performance, rich-domain-model, software-as-simulation, wiki-maintenance (concepts), contieri-clean-code-cookbook, duckdb-up-and-running, materialized-views-quick-insights, okken-python-testing-pytest (sources)
- Verified: 114 connection cards across 35 pages, no duplicates
- Note: 6 unrecognized connection types (Alternative, Builds on, Enabled by, Grounded in, Implements, Powered by) fall through to lenient fallback → rendered as "Related" — cosmetic, not a bug

## [2026-05-24] review | Self-review — missing connection separators

- Found: 2 .md files had `## Connections` section in body but NO `---` separator, so connections rendered as body content (h2 + ul/li) instead of connection cards
- Fixed: Added `---` separator before connections list in `knowledge-graph.md` and `sample-article.md`
- Also fixed: `knowledge-graph.md` "Core to the [[wiki-maintenance]]" → "Core to [[wiki-maintenance]] — the operational model" (proper regex match)
- Verified: 116 connection cards across 35 pages (was 114), all pages now have connection cards

## [2026-05-24] review | Self-review — multi-wikilink data loss

- Found: `pytest-basics.md` connection line had 3 wikilinks: `- Foundation for [[pytest-fixtures]] — , [[pytest-parametrization]], [[pytest-markers]]`
- Root cause: html-to-md.py migration merged multiple connections into one line; converter regex only captures first `[[...]]`
- Fixed: Split into 3 separate connection lines with proper descriptions
- Verified: 118 connection cards across 35 pages (was 116)
- Structural checks: all HTML files have consistent structure (hero, content-area, connections, footer), no broken cross-directory links, no unclosed tags, no wikilink orphans
- Note: 5 source files missing `updated` field in frontmatter (converter falls back to default)
