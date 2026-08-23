---
title: "Data Lifecycle — Data Engineering Handbook"
type: source
source_type: article
author: "Data Engineering Handbook (kythuatdulieu.github.io)"
url: "https://kythuatdulieu.github.io/concepts/foundation/data-lifecycle/"
source_date: 2026-06-07
ingested: 2026-06-14
created: 2026-06-14
updated: 2026-06-14
tags: [data-engineering, foundation, data-lifecycle, governance, best-practices]
concepts: [data-lifecycle, data-engineer]
---

## Summary

A comprehensive guide to the Data Lifecycle from the Vietnamese Data Engineering Handbook. Defines the six stages every piece of data traverses — from generation to destruction — and explains why lifecycle management is a critical part of Data Governance strategy. Covers the Hot Data vs Cold Data distinction, the three business drivers (cost optimization, GDPR compliance, security attack surface reduction), automation via cloud lifecycle rules (AWS S3 JSON policy example), best practices (classify data at source, full automation, encrypt archives), and common pitfalls (data hoarding, forgetting backups during deletion). Includes interview Q&A on GDPR's Right to be Forgotten (anonymization + crypto-shredding), BigQuery partition expiration, and Snowflake Time Travel.

## Core Message

> Data Lifecycle Management ensures that data — like any asset — is treated appropriately at every stage, from creation to destruction. Without it, data becomes a financial and legal liability rather than a strategic resource.

## Key Takeaways

1. **Six lifecycle stages**: Generation → Storage → Processing → Usage/Analytics → Archival → Destruction — each demands distinct handling
2. **Hot vs Cold data**: Hot data lives on SSD for real-time access; Cold data migrates to cheaper storage (HDD, Glacier) as access frequency drops
3. **Three business drivers**: Cost optimization (cheap storage for old data), compliance (GDPR right-to-be-forgotten), and security (reduce attack surface by destroying stale data)
4. **Automation is mandatory**: Manual lifecycle management fails at scale — cloud rules (AWS S3 Lifecycle, BigQuery partition expiration, Snowflake Time Travel) handle transitions and deletion automatically
5. **GDPR Right to be Forgotten**: Requires complete data purging across ALL systems including backups — solved via anonymization (replace PII with random strings) or crypto-shredding (delete encryption keys, rendering data unreadable)
6. **Data hoarding is the #1 pitfall**: "Keep it all — might need it someday" turns Data Lakes into Data Swamps, exploding cloud costs
7. **Backup oversight**: Deleting data from production DBs but forgetting backup copies still constitutes legal non-compliance under GDPR
8. **Lifecycle = cost lever**: Lifecycle policies can cut storage costs 50–90% by moving data through storage classes (STANDARD → STANDARD_IA → GLACIER → DELETE)

## Companion Concept

→ [[data-lifecycle]]
