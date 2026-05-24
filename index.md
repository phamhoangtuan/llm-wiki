# Wiki Index

> Auto-generated catalog. Updated on every ingest and lint pass.
> Click any link to open the styled HTML page.

---

## Concepts

- [Wiki Maintenance](concepts/wiki-maintenance.html) — How this LLM-maintained wiki works, its conventions and workflows
- [Knowledge Graph](concepts/knowledge-graph.html) — Lightweight knowledge graph via cross-linked pages, no vector DB needed
- [pytest Basics](concepts/pytest-basics.html) — pytest fundamentals: test discovery, naming conventions, plain assert, CLI usage
- [pytest Fixtures](concepts/pytest-fixtures.html) — Reusable setup/teardown via dependency injection, conftest.py, fixture scopes
- [pytest Parametrization](concepts/pytest-parametrization.html) — Run one test function with multiple data sets
- [pytest Markers](concepts/pytest-markers.html) — Tag tests for selective execution: skip, xfail, custom markers
- [pytest Mocking](concepts/pytest-mocking.html) — Isolate external dependencies via monkeypatch, pytest-mock, autospec
- [pytest Plugins](concepts/pytest-plugins.html) — Essential plugins: cov, xdist, randomly, mock, asyncio
- [pytest Configuration](concepts/pytest-configuration.html) — pyproject.toml and pytest.ini configuration
- [pytest Assertions](concepts/pytest-assertions.html) — Assert rewriting mechanism: rich diffs without framework-specific syntax
- [pytest Test Results](concepts/pytest-test-results.html) — Result symbols: PASSED, FAILED, SKIPPED, XFAIL, XPASS, ERROR
- [Testing Strategy](concepts/testing-strategy.html) — API-first testing, test pyramid, 4 pillars of professional testing
- [Software as Simulation](concepts/software-as-simulation.html) — Software is a simulator of reality, not a list of commands
- [MAPPER Principles](concepts/mapper-principles.html) — 6 principles: Model, Abstract, Partial, Programmable, Explaining, Reality
- [Bijection](concepts/bijection.html) — 1-1 mapping between reality and code; the golden design rule
- [Rich Domain Model](concepts/rich-domain-model.html) — Objects encapsulate data + behavior; contrast with anemic domain model
- [Tell, Don't Ask](concepts/tell-dont-ask.html) — Tell objects to act, don't ask for data to process outside
- [Immutability](concepts/immutability.html) — Essential attributes should never change; create new objects instead
- [Fail Fast](concepts/fail-fast.html) — Stop execution immediately on error; don't let errors propagate
- [Essential vs Accidental Complexity](concepts/essential-accidental-complexity.html) — Fred Brooks' two types: inherent vs design-caused
- [Technological Centaur](concepts/technological-centaur.html) — Human architect + AI assistant; clean code enables collaboration
- [Readability vs Performance](concepts/readability-vs-performance.html) — Write clean code first, optimize bottlenecks after profiling
- [Materialized Views](concepts/materialized-views.html) — Pre-computed query results stored as physical tables — the hybrid of tables and views
- [Incremental View Maintenance](concepts/incremental-view-maintenance.html) — Updating MVs by processing only changed data, not full recompute
- [Timely Dataflow](concepts/timely-dataflow.html) — Timestamp-based notification model for distributed incremental computation (Naiad)
- [Differential Dataflow](concepts/differential-dataflow.html) — Versioned incremental computation built on Timely Dataflow
- [DBSP](concepts/dbsp.html) — Signal-processing formalism for incremental view maintenance with 4 operators

## Sources

- [Python Testing with pytest](sources/okken-python-testing-pytest.html) — Notes on "Python Testing with pytest (2nd Ed.)" by Brian Okken — 398 pages
- [The LLM Wiki Pattern](sources/sample-article.html) — Karpathy's gist: LLM-maintained persistent wiki instead of RAG
- [Clean Code Cookbook](sources/contieri-clean-code-cookbook.html) — Notes on Contieri's book — 374 pages on software as simulation, MAPPER, bijection
- [Quick Insights on Materialized Views](sources/materialized-views-quick-insights.html) — Vu Trinh on MVs, IVM theory, freshness trade-offs, and streaming applications

## Syntheses

_No syntheses yet. Ask a question and file the answer to add one._

---

*Last updated: 2026-05-24*
*Pages: 31 (27 concepts + 4 sources)*
