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
