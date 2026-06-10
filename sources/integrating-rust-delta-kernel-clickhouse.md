---
title: "Integrating the Rust Delta Kernel into ClickHouse"
type: source
source_type: article
author: "Melvyn Peignon, Kseniia Sumarokova, Raul Marin"
url: "https://delta.io/blog/2026-05-18-integrating-the-rust-delta-kernel-into-clickhouse/"
source_date: 2026-05-18
ingested: 2026-06-02
created: 2026-06-02
updated: 2026-06-02
tags: [clickhouse, delta-lake, delta-kernel, rust, olap, table-formats]
concepts: [clickhouse, delta-kernel, delta-lake, change-data-capture]
---

## Summary

The ClickHouse team details their journey from implementing the Delta Lake protocol natively to adopting the Rust Delta Kernel — a shared abstraction layer that handles protocol complexity. This shift allowed them to accelerate feature development (writes, schema evolution, time travel, partition pruning, statistics-based pruning, CDF) while reducing maintenance overhead. The article also covers the significant build-system challenges of integrating a Rust crate into a C++ codebase (static linking, sanitizers, vendoring, cross-compilation, OpenSSL dependency), and their upstream contributions to `delta-kernel-rs`.

## Key Takeaways

1. **Delta Kernel as protocol abstraction** — The Kernel handles transaction log parsing, snapshot resolution, file skipping, and metadata. Engines plug in their own Parquet reader and file access via Engine APIs.
2. **Feature acceleration** — Adopting the Kernel delivered writes, schema evolution, time travel, partition pruning, statistics-based pruning, and Change Data Feed (CDF) much faster than native implementation would allow.
3. **Rust FFI in C++ is hard** — Required nightly Rust (for sanitizers), full crate vendoring (to avoid network fetches), Corrosion for CMake integration, and wrestling with OpenSSL dependency chains.
4. **ClickHouse CDF** — Exposed Delta Lake's Change Data Feed via `deltaLake()` table function with `delta_lake_snapshot_start_version` / `delta_lake_snapshot_end_version` settings.
5. **Upstream contributions** — ClickHouse contributed dynamic logging configuration and asynchronous metadata processing (`delta-kernel-rs` PRs #1111, #1827) back to the Delta Kernel.
6. **Remaining gaps** — Cannot create empty Delta tables from ClickHouse yet; MSAN builds of the kernel are disabled due to `ring` crate issues.

## Key Claims

- "Adopting these table formats is not trivial. Supporting them requires keeping up with complex and evolving protocols."
- "By adopting the Delta Kernel, we were able to focus on query execution and performance, while relying on a shared implementation for protocol correctness and feature completeness."
- "Rust's approach to composing dependencies introduces significantly more complexity than C++, making integration and control over the build far more challenging."
- "The Delta Kernel provides full support for managing writes to Delta tables at the transactional level."
- "We've spent easily 20 to 50 times more effort debugging and setting up Rust builds than reading Rust code."

## Connections

- Details [[clickhouse]]'s Delta Lake integration strategy and build system
- Explains [[delta-kernel]] architecture and Engine APIs
- Builds on [[delta-lake]] by showing how the Kernel enables feature coverage
- References [[change-data-capture]] via ClickHouse CDF and ClickPipes
