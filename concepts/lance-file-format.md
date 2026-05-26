---
title: "Lance File Format"
type: concept
tags: [file-formats, columnar, ml, data-engineering]
created: 2026-05-26
updated: 2026-05-26
sources: [benchmarking-vortex-file-format]
---

## Summary

**Lance** is a modern columnar file format optimized for machine learning and AI workloads. It was mentioned as another "[[apache-parquet|Parquet]] alternative" alongside [[vortex-file-format|Vortex]] in Daniel Beach's benchmarking article, though it was not actually tested in the benchmarks.

## Key Characteristics

- **Columnar storage** — like Parquet, stores data by column for efficient compression and selective reads
- **Random access** — optimized for accessing specific rows without scanning the entire file (important for ML training data sampling)
- **Versioning** — built-in support for dataset versioning (useful for ML experiment tracking)
- **ML-native** — designed with machine learning workflows (training, shuffling, sampling) in mind

## Position in the Ecosystem

Lance competes in the same space as other "next-generation" columnar formats aiming to improve on Parquet:

| Format | Primary Niche |
|---|---|
| [[apache-parquet|Parquet]] | General-purpose analytics (incumbent) |
| [[vortex-file-format|Vortex]] | High-performance scans, object storage |
| **Lance** | ML/AI workloads, random access, versioning |
| Apache ORC | Hive ecosystem, nested data |

> **Note**: This page is a stub — Lance was mentioned but not evaluated in the source. A dedicated source or deeper investigation would add substance.
---
- Competes with [[apache-parquet]] — Lance is another next-gen columnar format targeting Parquet's dominance
- Related to [[vortex-file-format]] — both are modern columnar formats seeking to replace Parquet for specific workloads
- Reference: [[benchmarking-vortex-file-format]] — mentioned as a comparison target (not tested)
