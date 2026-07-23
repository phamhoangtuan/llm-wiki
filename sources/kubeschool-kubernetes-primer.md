---
title: "KubeSchool — Understanding Kubernetes, an Architectural Primer"
type: source
source_type: article
author: "Portainer"
url: "https://kubeschool.portainer.io/"
source_date: 2025-01-01
ingested: 2026-07-13
tags: [kubernetes, architecture, cloud-native, networking, security, operators]
concepts: [kubernetes-architecture, kubernetes-networking, kubernetes-security, kubernetes-operator, containerization]
---

## Summary

Portainer's KubeSchool is a 15-chapter architectural primer on Kubernetes — not a tutorial, but a fluency course for how Kubernetes is put together, why it's built that way, and where its sharp edges are. It stays at the level of architecture, principles, and constraints, deliberately avoiding internals-level packet and syscall details. The central thesis: Kubernetes is a level-triggered control system whose whole job is making actual state match desired state, continuously.

## Chapter Map

| Ch | Topic | Core Idea |
| --- | --- | --- |
| 00 | What Kubernetes Actually Is | A cluster-as-a-platform that pools servers, schedules containers, and self-heals |
| 01 | Reconciliation | Desired state → Actual state loop; level-triggered, not edge-triggered |
| 02 | Object Model | Everything is an API object: spec (desired) + status (observed); versioned API groups |
| 03 | Watch & Reconcile Fabric | Every component talks to the API server and nothing else; coordination through shared state |
| 04 | Control Plane | API server (auth→authz→admission pipeline), etcd (Raft, odd members, backup), scheduler (filter+score), controller manager |
| 05 | Worker Nodes | Kubelet, Container Runtime Interface (CRI), kube-proxy (iptables/nftables/eBPF) |
| 06 | Pods & Workloads | Pods are ephemeral; requests/limits + QoS classes; liveness/readiness/startup probes; Deployment, StatefulSet, DaemonSet, Job |
| 07 | Networking | CNI plugin model; 4-layer model (container→pod→service→ingress); Services, CoreDNS, Ingress/Gateway API; HostPort/HostNetwork escape hatches |
| 08 | Storage | CSI plugin model; PV/PVC/StorageClass; dynamic provisioning; WaitForFirstConsumer for multi-zone |
| 09 | Configuration & Secrets | ConfigMap/Secret; secrets are base64 by default, not encrypted — enable encryption at rest + external vault |
| 10 | Scaling | HPA, VPA, Cluster Autoscaler, Karpenter; pod and node scaling are separate concerns |
| 11 | CRDs & Operators | CRDs add object types; operators install controllers running the same reconcile loop; Operator Framework capability levels (1-5); admission webhooks |
| 12 | Sizing | Control plane: 4+ CPU, 8GB+ RAM; etcd: sensitive to disk write latency (SSD/NVMe mandatory); lightweight distros (k3s, k0s, microk8s) |
| 13 | Failure Behavior | Node failure (auto-recovery), split-brain (duplicate pods, graceful cleanup), control-plane outage (data plane keeps running, management goes dark) |
| 14 | Enterprise Readiness | OIDC auth, RBAC, policy engines (OPA/Kyverno), multi-tenancy, secrets vault, image signing, observability, GitOps, certificate lifecycle |
| 15 | Sharp Edges | Resource requests/limits, secrets encoding, open default network, readiness probes, multi-zone storage, pod ephemerality |

## Design Philosophy

Kubernetes is a platform, not a product. It gives a powerful foundation and deliberately leaves gaps — networking (CNI), storage (CSI), auth (OIDC), policy (admission webhooks) — for you to fill with plugins suited to your environment. That tradeoff: enormous capability in exchange for real operational responsibility.
