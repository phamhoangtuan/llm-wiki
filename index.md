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
- [DuckDB](concepts/duckdb.html) — In-process OLAP database — "SQLite for analytics" — columnar, vectorized, zero-setup
- [Vectorized Execution](concepts/vectorized-execution.html) — Processing data in vectors (chunks) not row-by-row; SIMD, cache-efficient
- [In-Process OLAP](concepts/in-process-olap.html) — Analytical database runs as embedded library — no server, no network latency
- [System Design Interview](concepts/system-design-interview.html) — Framework for designing scalable distributed systems under constraints
- [Scalable Architecture](concepts/scalable-architecture.html) — Evolution from single server to horizontal scaling with distributed components
- [Load Balancer](concepts/load-balancer.html) — Traffic distribution, security, and high availability across backend servers
- [Database Replication](concepts/database-replication.html) — Master-slave pattern for read/write separation and horizontal read scaling
- [Cache Strategy](concepts/cache-strategy.html) — Read-through cache, TTL, eviction policies, and invalidation strategies
- [CDN](concepts/cdn.html) — Geographically distributed edge caching for static content delivery
- [Stateless Architecture](concepts/stateless-architecture.html) — Externalized sessions enabling horizontal scaling and autoscaling
- [Message Queue](concepts/message-queue.html) — Async decoupling of producers and consumers for resilience and independent scaling
- [Observability](concepts/observability.html) — Metrics, logs, and traces for understanding distributed system health
- [Vortex File Format](concepts/vortex-file-format.html) — Next-gen Rust-native columnar format; 100× random access claims vs Parquet, immature Python ecosystem as of 2026-05
- [Polars](concepts/polars.html) — Rust-based DataFrame library with lazy evaluation; reported OOM reliability issues on large CSV
- [Apache DataFusion](concepts/apache-datafusion.html) — Rust-native embeddable SQL query engine; fastest CSV scan in benchmarks (5.1s vs 25.5s DuckDB)
- [Apache Parquet](concepts/apache-parquet.html) — Dominant columnar storage format for data lakes; ~200× faster than CSV for analytics
- [Lance File Format](concepts/lance-file-format.html) — Columnar format optimized for ML/AI workloads; random access, versioning
- [Apache Flink](concepts/apache-flink.html) — Distributed stream processing engine with exactly-once semantics; Flink CDC for database ingestion
- [Change Data Capture (CDC)](concepts/change-data-capture.html) — Capturing row-level DB changes from transaction logs for real-time data sync
- [Data Ingestion](concepts/data-ingestion.html) — Moving data from sources to data lake; self-service platforms, batch vs streaming patterns
- [Apache Kafka](concepts/apache-kafka.html) — Distributed event streaming platform; persistent log, high throughput, schema registry
- [Apache Iceberg](concepts/apache-iceberg.html) — Open table format for data lakes with ACID transactions, schema evolution, time travel

## Sources

- [Python Testing with pytest](sources/okken-python-testing-pytest.html) — Notes on "Python Testing with pytest (2nd Ed.)" by Brian Okken — 398 pages
- [The LLM Wiki Pattern](sources/sample-article.html) — Karpathy's gist: LLM-maintained persistent wiki instead of RAG
- [Clean Code Cookbook](sources/contieri-clean-code-cookbook.html) — Notes on Contieri's book — 374 pages on software as simulation, MAPPER, bijection
- [Quick Insights on Materialized Views](sources/materialized-views-quick-insights.html) — Vu Trinh on MVs, IVM theory, freshness trade-offs, and streaming applications
- [DuckDB: Up and Running](sources/duckdb-up-and-running.html) — Wei-Meng Lee's guide — 308 pages on architecture, performance, and ecosystem
- [System Design Interview – An Insider's Guide](sources/system-design-interview-xu.html) — Alex Xu's 252-page ebook on designing scalable systems from single server to millions of users
- [Benchmarking Vortex File Format vs Parquet, CSV](sources/benchmarking-vortex-file-format.html) — Daniel Beach benchmarks Vortex vs Parquet/CSV with DuckDB, Polars, DataFusion (Backblaze ~24 GB dataset, 2026-05)
- [Hugo Data Ingestion Platform with Apache Flink](sources/hugo-data-ingestion-platform-flink.html) — Grab Engineering's evolution from siloed ingestion (Kafka Connect + Sprinkler) to unified Flink-based platform

## Syntheses

_No syntheses yet. Ask a question and file the answer to add one._

---

*Last updated: 2026-05-26*
*Pages: 57 (49 concepts + 8 sources)*
