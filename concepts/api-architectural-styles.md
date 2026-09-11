---
title: "API Architectural Styles"
type: concept
tags: [api, architecture, system-design, web]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [REST, GraphQL, gRPC, SOAP]
---

API architectural styles define how clients and servers communicate. Each style optimizes for different use cases — no single style is universally best.

## Four Major Styles

| Style | Characteristics | Format | Best For |
|-------|----------------|--------|----------|
| SOAP 📦 | Enveloped message structure, strict contracts (WSDL), built-in error handling | XML only | Enterprise systems, legacy integrations |
| REST 🌐 | Resource-driven, stateless, cacheable, uses HTTP methods (GET/POST/PUT/DELETE) | JSON, XML, HTML | Public APIs, web services, most modern applications |
| GraphQL 🔍 | Schema-driven, client specifies exact data needs, single endpoint | JSON | Mobile apps, complex data requirements, reducing over-fetching |
| gRPC ⚡ | Local procedure call style, high performance, binary protocol, streaming support | Protocol Buffers | Internal microservices, low-latency requirements |

## Choosing the Right Style

- **REST**: Default choice for public APIs. Simple, cacheable, ubiquitous tooling.
- **GraphQL**: When clients need flexible queries and bandwidth matters (mobile). Trade-off: complex server-side resolver logic.
- **gRPC**: When latency matters and you control both client and server. Trade-off: requires Protobuf tooling, less human-readable.
- **SOAP**: Legacy enterprise systems with strict contracts and formal error handling. Avoid for new projects unless integrating with existing SOAP services.

## Key Insight

> API style choice reflects architectural priorities: REST for simplicity and scale, GraphQL for client flexibility, gRPC for performance, SOAP for contract formality.

---
- Builds on [[http-evolution]] — HTTP/2 enables gRPC's multiplexed streaming
- Foundation for [[system-design-interview]] — API design is a fundamental system design skill
- Foundation for [[orchestration-vs-choreography]] — gRPC excels in orchestrated microservices