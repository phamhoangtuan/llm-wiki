---
title: "Kubernetes Operator"
type: concept
tags: [kubernetes, operators, controllers, cloud-native, golang, automation]
created: 2026-06-08
updated: 2026-06-15
sources: [programming-kubernetes]
aliases: [k8s-operator, kubernetes-controller]
---

## Summary

A Kubernetes Operator is a software extension that encodes domain-specific operational knowledge into automated controllers. Built on the control loop pattern (READ → CHANGE → UPDATE), operators watch custom resources and reconcile actual state toward desired state — turning manual SRE procedures into version-controlled, testable code. Operators are the mechanism that makes Kubernetes self-healing and self-managing.

## Running on K8s vs Programming K8s

| Approach | Description | Example |
| --- | --- | --- |
| **Run on K8s** 📦 | Deploy existing software onto a cluster | `kubectl apply -f deployment.yaml` |
| **Program K8s** 🔧 | Build applications aware of K8s, using APIs to manage state | Write a controller that auto-scales a database on load |

> One is a tenant. The other is a builder who reads the building's blueprints.

## The Control Loop: READ → CHANGE → UPDATE

Every Kubernetes controller and operator follows this universal pattern:

```
┌────────────────────────┐
│ 1. READ: Observe state  │ → Watch API events, detect drift from desired state
└────────┬───────────────┘
         ▼
┌────────────────────────┐
│ 2. CHANGE: Act          │ → Create, modify, or delete resources to close the gap
└────────┬───────────────┘
         ▼
┌────────────────────────┐
│ 3. UPDATE: Report       │ → Update .status in the API, emit logs, export metrics
└────────────────────────┘
```

**Analogy**: A thermostat — reads temperature (READ), turns AC on/off (CHANGE), updates the display (UPDATE).

## Operator = CRD + Custom Controller

An operator has two components:

| Component | Role | Example |
| --- | --- | --- |
| **Custom Resource Definition (CRD)** 📋 | Defines the schema for a domain-specific resource | `kind: PostgreSQLCluster` with fields: `replicas`, `storageSize`, `version` |
| **Custom Controller** ⚙️ | Supervises those resources, manages their lifecycle | Auto-provisions, backs up, failovers, and upgrades the PostgreSQL cluster |

Instead of 10 manual `kubectl` commands:

```yaml
apiVersion: database.example.com/v1
kind: PostgreSQLCluster
metadata:
  name: prod-db
spec:
  replicas: 3
  storageSize: 100Gi
  backupSchedule: "0 2 * * *"
```

→ The operator handles everything: provisioning, scaling, backup, recovery, upgrade.

> Operators turn tribal SRE knowledge into code that can be version-controlled, tested, and reused.

## The Go Ecosystem

Kubernetes is written in Go, and the ecosystem mirrors that:

| Library | Purpose |
| --- | --- |
| **client-go** 🚀 | Standard library for K8s API interaction — `clientset.CoreV1().Pods(ns).Get(ctx, name, opts)` |
| **API Machinery** ⚙️ | Building blocks for K8s-like APIs — Kinds, Resources, Schemes (Go type ↔ API mapping) |

**Pro tip**: Always use informers and caches from `client-go` instead of polling the API directly — reduces load on the API server.

## Extension Patterns

Three ways to extend Kubernetes, in order of complexity:

### 1. Custom Resource Definitions (CRDs) — Most Common

- **When**: Adding a new resource type with custom schema
- **Pros**: Easy to implement, integrates with `kubectl`, RBAC, validation
- **Cons**: Performance may be limited at extreme scale

### 2. Custom API Servers — For Edge Cases

- **When**: CRDs are too limiting — need custom storage backend, subresources, or high performance
- **Trade-off**: Significantly more complex to build and maintain

### 3. Webhooks — Dynamic Admission Control

- **Mutating Webhook**: Modify requests before etcd persistence (e.g., inject sidecar)
- **Validating Webhook**: Reject invalid requests (e.g., block images from untrusted registries)

## Production-Ready Operators

Three pillars for deploying operators to production:

| Pillar | Tools | Practice |
| --- | --- | --- |
| **Packaging** | Helm (templating, rollback), Kustomize (overlays, native) | Versioned releases, dependency management |
| **Security** | RBAC, ServiceAccounts | Least privilege — grant only required verbs on required resources |
| **Observability** | Prometheus metrics, structured JSON logs, OpenTelemetry tracing | Track reconciliation counts, latency, error rates per controller |

```go
// Export metrics for controller health
reconciliationsTotal.WithLabelValues(controllerName, result).Inc()
reconcileDuration.WithLabelValues(controllerName).Observe(duration.Seconds())
```

---

- Built on [[kubernetes-architecture]] — operators reuse the same reconcile loop, watch mechanism, and spec/status model as core controllers
- Related to [[go-web-ecosystem]] — Go's standard-library philosophy, static binaries, and implicit interfaces power the K8s ecosystem
- Related to [[goroutines]] — controllers leverage Go's lightweight concurrency for watch loops and parallel reconciliation
- Related to [[observability]] — production operators require metrics, logs, and traces for cluster health visibility
- Benchmark source: [[sources/programming-kubernetes]] — Schimanski & Hausenblas's 244-page guide
