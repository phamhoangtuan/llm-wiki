---
title: "Benchmarking Vortex File Format vs Parquet, CSV — DuckDB, Polars, DataFusion"
type: source
source_type: article
author: "Daniel Beach"
url: "https://dataengineeringcentral.substack.com/p/benchmarking-vortex-file-format-vs"
source_date: 2026-05-25
ingested: 2026-05-26
created: 2026-05-26
updated: 2026-06-15
tags: [file-formats, benchmarking, vortex, parquet, duckdb, polars, datafusion]
concepts: [vortex-file-format, polars, apache-datafusion, duckdb, apache-parquet, lance-file-format]
---

## Summary

Daniel Beach benchmarks the **[[vortex-file-format|Vortex]] file format** (a Rust-based next-generation columnar format) against CSV, [[apache-parquet|Parquet]], and (briefly) [[lance-file-format|Lance]], using [[duckdb|DuckDB]], [[polars|Polars]], and [[apache-datafusion|DataFusion]] as query engines. The dataset is Backblaze's open-source hard drive failure data — ~24 GB across 184 CSV files.

## Benchmark Results

| Format + Engine | Runtime | Notes |
|---|---|---|
| CSV + DuckDB | 25.465s | Baseline |
| CSV + Polars | OOM | Crashed with memory errors |
| CSV + DataFusion | 5.106s | Fastest CSV scan |
| Parquet + DuckDB | 0.125s | 200× faster than CSV |
| Parquet + DataFusion | 0.370s | |
| Parquet + Polars | 0.193s | |
| Vortex (pure scan) | 0.111s | Native vortex scan with filter pushdown |
| Vortex + DuckDB (via PyArrow) | 0.201s | DuckDB vortex extension OOM'd; fell back to Arrow bridge |
| Vortex + Polars (via PyArrow) | 0.114s | `to_polars()` LazyFrame; no globbing support |

## Key Findings

1. **DataFusion was fastest on raw CSV** — 5× faster than DuckDB on CSV, demonstrating excellent CSV parsing performance.
2. **Parquet is 200× faster than CSV** — the jump from CSV to any columnar format dwarfs differences between columnar formats.
3. **Vortex marginally faster than Parquet** — best Vortex time (0.111s pure scan) slightly beats best Parquet time (0.125s DuckDB), but the gap is small.
4. **Python integrations are immature** — DuckDB's vortex extension caused OOM crashes; Polars required file-by-file loading (no globbing); most integrations required converting to PyArrow first.
5. **Polars reliability issues** — author repeats earlier criticism: Polars OOM'd on CSV where DuckDB and DataFusion handled the same data without issue. Author claims to have "ripped Polars out of production" for this reason.

## Author's Conclusion

The performance lift over Parquet may not justify the hassle of immature Python integrations, ugly bridge code, and OOM issues when reading directories of Vortex files. The format shows promise but is "early days" in the Python ecosystem.

## Links

- [All benchmark code on GitHub](https://github.com/danielbeach/benchmarkingVortex)
- [Vortex documentation](https://docs.vortex.dev/)
- [Vortex GitHub repository](https://github.com/vortex-data/vortex)
- [Backblaze hard drive dataset](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data)
- [Author's earlier article on replacing Polars with DuckDB](https://dataengineeringcentral.substack.com/p/why-im-replacing-polars-with-duckdb)

---

- Related to [[vortex-file-format]] — the columnar file format under benchmark evaluation
- Related to [[polars]] — DataFrame library tested; OOM'd on CSV, competitive on Parquet/Vortex
- Related to [[apache-datafusion]] — fastest CSV parser in the benchmark (5.106s)
- Related to [[duckdb]] — fastest Parquet engine (0.125s); vortex extension OOM'd
- Related to [[apache-parquet]] — the incumbent format to beat
- Related to [[lance-file-format]] — another next-gen columnar format, briefly mentioned
