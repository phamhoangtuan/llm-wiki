---
title: "Cloud Service Models"
type: concept
tags: [cloud, infrastructure, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [IaaS, PaaS, SaaS]
---

Cloud service models represent three levels of infrastructure abstraction, each trading control for operational simplicity.

## The Three Models

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Applications | ✅ You | ✅ You | ☁️ Provider |
| Data | ✅ You | ✅ You | ☁️ Provider |
| Runtime | ✅ You | ☁️ Provider | ☁️ Provider |
| Middleware | ✅ You | ☁️ Provider | ☁️ Provider |
| OS | ✅ You | ☁️ Provider | ☁️ Provider |
| Virtualization | ☁️ Provider | ☁️ Provider | ☁️ Provider |
| Servers/Storage/Networking | ☁️ Provider | ☁️ Provider | ☁️ Provider |

**IaaS (Infrastructure-as-a-Service)** gives granular control over raw infrastructure. You rent compute, storage, and networking, but manage everything from the OS up. Examples: AWS EC2, Google Compute Engine. Best when you need full control over the environment.

**PaaS (Platform-as-a-Service)** optimizes for developer velocity. The provider manages the runtime and all underlying complexity — you focus on code and data only. Examples: Heroku, Google App Engine. Best when you want to ship fast without infrastructure concerns.

**SaaS (Software-as-a-Service)** delivers zero operational overhead. You pay to use a complete product; the provider handles ALL technical layers. Examples: Gmail, Salesforce, Slack. Best when the problem is solved by existing software.

## Choosing a Model

> Analogy: On-premises = raising cows for milk. Cloud = buying milk at the supermarket. You still get the end product, but don't worry about the barn, feed, or veterinary care.

The choice depends on business needs: IaaS for control, PaaS for velocity, SaaS for simplicity. You trade off flexibility against operational burden at each step.

---
- Builds on [[containerization]] — containers typically run on IaaS/PaaS infrastructure
- Foundation for [[scalable-architecture]] — cloud elasticity enables horizontal scaling
- Foundation for [[system-design-interview]] — cloud is the default deployment substrate