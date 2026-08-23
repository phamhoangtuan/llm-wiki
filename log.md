# Activity Log

> Append-only record of wiki operations. Each entry starts with a date prefix.

---

## [2026-08-23] lint | Post-ingest link fix pass

- Fixed 10 Title Case wikilinks → kebab-case slugs across 4 files (algorithm-analysis, big-o-notation, time-space-tradeoff, learning-algorithms-heineman)
- Broken wikilinks: 10 → 0
- Orphans: 6 (pre-existing, unchanged — data-architecture, data-security, data-warehousing, document-content-management, flow-zone-critique, master-data-management)
- Frontmatter: all pages complete
- Index: 350 pages (253 concepts + 97 sources) — consistent with disk
- Contradictions: 0
- HTML regenerated via convert-to-html.py

## [2026-08-23] ingest | Learning Algorithms — George T. Heineman

- Created sources/learning-algorithms-heineman.md
- New concepts: algorithm-analysis, big-o-notation, time-space-tradeoff
- Cross-linked to: complexity-metrics, readability-vs-performance, scalable-architecture, essential-accidental-complexity
- Updated index.md: +3 concepts, +1 source, 350 total pages
- HTML regenerated via convert-to-html.py

## [2026-08-15] chore | Allow raw documents in commit helper

- Updated `scripts/commit-and-push.sh` to include tracked and untracked files under `raw/`; raw documents remain immutable to wiki operations but are now versioned by the commit workflow

## [2026-08-15] chore | Add commit-and-push helper

- Created `scripts/commit-and-push.sh` to stage all non-raw changes, validate the index, commit with a supplied message, and push the current branch to `origin`
- Validated with `bash -n` and the missing-message guard; no commit or push executed

## [2026-08-15] lint | Fixed stale index.html concept count

- Root cause: `update_index_html()` in scripts/convert-to-html.py used a regex `<!-- MOC_DESC -->.*?</p>` without `re.DOTALL`, so it never matched across the newline before `</p>` — the count silently stayed stale
- Fix: added `flags=re.DOTALL` to the MOC_DESC substitution
- index.html count corrected: "202 concepts" → "246 concepts across 11 categories"

## [2026-08-15] lint | Post-ingest health check + fix pass

- Scanned 337 pages (246 concepts + 91 sources) across broken wikilinks, orphans, and frontmatter completeness
- Fixed 103 broken wikilinks (Title Case → kebab-case slug) across 23 concept pages — pre-existing from the 2026-07-14 DAMA + Software Architecture: The Hard Parts batch
- Broken wikilinks: 103 → 0
- Orphans reduced: 19 → 6. Remaining 6 (data-architecture, data-security, data-warehousing, document-content-management, flow-zone-critique, master-data-management) have frontmatter-only backlinks via their source pages' `concepts:` field — not true orphans
- Frontmatter: all 8 new pages complete; no new gaps; 0 contradictions introduced
- HTML regenerated via convert-to-html.py

## [2026-08-15] ingest | AI Engineering + Clean Code + Engineering Management + Fundamentals of Data Observability + Start With Why

- Created sources/ai-engineering-chip-huyen.md, sources/clean-code-martin.md, sources/engineering-management-drasner.md, sources/fundamentals-of-data-observability.md, sources/start-with-why-sinek.md
- Created concepts/ai-engineering.md (from AI Engineering), concepts/engineering-management.md (from Engineering Management for the Rest of Us), concepts/golden-circle.md (from Start With Why)
- Updated concepts/data-observability.md (three channels, observations model, expectations & circuit breakers from Petrella)
- Updated concepts/solid-principles.md, concepts/code-quality-pillars.md, concepts/tdd-methodology.md (clean-code-martin backlink)
- Updated concepts/ai-native-engineering.md, concepts/technical-leadership.md (cross-links to new concepts)
- Updated index.md: +3 concepts, +5 sources, 337 total pages
- HTML regenerated via convert-to-html.py

## [2026-07-14] ingest | #ENTRYLEVELBOSS + DAMA-DMBOK + Software Architecture: The Hard Parts + The Clean Coder

- Created sources/entrylevelboss.md, sources/dama-dmbok-2nd-edition.md, sources/software-architecture-hard-parts.md, sources/the-clean-coder.md
- Created concepts/job-search-strategy.md, concepts/networking-theory.md, concepts/personal-branding.md (from #ENTRYLEVELBOSS)
- Created concepts/data-architecture.md, concepts/data-security.md, concepts/data-integration.md, concepts/metadata-management.md, concepts/master-data-management.md, concepts/data-warehousing.md, concepts/document-content-management.md, concepts/data-storage-operations.md (from DAMA-DMBOK)
- Created concepts/architecture-quantum.md, concepts/static-vs-dynamic-coupling.md, concepts/architecture-fitness-functions.md, concepts/data-mesh.md, concepts/saga-pattern.md, concepts/decomposition-patterns.md, concepts/data-sovereignty.md (from Software Architecture: The Hard Parts)
- Created concepts/software-professionalism.md, concepts/saying-no.md, concepts/testing-pyramid.md, concepts/mentoring.md, concepts/flow-zone-critique.md (from The Clean Coder)
- Updated index.md: +23 concepts, +4 sources, 314 total pages

---

## [2026-08-06] ingest | Graph Engineering: The Karpathy Loop, Improved 1000x by Itself

- Created sources/graph-engineering-karpathy.md
- Created concepts/graph-engineering.md — umbrella: vibe coding → agentic engineering → graph engineering
- Created concepts/autoresearch.md — Karpathy's ratchet loop, program.md, 4 conditions for autonomous loops
- Created concepts/agent-hub.md — agent-first collaboration, commit DAG, CLI as graph interface
- Created concepts/dynamic-workflows.md — Anthropic's generated JavaScript orchestration, up to 1,000 sub-agents
- Created concepts/graph-grounding.md — constraining agents with graph facts, structured evaluation
- Created concepts/software-3.md — Karpathy's Software 3.0: prompts as programmable interface
- Created concepts/entity-resolution.md — model-based canonical entity mapping for knowledge graphs
- Updated concepts/agent-loop.md — added autoresearch as concrete implementation, ratchet loop section
- Updated concepts/knowledge-graph.md — added agent shared memory, grounding layer, construction pipeline sections
- Updated concepts/vibe-coding.md — added Karpathy's 3-stage progression to graph engineering
- Updated index.md — added 8 new concept entries + 1 source entry

## [2026-08-06] ingest | Fluent Python + Staff Engineer (Larson) + Tyranny of Metrics

- Created sources/fluent-python.md — Luciano Ramalho's 1,831-page Python guide
- Created sources/staff-engineer-larson.md — Will Larson's 215-page Staff+ guide
- Created sources/tyranny-of-metrics.md — Jerry Z. Muller's 233-page critique of metric fixation
- Created concepts/python-data-model.md — Python's unifying object model, dunder methods, protocols, goose typing
- Created concepts/pythonic-code.md — Python idioms, duck typing, "use what's available"
- Created concepts/metric-fixation.md — dysfunctional dominance of metrics over judgment, goal displacement, gaming
- Created concepts/goodharts-law.md — "When a measure becomes a target, it ceases to be a good measure"
- Updated index.md — added 4 concept + 3 source entries

## [2026-08-06] lint | Health check

- Broken wikilinks: 0 — all 223 wikilinks resolve correctly
- Orphan concepts: 0 — all concept pages have at least one inbound link
- Missing tags: 0
- Missing sources (expected): 82 source pages (sources don't need a sources field)
- Status: clean
- Updated index.md — added 4 concept + 3 source entries

## [2026-07-14] lint | Post-ingest health check

- Scanned all 291 wiki pages (209 concepts + 82 sources) across 5 lint dimensions
- **Broken wikilinks**: 0 found — all wikilinks resolve correctly
- **Frontmatter**: all concept and source pages have required fields (title, type, created/ingested, sources/concepts)
- **Orphans**: 0 true orphans — all concept pages have ≥1 inbound link from another page; 30 near-orphans (1 inbound) including 7 newly created concepts (expected)
- **Unindexed pages**: found 5 (1 concept + 4 sources) — all 5 added to index.md
  - concept: software-construction (from Code Complete ingest on 2026-07-13)
  - sources: code-complete, dive-into-design-patterns, game-theory-bonanno, head-first-software-architecture
- **Contradictions**: 0 found — new content (DataOps, stream processing, observability) is complementary to existing pages
- **Gaps**: no unreferenced concepts in source frontmatter — all sources' concepts: arrays resolve to existing concept pages
- Fixed: added 5 missing entries to index.md; regenerated HTML
- Total pages: 291 (209 concepts + 82 sources)

---

## [2026-07-14] ingest | 5 books batch

- Created sources/500-lines-or-less.md — AOSA vol.4: design decisions "in the small"
- Created sources/becoming-data-head.md — Gutman & Goldmeier on statistical thinking for non-technical professionals
- Created sources/data-observability-for-data-engineering.md — Pinto & El Khammal on pipeline transparency, lineage, and incident management
- Created sources/practical-dataops.md — Atwal's Lean/Agile/DevOps integration for data product delivery
- Created sources/streaming-systems.md — Akidau's definitive framework: 4 questions, watermarks, stream-table duality
- New concepts: data-observability, watermarks, stream-table-duality, statistical-thinking, data-head, t-shaped-skills, data-product
- Updated concepts: dataops (Lean/Agile/DevOps foundations, DataOps Factory, Minimum Viable DataOps), stream-processing (4 questions, streaming ⊃ batch, stream-table duality, watermarks), observability (data observability cross-reference)
- Updated index.md (208 concepts + 78 sources = 286 pages)

---

## [2025-07-23] redesign | Hallmark Cobalt theme

- Redesigned styles/main.css: OKLCH palette (anchor hue 250), Space Grotesk + Inter + JetBrains Mono font pairing, 4pt spacing scale, SVG icons, reduced motion
- Updated scripts/convert-to-html.py: SVG icon buttons, page footer on every page
- Updated scripts/js/theme.js: sun/moon SVG icon swap
- Updated index.html: new design system, footer
- Regenerated all 194 concept HTML pages + syntheses

## [2025-07-23] lint | Orphan fix

- Fixed orphan source: architecture-of-open-source-applications-vol2 now referenced by risk-driven-architecture, architectural-characteristics, design-patterns, architectural-decision-records

## [2026-07-13] ingest | KubeSchool — Understanding Kubernetes (Architectural Primer)

- Source: Portainer's KubeSchool — 15-chapter web primer on Kubernetes architecture, principles, and sharp edges
- Created sources/kubeschool-kubernetes-primer.md
- New concepts: kubernetes-architecture, kubernetes-networking, kubernetes-security
- Updated concepts: kubernetes-operator (+cross-ref to kubernetes-architecture)
- Regenerated HTML via convert-to-html.py
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 274 (201 concepts + 73 sources)

## [2026-07-13] ingest | Fundamentals of Data Engineering, Introduction to ML Systems, Architecture of OSS Vol II, The Art of Readable Code, The Staff Engineer's Path

- Source 1: "Fundamentals of Data Engineering" by Joe Reis & Matt Housley (ebook, 446 pages, finished 2026-03-22)
- Source 2: "Introduction to Machine Learning Systems" by Vijay Janapa Reddi (ebook, 2,020 pages, finished 2026-03-16)
- Source 3: "The Architecture of Open Source Applications, Volume II" by Amy Brown & Greg Wilson (ebook, 390 pages, finished 2026-03-25)
- Source 4: "The Art of Readable Code" by Dustin Boswell & Trevor Foucher (ebook, 198 pages, finished 2026-03-18)
- Source 5: "The Staff Engineer's Path" by Tanya Reilly (ebook, 368 pages, finished 2026-03-21)
- Created sources/fundamentals-of-data-engineering.md, sources/introduction-to-machine-learning-systems.md, sources/architecture-of-open-source-applications-vol2.md, sources/art-of-readable-code.md, sources/staff-engineers-path.md
- New concepts: code-readability, machine-learning-systems, mlops, sustainable-ai, ai-scaling-laws, compound-ai-systems, lindy-effect, staff-plus-archetypes, technical-leadership
- Updated concepts: data-engineering-fundamentals (+Lifecycle framework, 6 undercurrents, Data Maturity Model), staff-engineering (+Staff+ fork, 3 Pillars, humaning skills, mental models)
- Regenerated HTML via convert-to-html.py
- Updated index.md: +9 concept entries, +5 source entries
- Total pages: 270 (198 concepts + 72 sources)

## [2026-07-13] ingest | Big Book of Data Engineering, Code Complete, Dive Into Design Patterns, Game Theory (Bonanno), Head First Software Architecture

- Source 1: "Big Book of Data Engineering" by Databricks (ebook, 125 pages, finished 2026-04-10)
- Source 2: "Code Complete (2nd Edition)" by Steve McConnell (ebook, 1,271 pages, finished 2026-03-27)
- Source 3: "Dive Into Design Patterns" by Alexander Shvets (ebook, 410 pages, finished 2026-04-02)
- Source 4: "Game Theory: An Open Access Textbook" by Giacomo Bonanno (ebook, 585 pages, finished 2026-04-04)
- Source 5: "Head First Software Architecture" by Gandhi, Richards & Ford (ebook, 486 pages, finished 2026-04-07)
- Copied to: raw/big-book-data-engineering.md, raw/code-complete.md, raw/dive-into-design-patterns.md, raw/game-theory-bonanno.md, raw/head-first-software-architecture.md
- Created sources/big-book-data-engineering.md, sources/code-complete.md, sources/dive-into-design-patterns.md, sources/game-theory-bonanno.md, sources/head-first-software-architecture.md
- New concepts: medallion-architecture, delta-live-tables, software-construction, information-hiding, design-patterns, game-theory, nash-equilibrium, architectural-characteristics, architectural-decision-records
- Updated concepts: data-lakehouse (+Medallion section, big-book source), databricks-platform (+DLT, DatabricksIQ, big-book source), data-quality-monitoring (+DLT expectations, big-book source), essential-accidental-complexity (+construction, information-hiding, code-complete source), code-quality-pillars (+software-construction, information-hiding, code-complete source), risk-driven-architecture (+4D puzzle, two laws, architectural-characteristics, ADRs, head-first source), architecture-hoisting (+ADRs connection), microservices (+architectural-characteristics), solid-principles (+design-patterns, dive-into-design-patterns source), object-oriented-design (+design-patterns, dive-into-design-patterns source)
- Regenerated HTML via convert-to-html.py
- Updated index.md: +9 concept entries, +5 source entries
- Total pages: 257 (190 concepts + 67 sources)

## [2026-07-13] ingest | Data Algorithms, Hands-On Large Language Models, The Art of Functional Programming

- Source 1: "Data Algorithms" by Mahmoud Parsian (ebook, 778 pages, finished 2026-04-14)
- Source 2: "Hands-On Large Language Models" by Jay Alammar (ebook, 431 pages, finished 2026-04-13)
- Source 3: "The Art of Functional Programming" by Minh Quang Tran, PhD (ebook, 205 pages, finished 2026-04-11)
- Created sources/data-algorithms.md, sources/hands-on-large-language-models.md, sources/the-art-of-functional-programming.md
- New concepts: market-basket-analysis, kv-caching, lora, flash-attention, peft, reranking, functional-programming
- Updated concepts: apache-spark (+MBA section, Spark-for-MBA pipeline), model-quantization (+GGUF format, new source), fine-tuning (+PEFT methods, Prefix Tuning, LoRA cross-refs, new source), retrieval-augmented-generation (+reranking dependency, LoRA specialization, new source), immutability (+FP pillar connection, architecture-hoisting, new source)
- Regenerated HTML via convert-to-html.py
- Updated index.md: +7 concept entries, +3 source entries
- Total pages: 244 (181 concepts + 63 sources)

## [2026-07-13] lint | Post-ingest health check + fix pass

- Scanned all 257 wiki pages (190 concepts + 67 sources) across 5 lint dimensions
- Broken wikilinks: 1 found → 0 remaining
  - Fixed: sources/big-book-data-engineering.md `[[auto-loader]]` → plain text (Databricks-specific tool, doesn't warrant concept page)
- Orphans: 0 — all pages have at least 1 inbound link
- Near-orphans (1 inbound link): 12 — consistent with historical patterns (many are niche/recent pages):
  - ai-psychosis, apache-arrow, bloom-filter, data-scientist, http-evolution, knowledge-graph, market-basket-analysis, python-repl, redis, reranking, shift-left-security, snowflake-id
- Frontmatter: 0 issues — all 257 pages have complete frontmatter (title, created, updated, sources/concepts)
- Stale pages: 3 (cdn, load-balancer, stateless-architecture — last updated 2026-05-24, from initial system-design-interview ingest)
  - Deferred: these pages are structurally sound but could benefit from cross-reference enrichment
- Contradictions: 0 found — high-tag-overlap pairs reviewed, no conflicting claims detected
- Source concept refs without pages: 0 — all concepts listed in source frontmatter resolve to existing pages
- Regenerated HTML via convert-to-html.py
- Updated log.md

## [2026-07-11] ingest | Building LLMs for Production, Real-Time Analytics, Data Engineering with Python, Snowflake, Apache Flink

- Source 1: "Building LLMs for Production" by Peters & Bouchard (ebook, 423 pages, finished 2026-04-21)
- Source 2: "Building Real-Time Analytics Systems" by Mark Needham (ebook, 221 pages, finished 2026-04-26)
- Source 3: "Data Engineering with Python" by Paul Crickard (ebook, 299 pages, finished 2026-04-22)
- Source 4: "Snowflake: The Definitive Guide" by Joyce Kay Avila (ebook, 467 pages, finished 2026-04-24)
- Source 5: "Stream Processing with Apache Flink" by Fabian Hueske (ebook, 318 pages, finished 2026-04-27)
- Created sources/building-llms-for-production.md, sources/building-real-time-analytics-systems.md, sources/data-engineering-with-python.md, sources/snowflake-the-definitive-guide.md, sources/stream-processing-apache-flink.md
- New concepts: prompt-engineering, retrieval-augmented-generation, fine-tuning, model-distillation, model-quantization, model-pruning, llm-evaluation-metrics, real-time-analytics, lambda-architecture, kappa-architecture, stream-processing, apache-airflow, snowflake-data-cloud, event-time-processing, stateful-stream-processing, windowing
- Updated concepts: apache-flink (+ stream-processing, event-time-processing, stateful-stream-processing, windowing links), apache-kafka (+ real-time-analytics, stream-processing, lambda/kappa links), data-engineer (+ apache-airflow, real-time-analytics), clickhouse (+ real-time-analytics), data-lakehouse (+ lambda-architecture, kappa-architecture, snowflake-data-cloud), observability (+ llm-evaluation-metrics)
- Regenerated HTML via convert-to-html.py
- Updated index.md: +16 concept entries, +5 source entries
- Total pages: 228 (169 concepts + 59 sources)

## [2026-07-11] lint | Post-ingest health check + fix pass

- Scanned all 233 wiki pages (174 concepts + 59 sources) across 5 lint dimensions
- Broken wikilinks: 6 found → 0 remaining
  - Created concepts/apache-druid.md (linked from building-real-time-analytics-systems.md)
  - Created concepts/apache-pinot.md (linked from building-real-time-analytics-systems.md)
  - Created concepts/batch-processing.md (linked from real-time-analytics.md, 2 refs)
  - Created concepts/edge-computing.md (linked from building-real-time-analytics-systems.md, 2 refs)
  - Created concepts/langchain.md (linked from building-llms-for-production.md)
  - Created concepts/llama-index.md (linked from building-llms-for-production.md)
- Title-style wikilinks: 0 found (all use slug-style format)
- Orphans: 0 true orphans
- Near-orphans: 9 pages with 1 inbound link (deferred): ai-psychosis, architecture-in-agile, bloom-filter, feedback, http-evolution, python-repl, redis, shift-left-security, snowflake-id
- Frontmatter: all 6 new stub pages have complete frontmatter
- Regenerated HTML via convert-to-html.py
- Updated index.md: +6 concept entries, page count 228 → 233
- Total pages: 233 (174 concepts + 59 sources)

## [2026-06-26] lint | Post-ingest link hygiene pass

- Health score: 85→92/100
- Fixed: 1 fully broken wikilink → `[[agentic-development-life-cycle]]` in architecture-in-agile.md
- Fixed: 27 title-style wikilinks → slug-style across 4 new concept pages (architecture sub-wiki)
- Fixed: 22 title-style wikilinks → slug-style across 6 ultralearning sub-wiki pages
- Fixed: 2 title-style wikilinks → slug-style in distributed-consensus.md, leader-election.md (`[[apache-kafka]]`)
- Fixed: 50 index.md source links → `.html` changed to `.md` (source HTML not generated by design)
- Added backlinks: database-sharding.md → database-isolation, snowflake-id; database-replication.md → database-isolation, database-isolation.md → database-replication
- All title-style wikilinks now use `[[slug|Display Name]]` format — works in both Obsidian and HTML

## [2026-06-27] ingest | How AI Changes 4 Core Data Roles (Madison Mae)

- Source: Article on how AI reshapes 4 data roles (Data Analyst, Data Engineer, Data Scientist, Analytics Engineer)
- Created sources/how-ai-changes-4-core-data-roles.md
- New concepts: data-analyst, data-scientist, self-service-analytics
- Updated concepts: analytics-engineer (AI impact section), data-engineer (AI impact section), semantic-layer (new backlinks + sources)
- Updated index.md: +4 entries (3 concepts + 1 source), updated 3 existing entries
- Total pages: 195 (144 concepts + 51 sources)

## [2026-06-26] ingest | Just Enough Software Architecture (George Fairbanks)

- Source: Book notes on "Just Enough Software Architecture: A Risk-Driven Approach" by George Fairbanks (378 pages)
- Created sources/just-enough-software-architecture-fairbanks.md
- New concepts: risk-driven-architecture, architecture-hoisting, model-code-gap, architecture-in-agile
- Updated index.md: +5 entries (4 concepts + 1 source)
- Total pages: 190 (140 concepts + 50 sources)

## [2026-06-25] ingest | Ultralearning (Scott Young)

- Source: Book notes on "Ultralearning" by Scott Young (250 pages)
- Copied to: raw/notes/ultralearning-scott-young.md
- Created sources/ultralearning-scott-young.md
- New concepts: ultralearning, metalearning, spaced-repetition, testing-effect, directness, feedback
- Updated index.md: +6 entries (6 concepts + 1 source)
- Total pages: 185
- Post-ingest lint: fixed 2 broken wikilinks (Directness, Feedback) → created concept pages

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
- URL: <https://vutr.substack.com/p/quick-insights-on-materialized-views>
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
- URL: <https://dataengineeringcentral.substack.com/p/benchmarking-vortex-file-format-vs>
- Created sources/benchmarking-vortex-file-format.md
- New concepts: vortex-file-format, polars, apache-datafusion, apache-parquet, lance-file-format
- Updated concepts: duckdb (added benchmark source ref, vortex extension notes, Polars competitor connection)
- Updated index.md: +5 concept entries, +1 source entry
- Total pages: 51 (44 concepts + 7 sources)

## [2026-05-26] ingest | Hugo Data Ingestion Platform with Apache Flink (Grab Engineering)

- Source: Grab Engineering blog by Shuguang Xiang, Hung Nguyen, Hung Tran Viet, Shi Kai Ng (2026-05-22)
- URL: <https://engineering.grab.com/one-click-data-ingestion-platform-with-apache-flink>
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
- URL: <https://delta.io/blog/2026-05-06-delta-grows-up-writes-time-travel-and-unity-catalog/>
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
- URL: <https://delta.io/blog/2026-02-02-delta-catalog-managed-tables/>
- Created sources/delta-catalog-managed-tables.md
- New concepts: none (enriched existing)
- Updated concepts: delta-lake (catalog-managed architecture: discovery, reads via get_catalog_commits, writes via ratification, inline commits, convergence with Iceberg), unity-catalog (catalog commit protocol, get_catalog_commits API, staged vs inline commits, ratification/publishing)
- Updated index.md: +1 source entry
- Total pages: 70 (59 concepts + 12 sources)

## [2026-05-31] ingest | Learn Harness Engineering (walkinglabs)

- Source: "Learn Harness Engineering" by walkinglabs — online guide
- URL: <https://walkinglabs.github.io/learn-harness-engineering/en/>
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

## [2026-06-03] ingest | Go Web Programming (Sau Sheong Chang) + Test-Driven Development with Python, 2nd Ed. (Harry Percival)

- Source 1: "Go Web Programming" by Sau Sheong Chang (ebook, 314 pages, finished 2026-06-02)
- Source 2: "Test-Driven Development with Python, 2nd Edition" by Harry J.W. Percival (ebook, 662 pages, finished 2026-06-03)
- Copied to: raw/articles/go-web-programming.md, raw/articles/tdd-python-percival.md
- Created sources/go-web-programming.md
- Created sources/tdd-python-percival.md
- New concepts: goroutines, go-http-handlers, go-template-escaping, go-web-ecosystem, tdd-methodology, functional-testing
- Updated concepts: testing-strategy (added TDD/functional testing refs + source), fail-fast (added TDD fail-early connection + source)
- Updated index.md: +6 concept entries, +2 source entries
- Total pages: 87 (69 concepts + 17 sources)

## [2026-06-05] ingest | Apache Iceberg 1.11.0 Release

- Source: Apache Iceberg PMC blog post (2026-05-19)
- URL: <https://iceberg.apache.org/blog/apache-iceberg-1.11.0-release/>
- Created sources/apache-iceberg-1.11.0-release.md
- Updated concepts: apache-iceberg (major rewrite: V3 spec stabilization, table encryption, File Format API, server-side scan planning, SQL UDFs, engine support matrix), apache-flink (DynamicIcebergSink, Flink 2.1, post-commit maintenance, branch compaction, type support)
- Updated index.md: +1 source entry, updated 2 concept summaries
- Total pages: 88 (69 concepts + 18 sources)

## [2026-06-05] lint | Comprehensive health check + fix pass

- Scanned all 87 wiki pages across 5 lint dimensions (wikilinks, orphans, frontmatter, contradictions, stubs)
- Fixed 13 broken wikilinks: added `sources/` prefix to source references across 19 concept files (apache-flink, apache-iceberg, apache-datafusion, liquid-clustering, delta-lake, composition-root, duckdb, clickhouse, dbsp, analytics-engineer, database-sharding, delta-kernel, apache-kafka, change-data-capture, data-ingestion, vortex-file-format, polars, apache-parquet, unity-catalog)
- Fixed inverted wikilink syntax in wiki-maintenance.md: `[[sample-article|sources/sample-article]]` → `[[sources/sample-article|sample-article]]`
- Added backlinks from 20 concept pages to their 5 orphan source pages (contieri-clean-code-cookbook, okken-python-testing-pytest, go-web-programming, learn-harness-engineering, tdd-python-percival)
- Fixed broken markdown table in testing-strategy.md: split merged 4 Pillars and Layer tables with proper separator
- Added missing `iceberg` extension row to duckdb.md's ecosystem extension table
- Fixed Deletion Vectors misattribution in apache-iceberg.md comparison table: Delta changed from ✅ to ❌ (file rewriting) to distinguish from Iceberg's Roaring-bitmap mechanism
- HTML regenerated via convert-to-html.py
- No new pages created

## [2026-06-08] ingest | Cracking the Coding Interview, Good Code Bad Code, Seriously Good Software

- Source 1: "Cracking the Coding Interview, 6th Edition" by Gayle Laakmann McDowell (ebook, 708 pages, finished 2026-05-16)
- Source 2: "Good Code, Bad Code" by Tom Long (ebook, 338 pages, finished 2026-05-13)
- Source 3: "Seriously Good Software" by Marco Faella (ebook, 330 pages, finished 2026-05-15)
- Copied to: raw/articles/cracking-the-coding-interview.md, raw/articles/good-code-bad-code.md, raw/articles/seriously-good-software.md
- Created sources/cracking-the-coding-interview.md, sources/good-code-bad-code.md, sources/seriously-good-software.md
- New concepts: technical-interview, code-quality-pillars, software-quality-dimensions
- Updated concepts: readability-vs-performance (added quality pillars + dimensions refs), testing-strategy (added quality pillars ref), essential-accidental-complexity (added YAGNI + abstraction refs), fail-fast (added no-surprises/hard-to-misuse refs), system-design-interview (added technical-interview complementary link)
- Updated index.md: +3 concept entries, +3 source entries
- Total pages: 94 (72 concepts + 21 sources)

## [2026-06-08] ingest | Data Engineering with dbt, Practical Object-Oriented Design, Programming Kubernetes

- Source 1: "Data Engineering with dbt" by Roberto Zagni (ebook, 603 pages, finished 2026-05-08)
- Source 2: "Practical Object-Oriented Design, 2nd Edition" by Sandi Metz (ebook, 334 pages, finished 2026-05-09)
- Source 3: "Programming Kubernetes" by Stefan Schimanski & Michael Hausenblas (ebook, 244 pages, finished 2026-05-07)
- Copied to: raw/articles/data-engineering-with-dbt.md, raw/articles/practical-object-oriented-design.md, raw/articles/programming-kubernetes.md
- Created sources/data-engineering-with-dbt.md, sources/practical-object-oriented-design.md, sources/programming-kubernetes.md
- New concepts: dataops, object-oriented-design, kubernetes-operator
- Updated concepts: dbt (added DataOps backlink + source), analytics-engineer (added DataOps backlink + source), solid-principles (added OO-design foundation backlink), tell-dont-ask (added OO-design messages backlink), code-quality-pillars (added TRUE/DataOps connections), software-quality-dimensions (added design-as-discovery connection), elt (added source), go-web-ecosystem (added K8s operator link), goroutines (added K8s controller concurrency link), observability (added operator metrics/traces link)
- Updated index.md: +3 concept entries, +3 source entries
- Total pages: 100 (75 concepts + 24 sources)

## [2026-06-08] lint | Comprehensive health check + fix pass

- Scanned all 100 wiki pages across 5 lint dimensions (broken wikilinks, orphans, frontmatter, contradictions, knowledge gaps)
- Fixed 3 broken wikilinks: added `sources/` prefix to `lance-file-format.md`, `vectorized-execution.md`, `in-process-olap.md`
- Fixed 4 invalid `source_type` values: `notes`/`ebook` → `book` across contieri-clean-code-cookbook, okken-python-testing-pytest, duckdb-up-and-running, system-design-interview-xu
- Added missing `created`/`updated` frontmatter fields to all 24 source files
- Created concepts/middleware-pattern.md — gap: declared in go-web-programming.md source frontmatter but no concept page existed
- Orphans: 4 concept pages (apache-arrow, database-sharding, go-template-escaping, knowledge-graph) + 10 source pages with only 1 inbound link — low priority, no 0-count orphans
- Contradictions: 0 found after systematic examination of 30+ concept page pairs
- Updated index.md: +1 concept entry
- Total pages: 101 (76 concepts + 24 sources)

## [2026-06-08] ingest | Data Engineer Role — Data Engineering Handbook

- Source: "Data Engineer Role" from Data Engineering Handbook (kythuatdulieu.github.io)
- URL: <https://kythuatdulieu.github.io/concepts/foundation/data-engineer-role/>
- Copied to: raw/articles/data-engineer-role.md
- Created sources/data-engineer-role-handbook.md
- New concepts: data-engineer
- Updated index.md: +1 concept entry, +1 source entry
- Total pages: 102 (77 concepts + 25 sources)

## [2026-06-08] ingest | Semantic Layers (Madison Mae), Senior→Staff Engineer (Jordan Cutler), Databricks Zerobus (Daniel Beach)

- Source 1: "I was wrong about semantic layers" by Madison Mae (Learn Analytics Engineering, 2026-06-11)
- Source 2: "How to Grow From Senior to Staff Engineer in the AI Era" by Jordan Cutler & Gregor Ojstersek (Engineering Leadership, 2026-06-07)
- Source 3: "Databricks Zerobus — Event Streams + Lake House" by Daniel Beach (Data Engineering Central, 2026-06-01)
- Created sources/semantic-layers-for-ai.md, sources/senior-to-staff-engineer.md, sources/databricks-zerobus.md
- New concepts: semantic-layer, staff-engineering
- Updated index.md: +2 concept entries, +3 source entries
- Total pages: 104 (79 concepts + 28 sources)

## [2026-06-08] ingest | Data Engineering — Data Engineering Handbook

- Source: "Data Engineering" from Data Engineering Handbook (kythuatdulieu.github.io)
- URL: <https://kythuatdulieu.github.io/concepts/foundation/data-engineering/>
- Created sources/data-engineering-handbook.md
- Updated concepts: data-engineer (added four pillars, 6-step pipeline flow, idempotency/IaC/testing best practices, trade-offs, common mistakes)
- Updated index.md: +1 source entry
- Total pages: 104 (79 concepts + 29 sources)

## [2026-06-08] redesign | Complete wiki UX overhaul — sidebar, MOC table, search, popovers, theme

- Extracted shared CSS to styles/main.css (350 lines, eliminates ~32KB×108 pages of inline CSS duplication)
- Created scripts/js/{theme,sidebar,focus,toc,popovers}.js for client-side interactivity
- Rewrote convert-to-html.py templates: new three-panel layout with sticky header, left sidebar, right TOC
- Added breadcrumbs (Home / Category / Page) with MOC anchor links on every page
- Added prev/next pagination in footer for sequential browsing
- Added left sidebar with collapsible category tree populated from auto-generated meta/concepts.json
- Replaced old Browse Wiki grid with MOC table: tag→category mapping groups 79 concepts into 11 broad categories
- Added Tippy.js popover previews on wikilinks (hover to see definition)
- Added Pagefind full-text search (press / to search, fully static)
- Added focus mode toggle (hides sidebars for reading)
- Added resizable sidebar with drag handle (width persisted to localStorage)
- Added theme toggle button with manual dark/light switching + localStorage persistence
- Added right sidebar with auto-generated Table of Contents (H2/H3 headings)
- Auto-generates meta/concepts.json and meta/backlinks.json during conversion
- Fixed index.html merge conflict artifacts
- Added synthesis template (converter now iterates syntheses/ directory)
- No pages added — structural/UX changes only

## [2026-06-08] ingest | De-Coding the Technical Interview, High Performance Spark, The 1% Case Interview

- Source 1: "De-Coding the Technical Interview Process" by Emma Bostian (ebook, 138 pages, finished 2026-05-04)
- Source 2: "High Performance Spark" by Holden Karau & Rachel Warren (ebook, 356 pages, finished 2026-05-01)
- Source 3: "The 1%: Conquer Your Consulting Case Interview" by Florian Smeritschnig (ebook, 294 pages, finished 2026-05-02)
- Copied to: raw/articles/de-coding-technical-interview.md, raw/articles/high-performance-spark.md, raw/articles/the-1-percent-case-interview.md
- Created sources/de-coding-technical-interview.md, sources/high-performance-spark.md, sources/the-1-percent-case-interview.md
- New concepts: apache-spark, case-interview
- Updated concepts: technical-interview (added De-Coding TTIP source + case-interview contrast)
- Updated index.md: +2 concept entries, +3 source entries
- Total pages: 106 (81 concepts + 32 sources)

## [2026-06-12] ingest | Intuitive Python (David Muller)

- Source: "Intuitive Python" by David Muller (ebook, 137 pages, finished 2026-06-12)
- Copied to: raw/articles/intuitive-python.md (Vietnamese notes)
- Created sources/intuitive-python.md
- New concepts: python-professional-practices, python-static-analysis, python-debugging-pdb, python-standard-library, python-concurrency, python-repl
- Updated concepts: immutability (added namedtuple cross-ref), fail-fast (added static analysis cross-ref), readability-vs-performance (added concurrency safety cross-ref)
- Updated index.md: +6 concept entries, +1 source entry
- Total pages: 101 (87 concepts + 33 sources)

## [2026-06-14] ingest | Data Lifecycle — Data Engineering Handbook

- Source: Vietnamese Data Engineering Handbook, concept page about Vòng đời Dữ liệu (Data Lifecycle)
- URL: <https://kythuatdulieu.github.io/concepts/foundation/data-lifecycle/>
- Created sources/data-lifecycle-handbook.md
- Created concepts/data-lifecycle.md
- New concepts: data-lifecycle
- Updated index.md: +1 concept entry, +1 source entry
- Total pages: 103 (88 concepts + 34 sources)

## [2026-06-14] ingest | Agent Quality & Token Optimization — GitHub Workshop

- Source: "Agent Quality & Token Optimization" workshop by Felix Gozali & Lakshya Tyagi (GitHub)
- URL: <https://staticassets.goldcast.io/public_images/organization/4bbeac0f-e176-4d6f-85a7-ac3397470d44/lsQlOCxTfKqVMqgFOVUA_Agent_Quality_and_Token_Optimization_(customer-facing_workshop).pdf>
- Copied to: raw/assets/agent-quality-token-optimization-workshop.pdf
- Created sources/agent-quality-token-optimization.md
- Created concepts/agent-quality-optimization.md
- New concepts: agent-quality-optimization
- Related concepts: harness-engineering, technological-centaur, fail-fast, testing-strategy
- Updated index.md: +1 concept entry, +1 source entry
- Total pages: 105 (89 concepts + 35 sources)

## [2026-06-14] ingest | Learning Domain-Driven Design (Vlad Khononov)

- Source: "Learning Domain-Driven Design" by Vlad Khononov (ebook, 340 pages, finished 2026-06-14)
- Copied to: raw/articles/learning-domain-driven-design.md (Vietnamese notes)
- Created sources/learning-domain-driven-design.md
- Created concepts/domain-driven-design.md
- New concepts: domain-driven-design
- Related concepts: software-as-simulation, mapper-principles, bijection, rich-domain-model, tell-dont-ask, object-oriented-design, harness-engineering
- Updated index.md: +1 concept entry, +1 source entry
- Total pages: 118 (90 concepts + 36 sources)

## [2026-06-14] lint | Health check + fix pass

- Scanned 126 pages (90 concepts + 36 sources) across 6 lint dimensions (broken wikilinks, orphans, frontmatter, contradictions, stubs, gaps)
- Fixed 1 broken wikilink: created concepts/data-governance.md (linked from data-lifecycle.md)
- Fixed 1 frontmatter issue: added missing `created`/`updated` fields to sources/intuitive-python.md
- Verified: domain-driven-design wikilink now resolves (concept page created by DDD ingest)
- Empty URLs: 18 book sources have `url: ""` — acceptable for books without canonical URLs (consistent with past lint)
- Contradictions: 0 found
- Orphans: not checked systematically (deferred)
- Total pages: 119 (91 concepts + 36 sources)

## [2026-06-15] ingest | A Practical Guide to Becoming an AI-Native Engineer (ByteByteGo)

- Created sources/practical-guide-ai-native-engineer.md (Shah Rahman, Meta)
- New concepts: ai-native-engineering, context-engineering, agentic-development-life-cycle, vibe-coding
- Updated concepts/agent-quality-optimization.md (+ context-engineering, ai-native-engineering cross-refs)
- Updated concepts/harness-engineering.md (+ ADLC, ai-native-engineering cross-refs)

## [2026-06-15] ingest | In 2026 The Data Fundamentals Matter More Than Ever (SeattleDataGuy)

- Created sources/data-fundamentals-matter-2026.md (Ben Rogojan)
- New concepts: data-engineering-fundamentals
- Updated concepts/data-engineer.md (+ fundamentals, glue skills, CI/CD cross-refs)
- Updated concepts/data-governance.md (+ agent sprawl mention)
- Updated concepts/dataops.md (+ CI/CD tools, fundamentals cross-ref)

## [2026-06-15] ingest | CI/CD Tips — r/dataengineering Discussion

- Created sources/reddit-cicd-tips-data-engineering.md (community discussion)
- New concepts: cicd-data-pipelines
- Updated concepts/data-engineer.md (+ CI/CD link)
- Updated concepts/dataops.md (+ cicd-data-pipelines link)
- Updated concepts/data-governance.md (+ cicd cross-ref)

## [2026-06-15] post-ingest | HTML regeneration + index update

- Ran `uv run scripts/convert-to-html.py` — regenerated all .html files
- Updated index.md with 6 new concept entries + 3 new source entries
- Total pages: 136 (97 concepts + 39 sources)

## [2026-06-15] lint | Dead-end sources & connection card fixes

### Part 1: Fixed 10 dead-end sources (added wikilinks + connection cards)

- sources/benchmarking-vortex-file-format.md — added inline wikilinks + connection cards for 6 concepts
- sources/data-fundamentals-matter-2026.md — added inline wikilinks + connection cards for 4 concepts
- sources/delta-catalog-managed-tables.md — added inline wikilinks + connection cards for 2 concepts
- sources/delta-grows-up-writes-unity-catalog.md — added inline wikilinks + connection cards for 4 concepts
- sources/go-web-programming.md — added inline wikilinks + connection cards for 5 concepts
- sources/hugo-data-ingestion-platform-flink.md — added inline wikilinks + connection cards for 5 concepts
- sources/learn-harness-engineering.md — added inline wikilinks + connection cards for 1 concept
- sources/practical-guide-ai-native-engineer.md — added inline wikilinks + connection cards for 6 concepts
- sources/reddit-cicd-tips-data-engineering.md — added inline wikilinks + connection cards for 3 concepts
- sources/tdd-python-percival.md — added inline wikilinks + connection cards for 3 concepts

### Part 2: Fixed 12 connection card inconsistencies

- concepts/bijection.md — added [[fail-fast]] to connections
- concepts/duckdb.md — added [[apache-datafusion]], [[apache-iceberg]], [[vortex-file-format]] to connections
- concepts/apache-arrow.md — added [[duckdb]] to connections
- concepts/change-data-capture.md — added [[delta-kernel]] to connections
- concepts/data-lifecycle.md — added [[data-governance]] to connections
- concepts/clickhouse.md — added [[apache-iceberg]], [[in-process-olap]] to connections
- concepts/vortex-file-format.md — added [[apache-arrow]] to connections
- concepts/dbt.md — added [[apache-flink]] to connections
- concepts/analytics-engineer.md — added [[apache-flink]] to connections
- concepts/wiki-maintenance.md — added [[sources/sample-article]] to connections
- concepts/apache-parquet.md — added [[apache-iceberg]], [[lance-file-format]] to connections
- sources/unlocking-dbt-design-deploy-transformations.md — added connection cards section with [[analytics-engineer]], [[elt]]

### Part 3: Added backlinks from 5 Python concept pages to intuitive-python

- concepts/python-debugging-pdb.md — added [[sources/intuitive-python]] backlink
- concepts/python-standard-library.md — added [[sources/intuitive-python]] backlink
- concepts/python-concurrency.md — added [[sources/intuitive-python]] backlink
- concepts/python-repl.md — added [[sources/intuitive-python]] backlink
- concepts/python-professional-practices.md — added [[sources/intuitive-python]] backlink

- Regenerated HTML via `uv run scripts/convert-to-html.py`
- All dates bumped to 2026-06-15 on modified files

## [2026-06-15] lint | Fix broken wikilinks, orphans, frontmatter

- Created 3 stub concept pages for broken wikilinks: specification-driven-development, data-modeling, code-overload
- Fixed sources/semantic-layers-for-ai.md: ingested date 2026-06-08 → 2026-06-11 (was before source_date)
- Added created/updated fields to 3 new source pages (data-fundamentals-matter-2026, practical-guide-ai-native-engineer, reddit-cicd-tips-data-engineering)
- Cross-referenced orphans: middleware-pattern (from go-http-handlers), intuitive-python (from python-static-analysis)
- Bulk-updated stale `updated` dates on 84 pages to 2026-06-15
- Regenerated HTML, updated index.md (100 concepts + 39 sources = 139 pages)

## [2026-06-15] site | Remove sources from public website

- Modified scripts/convert-to-html.py: skip HTML generation for sources/
- Source wikilinks now render as plain text (`source-ref` class) instead of broken links
- Source connection cards render as non-clickable text (`text-ref` class)
- Deleted 39 existing source HTML files from sources/
- Website now shows only concepts (100 pages) — sources remain as canonical .md in repo

## [2026-06-15] ingest | Refactoring at Scale (Maude Lemaire)

- Created sources/refactoring-at-scale-lemaire.md (245-page book, notes in Vietnamese)
- New concepts: refactoring-at-scale, software-rot, complexity-metrics, code-archaeology
- Updated concepts/code-quality-pillars.md (+ refactoring, complexity metrics cross-refs)
- Updated concepts/essential-accidental-complexity.md (+ 5 cross-refs to new concepts)
- Regenerated HTML, updated index.md (104 concepts + 40 sources = 144 pages)

## [2026-06-15] infra | Deploy HTML to gh-pages branch, stop tracking on main

- Modified .github/workflows/build.yml: deploy to gh-pages via peaceiris/actions-gh-pages@v4
- Added /concepts/*.html, /sources/*.html, /syntheses/*.html, /index.html to .gitignore
- Removed 105 tracked HTML files from main (git rm --cached)
- Fixed update_index_html() bug: regex replace instead of string append
- Updated AGENTS.md: HTML is CI-deployed, local script is for preview only
- No more merge conflicts on index.html — CI never touches main branch files

## [2026-06-17] ingest | Byzantine Fault Tolerance (BFT) — Data Engineering Handbook

- Source: Vietnamese DE Handbook page on BFT (kythuatdulieu.github.io)
- Created sources/bft-data-engineering-handbook.md
- Created concepts/byzantine-fault-tolerance.md — Byzantine Generals Problem, 3f+1, PBFT, CFT vs BFT, DE applications (checksums, Merkle Trees, Zero-Trust Data Mesh)
- Updated index.md (105 concepts, 41 sources)

## [2026-06-17] ingest | CAP Theorem — Data Engineering Handbook

- Source: Vietnamese DE Handbook page on CAP Theorem (kythuatdulieu.github.io)
- Created sources/cap-theorem-handbook.md
- Created concepts/cap-theorem.md — Brewer's theorem, CP vs AP architectures, CAP-C vs ACID-C distinction, quorum mechanics (R+W>N), split-brain resolution, PACELC extension, best practices for DE
- Updated index.md (106 concepts, 42 sources)

## [2026-06-17] ingest | Data Quality Traffic Lights (Robert Sahlin) + Meta Engineering Org (Gergely Orosz)

- Sources: "Data quality traffic lights" (robertsahlin.substack.com) + "Why is Meta destroying its engineering organization?" (pragmaticengineer.com)
- Created sources/data-quality-traffic-lights-sahlin.md, sources/meta-destroying-engineering-org-orosz.md
- Created concepts/data-quality-monitoring.md — 3 pillars (detection, lineage, communication), 5 failure modes, TimesFM anomaly detection, programmatic trust for agents/ML
- Created concepts/ai-psychosis.md — organizational pathology, Meta case study, MTBF vs MTTR lesson, profit center vs cost center, symptoms and resistance
- Updated index.md (108 concepts, 44 sources)

## [2026-06-20] ingest | The New SDLC With Vibe Coding — Osmani, Saboo & Kartakis

- Source: "The New SDLC With Vibe Coding: From ad-hoc prompting to Agentic Engineering" by Addy Osmani, Shubham Saboo & Sokratis Kartakis (ebook, 51 pages, finished 2026-06-20)
- Source file at: /Users/tuanpham/Downloads/ (needs to be moved to raw/)
- Created sources/new-sdlc-vibe-coding.md
- New concepts: agent-loop, agent-components, agent-verification
- Updated concepts: vibe-coding (+ Agentic Engineering spectrum, token economics), harness-engineering (+ 90% rule, 6-component production anatomy), context-engineering (+ 6 dimensions, static vs dynamic, agent skills pattern), ai-native-engineering (+ Conductor vs Orchestrator modes, 4 orchestrator skills), agent-quality-optimization (+ CapEx vs OpEx token economics), agentic-development-life-cycle (+ 4-phase implementation roadmap)
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 156 (111 concepts + 45 sources)

## [2026-06-21] ingest | Distributed Consensus (Raft & Paxos) — Data Engineering Handbook

- Source: Vietnamese DE Handbook page on Raft & Paxos consensus algorithms (kythuatdulieu.github.io)
- Created sources/consensus-raft-paxos-handbook.md
- Created concepts/distributed-consensus.md — consensus problem (Agreement, Validity, Termination), FLP impossibility, Safety vs Liveness, Paxos (roles, two-phase protocol, Multi-Paxos, complexity issues), Raft (state machine, leader election, log replication, one-way data flow), comparison table, ecosystem
- Created concepts/leader-election.md — Raft's randomized timeout mechanism, Term-based safety, split-brain prevention, Multi-Paxos implicit election, production coordination services (Zookeeper, etcd, Consul, KRaft), common failure modes
- Updated concepts/byzantine-fault-tolerance.md — cross-referenced distributed-consensus for CFT vs BFT comparison
- Updated concepts/cap-theorem.md — cross-referenced distributed-consensus as mechanism enabling CP systems
- Updated index.md (113 concepts, 46 sources)

## [2026-06-21] ingest | Cloud Service Models (Alex Xu — System Design Interview)

- Created concepts/cloud-service-models.md — IaaS/PaaS/SaaS comparison table, choosing a model, cow/milk analogy
- Source: system-design-interview-xu (existing source)
- Updated index.md (114 concepts, 46 sources)

## [2026-06-21] ingest | Orchestration vs Choreography (Alex Xu — System Design Interview)

- Created concepts/orchestration-vs-choreography.md — comparison table, when to use each, e-commerce checkout example
- Source: system-design-interview-xu (existing source)
- Updated index.md (116 concepts, 46 sources)

## [2026-06-21] ingest | TLS & HTTPS (Alex Xu — System Design Interview)

- Created concepts/tls-https.md — 3-step TLS handshake, asymmetric vs symmetric encryption comparison, why TLS uses both
- Source: system-design-interview-xu (existing source)
- Updated index.md (115 concepts, 46 sources)

## [2026-06-21] ingest | Redis (Alex Xu — System Design Interview)

- Created concepts/redis.md — in-memory data store, single-threaded event loop, IO multiplexing, key use cases
- Source: system-design-big-archive (new source reference)
- Updated index.md (116 concepts, 46 sources)

## [2026-06-21] ingest | Message Delivery Semantics (Alex Xu — System Design Interview)

- Created concepts/message-delivery-semantics.md — at-most-once, at-least-once, effectively exactly-once; idempotency strategies; Two Generals Problem
- Source: system-design-big-archive
- Updated index.md (117 concepts, 46 sources)

## [2026-06-21] ingest | Snowflake ID (Alex Xu — System Design Interview)

- Created concepts/snowflake-id.md — 64-bit distributed unique ID pattern, time-ordered, no coordination
- Source: system-design-big-archive
- Updated index.md (117 concepts, 46 sources)

## [2026-06-21] ingest | HTTP Evolution (Alex Xu — System Design Interview)

- Created concepts/http-evolution.md — HTTP/1.0 through HTTP/3 (QUIC), HOL blocking across versions
- Source: system-design-big-archive
- Updated index.md (118 concepts, 46 sources)

## [2026-06-23] ingest | Databricks Platform concept page

- Created concepts/databricks-platform.md — 4-layer architecture, control vs data plane, SQL-first strategy
- Source: databricks-dea-study-guide (referenced in frontmatter)
- Updated index.md (128 concepts, 47 sources)

## [2026-06-21] ingest | System Design: The Big Archive (Alex Xu)

- Source: "System Design: The Big Archive" by Alex Xu (ebook, 159 pages, finished 2026-06-21)
- Created sources/system-design-big-archive.md
- New concepts: cloud-service-models, containerization, deployment-strategies, database-isolation, sso, password-storage, tls-https, redis, orchestration-vs-choreography, api-architectural-styles, http-evolution, bloom-filter, snowflake-id, message-delivery-semantics
- Updated concepts: apache-kafka (+ zero copy, sequential I/O perf internals), message-queue (+ delivery semantics cross-ref), database-sharding (+ hash vs range details), cache-strategy (+ redis, bloom-filter cross-refs), system-design-interview (+ source ref)
- Updated index.md: +14 concept entries, +1 source entry
- Total pages: 174 (127 concepts + 47 sources)

## [2026-06-23] ingest | Databricks Certified DE Associate Study Guide (Derar Alhussein)

- Source: "Databricks Certified Data Engineer Associate Study Guide" by Derar Alhussein (ebook, 802 pages, finished 2026-06-23)
- Created sources/databricks-dea-study-guide.md
- New concepts: data-lakehouse, databricks-platform, dbfs
- Updated concepts: apache-spark (+ Databricks Runtime context, driver/worker hierarchy, data-lakehouse/databricks-platform cross-refs), delta-lake (+ Databricks Runtime role, lakehouse foundation), unity-catalog (+ governance evolution, platform architecture role)
- Updated index.md: +3 concept entries, +1 source entry
- Total pages: 178 (130 concepts + 48 sources)

## [2026-06-27] ingest | Clean Code Principles And Patterns (Petri Silen) + Building an Anonymization Pipeline (Arbuckle & El Emam)

- Source 1: "Clean Code Principles And Patterns (Python Edition)" by Petri Silen (ebook, 676 pages, finished 2026-04-28)
- Source 2: "Building an Anonymization Pipeline: Creating Safe Data" by Luk Arbuckle & Khaled El Emam (ebook, 167 pages, finished 2026-04-29)
- Created sources/clean-code-principles-patterns-silen.md
- Created sources/building-anonymization-pipeline.md
- New concepts: microservices, shift-left-security, data-anonymization, differential-privacy, synthetic-data
- Updated concepts: solid-principles (+ source ref), object-oriented-design (+ composition over inheritance section + source ref), code-quality-pillars (+ source ref), testing-strategy (+ testing pyramid/BDD + source ref), observability (+ OpenTelemetry/SLIs/SLOs section + source ref), software-rot (+ technical debt management section + source ref), data-governance (+ Five Safes framework section + source ref), data-quality-monitoring (+ anonymization output monitoring section + source ref)
- Updated index.md: +5 concept entries, +2 source entries
- Total pages: 202 (149 concepts + 53 sources)

## [2026-06-29] ingest | System Design Interview – An Insider's Guide: Volume 2 (Alex Xu & Sahn Lam)

- Source: "System Design Interview – An Insider's Guide: Volume 2" by Alex Xu & Sahn Lam (ebook, 429 pages, finished 2026-06-29)
- Copied to: raw/system-design-interview-volume-2.md (Vietnamese notes)
- Created sources/system-design-interview-volume-2.md
- New concepts: proximity-service, geospatial-indexing, geohash, quadtree
- Updated concepts: system-design-interview (+ Volume 2 reference, QPS 10^5 shortcut, QPS→architecture table, canonical problems), database-replication (+ Primary-Secondary cluster diagram, replication lag acceptability), cache-strategy (+ cache stampede mitigation: staggered invalidation, cache warming, rate limiting, circuit breakers), deployment-strategies (+ incremental rollout for in-memory index rebuild, Blue/Green risk), scalable-architecture (+ QPS-driven architecture decisions table)
- Updated index.md: +4 concept entries, +1 source entry, updated 5 existing summaries
- Total pages: 207 (153 concepts + 54 sources)

## [2026-06-29] lint | Post-ingest health check

- Scanned all 207 wiki pages (153 concepts + 54 sources) across 3 lint dimensions (broken wikilinks, orphans, frontmatter)
- Broken wikilinks: 0 found — all wikilinks resolve correctly
- Orphans: 14 near-orphans (1 inbound link each): ai-psychosis, apache-arrow, architecture-in-agile, bloom-filter, cloud-service-models, data-scientist, feedback, http-evolution, knowledge-graph, message-delivery-semantics, python-repl, redis, shift-left-security, snowflake-id — deferred to next lint pass
- Frontmatter: all 10 new/updated files have complete frontmatter; 1 source (system-design-interview-volume-2) has empty `url: ""` — consistent with 18 other book sources
- Fixed: stale comment in data-engineering-fundamentals.md (claimed `[[data-modeling]]` didn't exist; page was created in prior ingest)
- HTML regenerated

## [2026-06-27] lint | Post-ingest health check + fix pass

- Scanned all 202 wiki pages (149 concepts + 53 sources) across 6 lint dimensions
- Fixed 12 broken wikilinks:
  - **Missing `sources/` prefix (6)**: ai-psychosis, byzantine-fault-tolerance, cap-theorem, data-quality-monitoring, distributed-consensus, leader-election — inline source citations lacked `sources/` prefix
  - **Title Case → kebab-case slug (6)**: architecture-in-agile (`[[Model-Code Gap]]` → `[[model-code-gap]]`), spaced-repetition (`[[Testing Effect]]` → `[[testing-effect]]`), ultralearning-scott-young (`[[Metalearning]]`, `[[Directness]]`, `[[Testing Effect]]`, `[[Spaced Repetition]]`)
- Fixed 11 source files missing frontmatter fields:
  - Added `created`/`updated` to: how-ai-changes-4-core-data-roles, just-enough-software-architecture-fairbanks, ultralearning-scott-young, databricks-dea-study-guide, system-design-big-archive, consensus-raft-paxos-handbook, new-sdlc-vibe-coding, meta-destroying-engineering-org-orosz, data-quality-traffic-lights-sahlin, cap-theorem-handbook, bft-data-engineering-handbook
  - Added missing `url: ""` to ultralearning-scott-young
- Verified: 0 contradictions, 0 true orphans (14 near-orphans with 1 inbound link noted), 0 gaps (all source concept refs have pages), 100% frontmatter completeness
- HTML regenerated via convert-to-html.py

## [2026-08-18] ingest | Five engineering systems books

- Created sources/an-elegant-puzzle.md, sources/building-secure-and-reliable-systems.md, sources/site-reliability-engineering.md, sources/software-engineering-at-google.md, and sources/the-accidental-cto.md
- Created concepts/site-reliability-engineering.md, concepts/secure-system-design.md, concepts/technical-debt-management.md, and concepts/continuous-delivery.md
- Updated engineering management, scalable architecture, database replication, CDC, observability, deployment strategies, testing strategy, and shift-left security concepts with new evidence and cross-references
- Updated index.md and regenerated concept HTML plus meta indexes via uv run scripts/convert-to-html.py
- Verified 0 missing wikilinks; total pages: 346 (250 concepts + 96 sources)

## [2026-08-18] lint | Health check + fix pass

- Scanned all 346 pages (250 concepts + 96 sources): broken wikilinks 0, dangling frontmatter refs 0, index coverage complete, 0 contradictions
- Fixed 4 source pages missing the `url` frontmatter key (added `url: ""`): art-of-readable-code, fundamentals-of-data-engineering, introduction-to-machine-learning-systems, staff-engineers-path
- Fixed 2 true orphans: wired staff-engineer-larson into concepts/staff-engineering.md and 500-lines-or-less into concepts/code-readability.md (sources frontmatter + benchmark wikilinks)
- Regenerated HTML for 6 stale concept pages via uv run scripts/convert-to-html.py
- Noted 28 near-orphans (single inbound reference), consistent with prior passes — no action
