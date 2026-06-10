---
title: "Programming Kubernetes"
type: source
source_type: book
author: "Stefan Schimanski & Michael Hausenblas"
source_date: 2019-01-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-08
url: ""
tags: [kubernetes, golang, operators, controllers, cloud-native]
concepts: [kubernetes-operator]
---

## Summary

A 244-page guide to building Kubernetes-native applications — software that doesn't just run on K8s but interacts directly with the API server to manage cluster state. Covers the control loop pattern (READ → CHANGE → UPDATE), the Operator model (CRD + Custom Controller), extension patterns (CRDs, Custom API Servers, Webhooks), the Go ecosystem (client-go, API Machinery), and production concerns (Helm/Kustomize packaging, RBAC, observability).

## Core Message

> Don't just deploy applications on Kubernetes. Build Kubernetes-native applications — programs that speak the API, leverage declarative state management, and achieve maximum portability and automation.

## Key Takeaways

1. **Native > Hosted**: Programming Kubernetes means building apps aware they run on K8s — tenants build the house, not just live in it
2. **Control Loop is the heart**: READ (observe) → CHANGE (act) → UPDATE (report) — the universal automation pattern
3. **Operators encode operational knowledge**: CRD + Custom Controller = Operator — turn SRE tribal knowledge into version-controlled code
4. **Go + client-go is the gold standard**: Kubernetes itself is Go; the ecosystem (informers, caches, API Machinery) is Go-native
5. **Extend strategically**: CRDs for most use cases, Custom API Servers for edge cases, Webhooks for validation/mutation
6. **Production needs 3 pillars**: Packaging (Helm/Kustomize) + Security (RBAC, least privilege) + Observability (logs/metrics/traces)

## Companion Concept

→ [[kubernetes-operator]] — the control loop, operator pattern, and extension points
