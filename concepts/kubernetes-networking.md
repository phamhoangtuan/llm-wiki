---
title: "Kubernetes Networking"
type: concept
tags: [kubernetes, networking, cni, services, dns, cloud-native]
created: 2026-07-13
updated: 2026-07-13
sources: [kubeschool-kubernetes-primer]
aliases: [k8s-networking, kubernetes-network-model]
---

## Summary

**Kubernetes Networking** follows a simple model — every pod gets its own IP, pods talk directly across nodes without NAT, and a pod sees itself at the same address others use — but delegates implementation to a pluggable **CNI** (Container Network Interface). This is the same plugin philosophy used for storage (CSI): Kubernetes defines the abstraction, you pick the implementation fitting your environment.

## The Four-Layer Model

From innermost outward:

| Layer | What | How |
| --- | --- | --- |
| **Container** | Containers inside one pod | Share a network namespace; communicate over `127.0.0.1` (loopback) |
| **Pod** | Every pod gets a unique IP | CNI builds this network; any pod can reach any other directly, no NAT |
| **Service** | Stable virtual IP in front of volatile pods | ClusterIP (internal), NodePort, LoadBalancer; kube-proxy wires forwarding rules |
| **Ingress** | External traffic enters the cluster | Ingress controller routes by host/path; Gateway API is the modern successor |

## Tracing a Request

Public load balancer (:80) → NodePort (:31000, every node) → Service ClusterIP (virtual) → Pod IP → container (loopback). Each hop moves one layer inward. The response travels back along the same path.

## Service Discovery

Every service gets a DNS name: `service.namespace.svc.cluster.local`. CoreDNS resolves it to the stable ClusterIP. Within the same namespace, the short service name suffices. Across namespaces: `servicename.namespace`. Always reach services by name, never by pod IP — pod IPs are volatile.

## CNI Plugin Choice

| Approach | Characteristics |
| --- | --- |
| **Overlay** (Flannel, Calico) | Wraps pod traffic; simple and portable; small overhead |
| **Native routing + eBPF** (Cilium) | High-performance, fine-grained policy, often replaces kube-proxy entirely |

The CNI choice sets your performance, security model, and which features you can use.

## Sharp Edges

- **Default network is open**: any pod can reach any other until NetworkPolicies are applied — and those only work if your CNI enforces them
- **Service ClusterIP is virtual**: nothing listens on it; it's just forwarding rules
- **HostNetwork bypasses isolation**: the pod uses the host's IP and sees every interface — powerful and dangerous
- **LoadBalancer on bare metal**: needs MetalLB or kube-vip (Layer 2 or BGP mode) since there's no cloud provider to create one

---

- Part of [[kubernetes-architecture]] — networking is the CNI plugin extension of the architecture
- Related to [[kubernetes-security]] — NetworkPolicy enforcement is a core security boundary
- Related to [[load-balancer]] — the LoadBalancer service type and ingress controllers are Kubernetes-specific load balancing
- Related to [[containerization]] — pods share a network namespace, a Linux kernel feature for container isolation
- Benchmark source: [[sources/kubeschool-kubernetes-primer]]
