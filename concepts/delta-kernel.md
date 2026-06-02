---
title: "Delta Kernel"
type: concept
tags: [delta-lake, delta-kernel, rust, table-formats, data-engineering]
created: 2026-06-02
updated: 2026-06-02
sources: [integrating-rust-delta-kernel-clickhouse]
aliases: [delta-kernel-rs, Rust Delta Kernel]
---

## Summary

The **Delta Kernel** (specifically `delta-kernel-rs`) is a Rust library that provides a shared, maintained abstraction layer for the [[delta-lake|Delta Lake]] protocol. Instead of each query engine implementing the Delta protocol from scratch, the Kernel centralizes protocol handling and exposes well-defined Engine APIs. Engines like [[clickhouse|ClickHouse]] plug in their own optimized Parquet readers and file access while the Kernel handles everything else.

## Architecture

```
┌──────────────────────────────────────────┐
│            QUERY ENGINE (e.g. ClickHouse) │
│  ┌────────────────────────────────────┐  │
│  │  Custom Parquet reader             │  │
│  │  Custom file access (S3, HDFS)     │  │
│  └───────────┬────────────────────────┘  │
│              │ Engine APIs                │
│  ┌───────────▼────────────────────────┐  │
│  │        DELTA KERNEL (Rust)          │  │
│  │  • Transaction log parsing          │  │
│  │  • Snapshot resolution              │  │
│  │  • Metadata interpretation          │  │
│  │  • Data skipping (partition+stats)  │  │
│  │  • Schema evolution reconciliation  │  │
│  │  • Write coordination               │  │
│  └───────────┬────────────────────────┘  │
└──────────────┼───────────────────────────┘
               │
┌──────────────▼───────────────────────────┐
│          DELTA TABLE FILES                │
│  _delta_log/  +  *.parquet               │
└──────────────────────────────────────────┘
```

## What the Kernel Abstracts

Instead of each engine independently implementing the [Delta protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md), the Kernel handles:

| Responsibility | Description |
|---|---|
| **Transaction log parsing** | Reads and interprets `_delta_log/*.json` files |
| **Snapshot resolution** | Determines the correct set of data files for a given version |
| **Data skipping** | Applies partition and statistics-based pruning to eliminate irrelevant files |
| **Schema evolution** | Exposes both logical schema (user-facing) and physical schema (Parquet files); provides schema transformation metadata per file |
| **Write coordination** | Manages transactional writes at the log level (Parquet files written by engine) |
| **CDF (Change Data Feed)** | Exposes row-level changes (inserts, updates, deletes) as event streams |

## Engine APIs

The Kernel is designed with a clear separation:
- **Engine provides**: Parquet file reading, object storage access (S3, HDFS, etc.)
- **Kernel provides**: Everything else — metadata, statistics, schema reconciliation, deletion vectors, snapshot management

This means engines can retain their heavily optimized I/O paths (e.g., ClickHouse's Parquet reader) while offloading protocol complexity.

## Adoption by ClickHouse

ClickHouse moved from a native Delta protocol implementation to the Delta Kernel because:

| Before (Native) | After (Kernel) |
|---|---|
| Full protocol implementation from scratch | Shared implementation; offload to Kernel |
| Each feature required independent work | Features inherited from Kernel updates |
| Hard to keep pace with evolving spec | Kernel tracks spec changes |
| Maintenance burden on ClickHouse team | Maintenance shared across ecosystem |

The Kernel integration unlocked: writes, schema evolution, time travel, partition pruning, statistics-based pruning, and CDF — much faster than would have been possible with native implementation.

## Upstream Contributions

ClickHouse contributed improvements to `delta-kernel-rs` found through production workloads:
- **Dynamic logging configuration** ([PR #1111](https://github.com/delta-io/delta-kernel-rs/pull/1111)) — replaced static logging init with runtime-configurable logging for debugging
- **Asynchronous metadata processing** ([PR #1827](https://github.com/delta-io/delta-kernel-rs/pull/1827)) — modified FFI to pass handles instead of references, enabling parallelized metadata reads

## Current Limitations

- **Cannot create empty tables** — the Kernel can attach to existing Delta tables but cannot initialize new ones (planned contribution)
- **OpenSSL dependency** — deep in dependency graph (`openssl` crate), conflicting with some build requirements
- **MSAN builds disabled** — `ring` crate (nested dependency) has issues with memory sanitizer
---
- Adopted by [[clickhouse]] — ClickHouse uses `delta-kernel-rs` for Delta Lake protocol handling via FFI
- Built on [[delta-lake]] — the Kernel is the protocol abstraction layer for Delta Lake
- Contrasts with native protocol implementations — Engines previously had to implement Delta specification directly
- Contributed to via [[integrating-rust-delta-kernel-clickhouse]] — ClickHouse's upstream PRs and build integration story
