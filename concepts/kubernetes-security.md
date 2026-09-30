---
title: "Kubernetes Security"
type: concept
tags: [kubernetes, security, rbac, policy, secrets, cloud-native]
created: 2026-07-13
updated: 2026-07-13
sources: [kubeschool-kubernetes-primer]
aliases: [k8s-security, kubernetes-rbac]
---

## Summary

**Kubernetes Security** is the set of controls that protect the cluster at every layer of the API request pipeline — authentication, authorization, admission control — plus the runtime concerns of secrets management, network policy, image trust, and multi-tenancy. Kubernetes provides the mechanisms but deliberately leaves gaps: it has no built-in user store, secrets are only base64-encoded by default, and the default network is wide open.

## The API Request Pipeline

Every request to the API server runs a fixed three-stage pipeline:

1. **Authentication**: Who are you? (certificates, tokens, OIDC)
2. **Authorization**: Are you allowed to do this? (RBAC)
3. **Admission Control**: Does this meet policy? (mutating/validating webhooks)

## Key Security Mechanisms

| Mechanism | What It Does |
| --- | --- |
| **RBAC** | Defines what each identity may do, scoped to namespace or cluster; enforce least privilege |
| **OIDC Integration** | Kubernetes has no built-in user store — integrate corporate identity via OpenID Connect |
| **Policy Engines** (OPA Gatekeeper, Kyverno) | Reject or mutate objects that violate rules (e.g., no privileged containers, approved registries only) |
| **Pod Security Admission** | Enforces baseline safety standards across namespaces |
| **Network Policies** | Segment traffic between pods/namespaces — only effective if your CNI enforces them |
| **Secrets Encryption** | Secrets are base64-encoded by default — trivially reversible. Enable encryption at rest + use external vault |
| **Image Trust** | Only run signed, scanned images from approved registries; enforce at admission |

## Enterprise Security Posture

A complete enterprise Kubernetes security setup fills every gap in the platform:

| Layer | Enterprise Practice |
| --- | --- |
| Identity | OIDC integration with corporate SSO — no static credentials |
| Access | Fine-grained RBAC, least privilege per namespace |
| Policy | Kyverno/OPA rules enforced at admission — not wiki pages people ignore |
| Secrets | External vault (Vault, AWS Secrets Manager) as source of truth, synced via operator |
| Network | NetworkPolicy everywhere; default-deny within namespaces |
| Supply Chain | Signed images from approved registries; signature verification at admission |
| Audit | API audit log recording who did what; SIEM integration |

## Sharp Edges

- **Secrets are not secret by default** — treat base64 as encoding, not security
- **RBAC left open** is one of the most common ways clusters get compromised
- **The default network is open** — a compromised frontend has a clear path to your backend
- **Policy without enforcement** is just documentation

---

- Part of [[kubernetes-architecture]] — the API server pipeline (auth→authz→admission) is the security foundation
- Related to [[kubernetes-networking]] — NetworkPolicy is the primary traffic segmentation mechanism
- Related to [[shift-left-security]] — policy engines and image signing move security checks to admission time
- Related to [[sso]] — OIDC integration connects Kubernetes auth to corporate identity providers
- Benchmark source: [[sources/kubeschool-kubernetes-primer]]
