---
title: "Goroutines"
type: concept
tags: [go, golang, concurrency, goroutines, performance]
created: 2026-06-03
updated: 2026-06-03
sources: [go-web-programming]
---

## Summary

Goroutines are Go's lightweight concurrency primitive — functions that run concurrently with other goroutines. Managed by the Go runtime (not the OS), they enable handling hundreds of thousands of concurrent tasks with minimal overhead. Every incoming HTTP request in a Go web server is handled in its own goroutine by default.

## Concurrency vs Parallelism

> "Concurrency is about dealing with lots of things at once; parallelism is about doing lots of things at once." — Rob Pike

| Concept | Definition | Analogy |
|---------|-----------|---------|
| **Concurrency** | Managing multiple tasks simultaneously (may not run in parallel) | One chef handling 10 orders: cooks dish A, preps dish B while waiting for water to boil |
| **Parallelism** | Executing multiple tasks truly at the same time (requires multiple CPU cores) | 10 chefs, each cooking one order simultaneously |

Concurrency is a **design property**; parallelism is a **runtime behavior**.

## How Goroutines Work

- **Stack size**: ~2KB initial stack (vs ~1MB for OS threads) — grows and shrinks as needed.
- **Multiplexing**: Go runtime schedules goroutines onto a small pool of OS threads (M:N scheduling).
- **Cost**: Spawning a goroutine is extremely cheap — like allocating a small object.
- **Scale**: One OS thread can schedule hundreds of thousands of goroutines.

```
go func() {
    logAnalytics(r) // Runs concurrently, doesn't block the response
}()

// Main logic continues immediately
fmt.Fprint(w, "Response sent!")
```

## Benefits for Web Applications

- **Vertical scaling**: Handle more concurrent requests on the same hardware.
- **Non-blocking I/O**: Goroutines yield during I/O waits, letting others run.
- **Simpler than threads**: No manual thread management, no callback hell.
- **Built-in**: Every `http.Handler` invocation runs in its own goroutine — no extra code needed.

## When to Use

- Background tasks (analytics, logging, notification sending) that shouldn't block the response.
- Concurrent I/O (multiple API calls, database queries) — fire them in parallel with goroutines + channels.
- Long-polling or WebSocket connections — each connection gets its own lightweight goroutine.

## Caution

Goroutines are not free. Profile before optimizing — `pprof` helps identify goroutine leaks and contention points.

---
- Foundation for [[go-web-ecosystem]] — goroutines are the engine behind Go's web scalability
- Related to [[go-http-handlers]] — each HTTP handler runs in its own goroutine
