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

## [2026-05-24] ingest | System Design Interview – An Insider's Guide (Alex Xu)

- Source: "System Design Interview – An Insider's Guide" by Alex Xu (ebook, 252 pages, finished 2026-05-17)
- Copied to: raw/system-design-interview-xu.md (Vietnamese notes)
- Created sources/system-design-interview-xu.md
- New concepts: system-design-interview, scalable-architecture, load-balancer, database-replication, cache-strategy, cdn, stateless-architecture, message-queue, observability
- Updated index.md: +9 concept entries, +1 source entry
- Total pages: 45 (39 concepts + 6 sources)

## [2026-05-26] ingest | Benchmarking Vortex File Format vs Parquet, CSV

- Source: Daniel Beach (Data Engineering Central), Substack article published 2026-05-25
- URL: https://dataengineeringcentral.substack.com/p/benchmarking-vortex-file-format-vs
- Created sources/benchmarking-vortex-file-format.md
- New concepts: vortex-file-format, polars, apache-datafusion, apache-parquet, lance-file-format
- Updated concepts: duckdb (added benchmark source ref, vortex extension notes, Polars competitor connection)
- Updated index.md: +5 concept entries, +1 source entry
- Total pages: 51 (44 concepts + 7 sources)

## [2026-05-26] ingest | Hugo Data Ingestion Platform with Apache Flink (Grab Engineering)

- Source: Grab Engineering blog by Shuguang Xiang, Hung Nguyen, Hung Tran Viet, Shi Kai Ng (2026-05-22)
- URL: https://engineering.grab.com/one-click-data-ingestion-platform-with-apache-flink
- Created sources/hugo-data-ingestion-platform-flink.md
- New concepts: apache-flink, change-data-capture, data-ingestion, apache-kafka, apache-iceberg
- Updated concepts: message-queue (added Kafka reference and cross-link)
- Updated index.md: +5 concept entries, +1 source entry
- Total pages: 57 (49 concepts + 8 sources)

## [2026-05-28] ingest | Unlocking dbt (Cameron Cyr & Dustin Dorsey)

- Source: "Unlocking dbt: Design and Deploy Transformations in Your Cloud Data Warehouse" by Cameron Cyr & Dustin Dorsey (ebook, 351 pages, finished 2026-05-28)
- Copied to: raw/articles/unlocking-dbt-design-deploy-transformations.md (Vietnamese notes)
- Created sources/unlocking-dbt-design-deploy-transformations.md
- New concepts: dbt, analytics-engineer, elt
- Updated concepts: data-ingestion (added ELT/T reference, dbt in tooling landscape)
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 60 (52 concepts + 9 sources)

## [2026-05-28] ingest | Delta Grows Up: Writes, Unity Catalog, Time Travel (DuckDB Labs)

- Source: Ben Fleis (DuckDB Labs), republished on delta.io (2026-05-06)
- URL: https://delta.io/blog/2026-05-06-delta-grows-up-writes-time-travel-and-unity-catalog/
- Created sources/delta-grows-up-writes-unity-catalog.md
- New concepts: delta-lake, unity-catalog
- Updated concepts: duckdb (added Delta/UC extensions + source ref), apache-iceberg (added Delta Lake competitor connection)
- Updated index.md: +2 concept entries, +1 source entry
- Total pages: 62 (54 concepts + 10 sources)

## [2026-05-28] lint | Health check — fixed 3 broken wikilinks, 8 frontmatter issues, 2 near-orphans

- Broken wikilinks fixed: `apache-arrow`, `database-sharding` (created stub pages); `sources/` prefix removed in dbsp.md
- Frontmatter fixes: added `url` field to 7 source files (books got `""`, articles got actual URLs)
- Malformed dates fixed: duckdb-up-and-running (`308 pages` → `2024-05-24`), unlocking-dbt (`2025` → `2025-01-01`)
- Duplicate concepts cleaned: duckdb-up-and-running, materialized-views-quick-insights
- Near-orphan cross-references added: lance-file-format (from vortex-file-format), pytest-configuration + pytest-test-results (from pytest-basics)
- Omission fixed: duckdb.md now notes DataFusion's 5× CSV advantage
- Stub pages: apache-arrow, database-sharding (self-identified)
- Verified: 0 contradictions, 0 stale pages, 0 true orphans, index fully in sync
- New concepts: apache-arrow, database-sharding
- Total pages: 64 (56 concepts + 10 sources)

## [2026-05-31] ingest | Dependency Injection Principles, Practices, and Patterns (van Deursen & Seemann)

- Source: "Dependency Injection Principles, Practices, and Patterns" by Steven van Deursen & Mark Seemann (ebook, 643 pages, finished 2026-05-31)
- Copied to: raw/articles/dependency-injection-principles-patterns.md (Vietnamese notes)
- Created sources/dependency-injection-principles-patterns.md
- New concepts: dependency-injection, composition-root, solid-principles
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 69 (59 concepts + 11 sources)

## [2026-05-31] ingest | Delta Catalog-Managed Tables (Delta 4.1.0 + UC 0.4.0)

- Source: Benjamin Mathew, Scott Sandre, Scott Haines — delta.io blog (2026-02-02)
- URL: https://delta.io/blog/2026-02-02-delta-catalog-managed-tables/
- Created sources/delta-catalog-managed-tables.md
- New concepts: none (enriched existing)
- Updated concepts: delta-lake (catalog-managed architecture: discovery, reads via get_catalog_commits, writes via ratification, inline commits, convergence with Iceberg), unity-catalog (catalog commit protocol, get_catalog_commits API, staged vs inline commits, ratification/publishing)
- Updated index.md: +1 source entry
- Total pages: 70 (59 concepts + 12 sources)

## [2026-05-31] ingest | Learn Harness Engineering (walkinglabs)

- Source: "Learn Harness Engineering" by walkinglabs — online guide
- URL: https://walkinglabs.github.io/learn-harness-engineering/en/
- Copied to: raw/articles/learn-harness-engineering.md (Vietnamese notes)
- Created sources/learn-harness-engineering.md
- New concepts: harness-engineering
- Updated index.md: +1 concept entries, +1 source entry
- Total pages: 73 (60 concepts + 13 sources)

## [2026-05-31] lint | Cross-reference fixes

- Added backlinks to harness-engineering: technological-centaur, testing-strategy, fail-fast
- Added bidirectional cross-link: technological-centaur ↔ harness-engineering
- Added dependency-injection wikilink to pytest-fixtures
- Added dependency-injection and harness-engineering wikilinks to testing-strategy
- Added lakehouse tag to apache-iceberg
- Updated dates on all modified concept pages
- No new pages created

## [2026-06-02] ingest | Integrating the Rust Delta Kernel into ClickHouse + Debunking 8 Data Layout Myths

- Source 1: "Integrating the Rust Delta Kernel into ClickHouse" by Melvyn Peignon, Kseniia Sumarokova, Raul Marin (delta.io, 2026-05-18)
- Source 2: "Debunking 8 Data Layout Myths: Why Liquid Clustering Outperforms Partitioning" by Jeffrey Gong, Yu Xu, Rahul Mahadev (Databricks, 2026-06-01)
- Created sources/integrating-rust-delta-kernel-clickhouse.md
- Created sources/debunking-data-layout-myths-liquid-clustering.md
- New concepts: clickhouse, delta-kernel, liquid-clustering
- Updated concepts: delta-lake (Delta Kernel, Liquid Clustering, CDF sections), apache-iceberg (Liquid Clustering note), change-data-capture (ClickHouse CDF/ClickPipes), apache-parquet (file statistics, data skipping context)
- Updated index.md: +3 concept entries, +2 source entries
- Total pages: 78 (63 concepts + 15 sources)
