---
title: "Go Web Programming"
type: source
source_type: book
author: "Sau Sheong Chang"
url: ""
source_date: 2015-01-01
ingested: 2026-06-03
tags: [go, web, golang, http, backend, concurrency]
concepts: [goroutines, go-http-handlers, go-template-escaping, go-web-ecosystem, middleware-pattern]
---

## Summary

*Go Web Programming* by Sau Sheong Chang (314 pages) teaches building web applications with Go's standard library — not heavyweight frameworks. The core philosophy: understand the plumbing of web development before reaching for abstractions. Rejects "Cargo Cult Programming" (copy-paste without understanding why).

## Key Topics

### HTTP from the Ground Up

- HTTP is stateless, text-based, request-response. Each cycle is independent.
- Request structure: request-line, headers, empty line, optional body.
- GET (safe, idempotent) vs POST (neither) — semantic distinctions matter.

### Handlers & ServeMux

- `ServeMux` acts as a "traffic cop" — inspects URL and routes to the correct handler.
- `/path` = exact match; `/path/` = subtree match (captures all sub-paths).
- `Handler` (interface with `ServeHTTP`) vs `HandlerFunc` (convenience function) — choose based on whether you need state.

### Template Engine & Security

- Go's `html/template` provides **context-aware escaping**: understands whether data lands in HTML, attributes, or JavaScript — escapes accordingly for XSS protection by default.
- `text/template` lacks this safety — use `html/template` for web output.

### Concurrency with Goroutines

- Goroutines: ~2KB stack vs ~1MB for OS threads — hundreds of thousands on one machine.
- Concurrency ≠ Parallelism: concurrency is dealing with many things at once; parallelism is doing many things at once.
- Each incoming HTTP request is handled in its own goroutine by default.

### Middleware Chaining

- Middleware wraps handlers: `protect(logRequests(handler))` — like Lego bricks.
- Cross-cutting concerns (auth, logging) stay separate from business logic.

### Deployment

- Go compiles to a **single static binary** — no app server (Tomcat), no dependencies, instant startup.
- `ListenAndServeTLS` enables HTTPS + HTTP/2 natively.
- Deploy options: standalone, Docker/Kubernetes, cloud platforms.

## Key Quotes

> "In Go, we reject Cargo Cult Programming — copy-pasting code without understanding why."

> "The beauty of Go lies in its simplicity. By relying on powerful standard libraries, you avoid the cargo cult confusion of heavy frameworks."

> "Concurrency is about dealing with lots of things at once; parallelism is about doing lots of things at once." — Rob Pike
