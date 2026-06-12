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
- [Apache Flink](concepts/apache-flink.html) — Distributed stream processing engine with exactly-once semantics; Flink 2.1 + DynamicIcebergSink (1.11.0) for multi-table routing and auto-schema evolution
- [Change Data Capture (CDC)](concepts/change-data-capture.html) — Capturing row-level DB changes from transaction logs for real-time data sync
- [Data Ingestion](concepts/data-ingestion.html) — Moving data from sources to data lake; self-service platforms, batch vs streaming patterns
- [Apache Kafka](concepts/apache-kafka.html) — Distributed event streaming platform; persistent log, high throughput, schema registry
- [Apache Iceberg](concepts/apache-iceberg.html) — Open table format; V3 spec stabilized (1.11.0) with deletion vectors, table encryption, pluggable File Format API, server-side scan planning
- [dbt (data build tool)](concepts/dbt.html) — SQL transformation framework for ELT; compute-neutral, declarative, with built-in testing and docs
- [Analytics Engineer](concepts/analytics-engineer.html) — Bridge role between Data Engineer and Analyst; owns the transformation layer
- [ELT (Extract-Load-Transform)](concepts/elt.html) — Modern data paradigm: load raw first, transform in-warehouse; dbt handles the "T"
- [Delta Lake](concepts/delta-lake.html) — Open table format with ACID, time travel, schema enforcement; DuckDB supports reads + writes (stable)
- [Unity Catalog](concepts/unity-catalog.html) — Open standard for data governance; Catalog Commits coordinate concurrent writes to Delta tables
- [Apache Arrow](concepts/apache-arrow.html) — Language-agnostic columnar in-memory format; zero-copy interop across Python, C++, Rust, Java
- [Database Sharding](concepts/database-sharding.html) — Horizontal partitioning for write scalability; contrasts with replication
- [Dependency Injection](concepts/dependency-injection.html) — Design discipline for loose coupling; constructor/method/property injection, lifetime management, anti-patterns
- [Composition Root](concepts/composition-root.html) — Single centralized location where object graphs are wired; Pure DI vs DI Containers
- [SOLID Principles](concepts/solid-principles.html) — SRP, OCP, LSP, ISP, DIP — the foundation for effective Dependency Injection
- [Harness Engineering](concepts/harness-engineering.html) — Closed-loop systems for reliable AI agents; 4 primitives, 5-phase workflow, verification-first design
- [ClickHouse](concepts/clickhouse.html) — High-performance column-oriented OLAP DBMS; data lake ready with Delta Lake and Iceberg support
- [Delta Kernel](concepts/delta-kernel.html) — Rust abstraction layer for Delta Lake protocol; handles transaction logs, snapshots, schema evolution
- [Liquid Clustering](concepts/liquid-clustering.html) — Modern data layout for Delta/Iceberg tables; replaces Hive-style partitioning with incremental, multi-dimensional clustering
- [Goroutines](concepts/goroutines.html) — Go's lightweight concurrency primitive; concurrency vs parallelism distinction — handles 100K+ concurrent tasks
- [Go HTTP Handlers](concepts/go-http-handlers.html) — Handler interface, HandlerFunc, ServeMux routing, and middleware chaining — the building blocks of Go web apps
- [Go Template Escaping](concepts/go-template-escaping.html) — Context-aware HTML escaping in `html/template`; XSS protection by default — understands HTML/JS/CSS contexts
- [Go Web Ecosystem](concepts/go-web-ecosystem.html) — Go's philosophy: standard library over frameworks, static binary deployment, built-in testing, implicit interfaces
- [TDD Methodology](concepts/tdd-methodology.html) — Red-Green-Refactor cycle, Outside-In TDD (Double Loop), YAGNI, the Testing Goat discipline
- [Functional Testing](concepts/functional-testing.html) — User-perspective testing via Selenium/HTTP client; outer loop of TDD; test behavior not constants
- [Technical Interview](concepts/technical-interview.html) — Philosophy of coding interviews: relative evaluation, false positives/negatives, company cultures, BUD optimization, Talk Aloud
- [Code Quality Pillars](concepts/code-quality-pillars.html) — Engineering vs Coding distinction, 4 goals and 6 tactical pillars for maintainable software
- [Software Quality Dimensions](concepts/software-quality-dimensions.html) — Multi-dimensional quality spectrum, four core trade-offs, YAGNI, analyzability, abstraction costs
- [DataOps](concepts/dataops.html) — Applying software engineering practices (version control, testing, modularity) to data pipelines and transformations
- [Object-Oriented Design](concepts/object-oriented-design.html) — Practical OO design: TRUE standard, design as discovery, messages over methods, SRP as foundation
- [Kubernetes Operator](concepts/kubernetes-operator.html) — Control loop pattern (READ → CHANGE → UPDATE), CRDs, extension patterns, Go ecosystem for K8s-native apps
- [Middleware Pattern](concepts/middleware-pattern.html) — Composable HTTP handler wrapping for cross-cutting concerns; Go's standard-library middleware chaining
- [Data Engineer](concepts/data-engineer.html) — Specialized SWE role: builds data infrastructure, pipelines, and platforms; bridges SWE and DA/DS
- [Semantic Layer](concepts/semantic-layer.html) — Unified context layer standardizing metrics and business logic for AI agents across dbt, BI, docs, and query patterns
- [Staff Engineering](concepts/staff-engineering.html) — Career level beyond Senior: expanding surface area, influencing across teams, building compounding systems
- [Apache Spark](concepts/apache-spark.html) — Distributed data processing engine; internals, shuffle optimization, join strategies, data skew mitigation
- [Case Interview](concepts/case-interview.html) — Consulting case interview methodology: MECE, Pyramid Principle, SCORE framework, 9-Step Math
- [Python Professional Practices](concepts/python-professional-practices.html) — Transition from "code that runs" to production-grade Python via automated quality control
- [Python Static Analysis](concepts/python-static-analysis.html) — Black + Flake8 + Mypy trifecta for automated code quality gates
- [Python Debugging with PDB](concepts/python-debugging-pdb.html) — Interactive debugging via breakpoint() and PDB: surgical state inspection over print()
- [Python Standard Library](concepts/python-standard-library.html) — Batteries-included: collections (defaultdict, namedtuple) and sqlite3
- [Python Concurrency](concepts/python-concurrency.html) — Threads vs Processes, GIL, race condition dangers, and when to use concurrency
- [Python REPL](concepts/python-repl.html) — Interactive console as a living laboratory: repr, dir(), help(), __mro__ for object exploration

## Sources

- [Python Testing with pytest](sources/okken-python-testing-pytest.html) — Notes on "Python Testing with pytest (2nd Ed.)" by Brian Okken — 398 pages
- [The LLM Wiki Pattern](sources/sample-article.html) — Karpathy's gist: LLM-maintained persistent wiki instead of RAG
- [Clean Code Cookbook](sources/contieri-clean-code-cookbook.html) — Notes on Contieri's book — 374 pages on software as simulation, MAPPER, bijection
- [Quick Insights on Materialized Views](sources/materialized-views-quick-insights.html) — Vu Trinh on MVs, IVM theory, freshness trade-offs, and streaming applications
- [DuckDB: Up and Running](sources/duckdb-up-and-running.html) — Wei-Meng Lee's guide — 308 pages on architecture, performance, and ecosystem
- [System Design Interview – An Insider's Guide](sources/system-design-interview-xu.html) — Alex Xu's 252-page ebook on designing scalable systems from single server to millions of users
- [Benchmarking Vortex File Format vs Parquet, CSV](sources/benchmarking-vortex-file-format.html) — Daniel Beach benchmarks Vortex vs Parquet/CSV with DuckDB, Polars, DataFusion (Backblaze ~24 GB dataset, 2026-05)
- [Hugo Data Ingestion Platform with Apache Flink](sources/hugo-data-ingestion-platform-flink.html) — Grab Engineering's evolution from siloed ingestion (Kafka Connect + Sprinkler) to unified Flink-based platform
- [Unlocking dbt: Design and Deploy Transformations](sources/unlocking-dbt-design-deploy-transformations.html) — Cameron Cyr & Dustin Dorsey's 351-page guide to dbt fundamentals, modeling, testing, and deployment
- [Dependency Injection Principles, Practices, and Patterns](sources/dependency-injection-principles-patterns.html) — van Deursen & Seemann's 643-page definitive guide to DI, Composition Root, and SOLID
- [Delta Grows Up: Writes, Unity Catalog and Time Travel](sources/delta-grows-up-writes-unity-catalog.html) — DuckDB Labs announces stable Delta extension with writes, time travel, and Unity Catalog integration
- [The Next Evolution of Delta — Catalog-Managed Tables](sources/delta-catalog-managed-tables.html) — Delta 4.1.0 + UC 0.4.0: catalog becomes authority for table state, inline commits, convergence with Iceberg
- [Learn Harness Engineering](sources/learn-harness-engineering.html) — walkinglabs' guide: closed-loop AI agent systems, 4 primitives, 5-phase workflow, verification-first design
- [Integrating the Rust Delta Kernel into ClickHouse](sources/integrating-rust-delta-kernel-clickhouse.html) — ClickHouse's journey from native Delta protocol to Rust Kernel; FFI build challenges, CDF support
- [Debunking 8 Data Layout Myths](sources/debunking-data-layout-myths-liquid-clustering.html) — Databricks' case for Liquid Clustering over partitioning; PB-scale benchmarks, 8 myths debunked
- [Go Web Programming](sources/go-web-programming.html) — Sau Sheong Chang's guide to building web apps with Go's standard library — 314 pages
- [Test-Driven Development with Python](sources/tdd-python-percival.html) — Harry Percival's hands-on journey through TDD with Django and Selenium — 662 pages
- [Apache Iceberg 1.11.0 Release](sources/apache-iceberg-1.11.0-release.html) — Major release: V3 spec stabilization, table encryption, File Format API, server-side scan planning, SQL UDFs
- [Cracking the Coding Interview](sources/cracking-the-coding-interview.html) — McDowell's 708-page guide to technical interview philosophy, company cultures, and problem-solving strategies
- [Good Code, Bad Code](sources/good-code-bad-code.html) — Tom Long's 338-page guide: 4 goals, 6 pillars, and the engineering mindset
- [Seriously Good Software](sources/seriously-good-software.html) — Marco Faella's 330-page deep dive: quality spectrum, trade-offs, YAGNI, and abstraction costs
- [Data Engineering with dbt](sources/data-engineering-with-dbt.html) — Roberto Zagni's 603-page guide: DataOps mindset, 3-tier modeling, soft boundaries, Jinja-powered SQL
- [Practical Object-Oriented Design](sources/practical-object-oriented-design.html) — Sandi Metz's 334-page guide: TRUE standard, design as discovery, messages in OOP
- [Programming Kubernetes](sources/programming-kubernetes.html) — Schimanski & Hausenblas's 244-page guide: control loops, operators, CRDs, Go ecosystem for K8s-native development
- [Data Engineer Role — Data Engineering Handbook](sources/data-engineer-role-handbook.html) — Vietnamese DE Handbook: role definition, differentiation from SWE/DA/DS, daily workflow, best practices
- [Semantic Layers Are Now for AI](sources/semantic-layers-for-ai.html) — Madison Mae on why semantic layers are critical for AI agents, testing ktx open-source context layer
- [How to Grow From Senior to Staff Engineer](sources/senior-to-staff-engineer.html) — Jordan Cutler's Pinterest case study: 3 dimensions of Staff-level impact in the AI era
- [Databricks Zerobus — Event Streams + Lake House](sources/databricks-zerobus.html) — Daniel Beach explores serverless streaming into Delta Lake without Kafka infrastructure
- [Data Engineering — Data Engineering Handbook](sources/data-engineering-handbook.html) — Vietnamese DE Handbook: discipline overview, four pillars, pipeline flow, best practices
- [De-Coding the Technical Interview Process](sources/de-coding-technical-interview.html) — Emma Bostian's 138-page guide: 5-stage interview lifecycle, 5-step problem-solving cycle
- [High Performance Spark](sources/high-performance-spark.html) — Karau & Warren's 356-page optimization guide: shuffles, joins, skew, Catalyst, Tungsten
- [The 1%: Conquer Your Consulting Case Interview](sources/the-1-percent-case-interview.html) — Smeritschnig's 294-page insider's guide: MECE, SCORE, Pyramid Principle
- [Intuitive Python](sources/intuitive-python.html) — David Muller's 137-page guide to professional Python: static analysis, PDB debugging, standard library, concurrency

## Syntheses

_No syntheses yet. Ask a question and file the answer to add one._

---

*Last updated: 2026-06-12*
*Pages: 112 (87 concepts + 33 sources)*
