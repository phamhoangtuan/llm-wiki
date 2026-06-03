---
title: "Go HTTP Handlers"
type: concept
tags: [go, golang, http, handlers, middleware, web]
created: 2026-06-03
updated: 2026-06-03
sources: [go-web-programming]
---

## Summary

In Go's standard library, HTTP handlers are the core abstraction for processing web requests. A handler receives a request, executes business logic, and writes a response. Combined with `ServeMux` (the router) and middleware chaining, handlers form a clean, modular alternative to heavyweight MVC frameworks.

## Handler vs HandlerFunc

Go provides two ways to define request handlers:

| Type | Definition | Use When |
|------|-----------|----------|
| **Handler** (interface) | Type with method `ServeHTTP(w ResponseWriter, r *Request)` | Need custom handler with state (e.g., database handle) |
| **HandlerFunc** (function) | Function with signature `func(w ResponseWriter, r *Request)` | Simple handler, no internal state needed |

```
// HandlerFunc — simple, convenient
http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "Hello, World!")
})

// Handler interface — when you need state/dependencies
type MyHandler struct {
    db *sql.DB
}
func (h *MyHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    // Access h.db here
}
```

## ServeMux — The Router

`ServeMux` inspects incoming request URLs and dispatches to the correct handler.

| Pattern | Matching Behavior |
|---------|-------------------|
| `/login` | **Exact match** — only `/login` |
| `/thread/` | **Subtree match** — `/thread/123`, `/thread/456/edit`, etc. |

```
mux := http.NewServeMux()
mux.HandleFunc("/login", loginHandler)
mux.HandleFunc("/thread/", threadHandler)
```

## The 3 Core Handler Responsibilities

1. **Receive & Process**: Unpack the HTTP request, perform business logic.
2. **Call Template Engine**: Pass data to generate HTML output.
3. **Bundle Response**: Wrap HTML into HTTP response and send.

## Middleware Chaining

Middleware wraps handlers in layers — like Lego bricks — for cross-cutting concerns:

```
func protect(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if !isValidSession(r) {
            http.Redirect(w, r, "/login", http.StatusSeeOther)
            return
        }
        next.ServeHTTP(w, r)
    })
}

mux.Handle("/dashboard", protect(dashboardHandler))
mux.Handle("/profile", protect(logRequests(profileHandler)))
```

**Benefits**:
- Business logic stays clean — not polluted by auth/logging code.
- Middleware is reusable — DRY, consistent security across endpoints.
- Easy to test each layer independently.

---
- Built on [[goroutines]] — each handler invocation runs in its own goroutine
- Foundation for [[go-web-ecosystem]] — handlers are the building blocks of Go web apps
- Related to [[dependency-injection]] — handlers get dependencies injected (e.g., db handle) for testability
