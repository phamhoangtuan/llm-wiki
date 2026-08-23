---
title: "Middleware Pattern"
type: concept
tags: [go, golang, http, middleware, web, design-patterns]
created: 2026-06-08
updated: 2026-06-15
sources: [go-web-programming]
aliases: [middleware-chaining, handler-wrapping]
---

## Summary

The Middleware Pattern wraps HTTP handlers with composable layers of cross-cutting behavior — authentication, logging, rate limiting, compression. Each middleware is a function that takes a handler and returns a handler, forming chains like `protect(logRequests(handler))`. This pattern keeps business logic clean by separating orthogonal concerns into reusable, stackable components.

## How It Works

Each middleware is a higher-order function:

```go
func logRequests(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s", r.Method, r.URL.Path)
        next.ServeHTTP(w, r)
    })
}

func protect(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if !isAuthenticated(r) {
            http.Error(w, "Unauthorized", 401)
            return
        }
        next.ServeHTTP(w, r)
    })
}
```

**Chaining**: `protect(logRequests(handler))` — requests pass through `protect` (auth check) → `logRequests` (logging) → the core handler. Like Lego bricks — each middleware adds one responsibility without touching the others.

## Why This Pattern

| Problem | Middleware Solution |
|---|---|
| Cross-cutting concerns mixed into handlers | Separate auth, logging, CORS into middleware |
| Repeated boilerplate in every handler | Write once, stack everywhere |
| Hard to add/remove orthogonal behavior | Add or drop middleware without changing handlers |
| Testing concerns in isolation | Test each middleware independently |

## The Three Middleware Rules

1. **Middleware wraps a handler** — takes `http.Handler`, returns `http.Handler`
2. **Order matters** — outer middleware runs first (e.g., auth before logging)
3. **Middleware is stateless** — each request gets a fresh chain

## In Go's Standard Library

Go's `net/http` supports middleware natively through the `http.Handler` interface. No framework required:

```go
mux := http.NewServeMux()
mux.HandleFunc("/api/data", dataHandler)

// Stack middleware from outside-in:
handler := protect(logRequests(recoverPanic(mux)))
http.ListenAndServe(":8080", handler)
```

## Common Middleware Examples

| Middleware | Purpose |
|---|---|
| **Auth** | Validate tokens/sessions; reject unauthorized requests |
| **Logging** | Record method, path, duration, status code |
| **Recovery** | Catch panics, return 500 instead of crashing |
| **CORS** | Set cross-origin headers for browser access |
| **Rate Limiting** | Throttle requests per IP/user |
| **Compression** | Gzip response bodies for bandwidth savings |
| **Tracing** | Inject trace IDs for distributed observability |

---

- Built on [[go-http-handlers]] — middleware operates on the `http.Handler` interface
- Core to [[go-web-ecosystem]] — middleware chains embody Go's standard-library-first philosophy
- Benchmark source: [[sources/go-web-programming]] — Sau Sheong Chang's guide to Go web apps
