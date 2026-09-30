---
title: "Databricks Zerobus — Event Streams + Lake House"
type: source
source_type: article
author: "Daniel Beach"
url: "https://dataengineeringcentral.substack.com/p/databricks-zerobus-event-streams"
source_date: 2026-06-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-15
tags: [streaming, delta-lake, databricks, kafka, lakehouse]
concepts: [delta-lake, apache-kafka]
---

## Summary

Daniel Beach explores Databricks Zerobus — a serverless, API-based streaming ingestion service that pushes events directly into Delta Lake without Kafka or Spark Streaming overhead. Covers what Zerobus is (gRPC/REST/OpenTelemetry, push-only, Arrow-native), how to use it (endpoint config, OAuth, SDK, Arrow schema), and a hands-on test with Divvy bike trip data. Finds it surprisingly slick for simple use cases, with the caveat that file management (OPTIMIZE) becomes critical at production scale.

## Core Message

> Streaming to a Lake House shouldn't require a legion of engineers babysitting Kafka clusters. Zerobus simplifies streaming ingestion into Delta Lake to a few API calls — no infrastructure to maintain, SDKs are straightforward, Arrow-native. It's to Kafka what DuckDB is to Spark: eating at the edges, not replacing, but dramatically lowering the barrier.

## Key Takeaways

1. **Zerobus = serverless streaming into Delta Lake**: gRPC, REST, OpenTelemetry APIs — push-only, no pull/broker architecture
2. **No Kafka/Spark Streaming needed**: Removes infrastructure complexity for Lake House streaming ingestion
3. **Arrow-native**: Uses Apache Arrow Flight for data transfer, schema defined via PyArrow
4. **Caveats**: Serverless compute not yet supported (requires All-Purpose cluster), file fragmentation requires OPTIMIZE management at scale
5. **Ecosystem shift**: Streaming is complex — tools like Zerobus (and Arroyo) are making it accessible to teams without dedicated streaming infrastructure engineers

## Companion Concepts

→ [[delta-lake]] — Zerobus ingests directly into Delta tables
→ [[apache-kafka]] — Zerobus is a Kafka alternative for Lake House use cases
