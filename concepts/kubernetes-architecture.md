---
title: "Kubernetes Architecture"
type: concept
tags: [kubernetes, architecture, cloud-native, control-plane, reconciliation]
created: 2026-07-13
updated: 2026-07-13
sources: [kubeschool-kubernetes-primer, programming-kubernetes]
aliases: [k8s-architecture, kubernetes-internals]
---

## Summary

**Kubernetes Architecture** is the design of a level-triggered control system that continuously reconciles actual state toward declared desired state. It splits into two layers: the **control plane** (decision-making) and **worker nodes** (execution). Every component coordinates through the API server as a single hub — no component orders another around. The architecture is deliberately extensible through plugin interfaces (CNI, CSI) and the same object-plus-controller pattern used by the core.

## The Reconciliation Loop

> You declare outcomes, the system enforces them. Stop thinking in commands and start thinking in the state you want to be true.

The loop is **level-triggered**, not edge-triggered. A controller that was asleep or disconnected simply looks at reality when it wakes up and corrects whatever gap it finds — it doesn't need a perfect event history. This is what makes Kubernetes hard to knock over.

Every useful behavior follows from this one mechanism: self-healing (pod missing → create replacement), scaling (count changed → adjust), rollout (old state → new state in controlled steps).

## The Object Model: Spec + Status

Everything in Kubernetes is an API object with the same shape:

- **spec**: the desired state you declared
- **status**: the observed state the system reports back

You write the spec. Controllers write the status. The gap between the two is the work the system is doing. Objects live in versioned API groups (`apps/v1`, `networking.k8s.io/v1`) — the version signals stability from alpha to stable.

## The Hub-and-Spoke Coordination Model

No component calls another in a chain for cluster state. Every component talks to the API server and nothing else. They stay current using **watches** — long-lived subscriptions where the API server streams changes. A component does talk directly to the things it drives on its own machine (the kubelet drives the container runtime), but it learns *what* to do only from the API server.

## Control Plane Components

| Component | Role |
| --- | --- |
| **API Server** | Front door; auth → authorization → admission pipeline; only component touching etcd directly |
| **etcd** | Distributed KV store holding entire cluster state; Raft consensus (odd members: 3 or 5); sensitive to disk write latency — SSD/NVMe mandatory |
| **Scheduler** | Two-pass placement: filter infeasible nodes, score remaining; steered by taints/tolerations, affinities, topology spread, priority |
| **Controller Manager** | Runs many controllers side-by-side: node health, replicas, endpoints, namespace lifecycle |
| **Cloud Controller Manager** | Provider-specific logic (e.g., creating cloud load balancers); keeps core Kubernetes provider-agnostic |

## Worker Node Components

| Component | Role |
| --- | --- |
| **Kubelet** | Agent on every node; ensures assigned pods' containers are running and healthy; handles node-pressure eviction |
| **Container Runtime** | Actually runs containers via CRI; containerd or CRI-O with runc underneath |
| **Kube-proxy** | Makes service virtual IPs actually work; iptables (default), nftables (modern), or replaced entirely by eBPF-based CNI |

## High Availability

- **API servers**: active-active behind a load balancer
- **Scheduler + Controller Manager**: active-passive with leader election
- **etcd**: odd-numbered cluster (3 or 5) for Raft majority

Managed Kubernetes services handle this redundancy — a large reason teams choose them.

---

- Foundation for [[kubernetes-operator]] — operators reuse the same object-plus-controller pattern and reconcile loop
- Related to [[kubernetes-networking]] — the CNI plugin model extends the architecture's networking layer
- Related to [[kubernetes-security]] — RBAC, admission control, and policy engines plug into the API server pipeline
- Related to [[distributed-consensus]] — etcd uses Raft for consensus across control-plane nodes
- Related to [[containerization]] — Kubernetes orchestrates containers; understanding the runtime layer is prerequisite
- Benchmark source: [[sources/kubeschool-kubernetes-primer]] — Portainer's architectural primer
- Benchmark source: [[sources/programming-kubernetes]] — control loops, CRDs, extension patterns
