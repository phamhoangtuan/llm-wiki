---
title: "Containerization"
type: concept
tags: [containers, docker, virtualization, infrastructure, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [Docker, containers]
---

Containerization packages software code with all its dependencies (libraries, frameworks) into an isolated unit called a container. Unlike virtual machines, containers share the host OS kernel — no guest OS needed.

## Containers vs Virtual Machines

**Virtualized Stack**: Infrastructure → Host OS → Hypervisor → Guest OS → App

**Containerized Stack**: Infrastructure → Host OS → Container Engine → App (with dependencies)

The critical difference: containers virtualize the **Operating System**, not hardware. No need to boot a Guest OS for each application.

## Three Core Benefits

| Benefit | Explanation | Example |
|---------|-------------|---------|
| Isolation 🧱 | Apps sandboxed with specific requirements, avoiding version conflicts | App A needs Python 3.8, App B needs 3.11 — run side by side without conflict |
| Portability 🌍 | "Build once, run anywhere" — container runs on laptop = production | Docker image built on Mac → deploy to AWS Linux unchanged |
| Speed ⚡ | No hypervisor + no Guest OS boot → instant-on start times | Container starts ~100ms vs VM ~30s |

## Production Pattern

Modern production environments commonly use **"Containerized on Virtualized"** — combining the security isolation of VM boundaries with the deployment agility of containers. You don't have to choose one.

---
- Builds on [[cloud-service-models]] — containers typically run on IaaS/PaaS
- Foundation for [[deployment-strategies]] — containers enable Blue-Green and Canary rollouts
- Contrast with [[goroutines]] — OS-level container isolation vs language-level concurrency