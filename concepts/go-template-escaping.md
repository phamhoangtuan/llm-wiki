---
title: "Go Template Escaping"
type: concept
tags: [go, golang, templates, security, xss, html]
created: 2026-06-03
updated: 2026-06-03
sources: [go-web-programming]
---

## Summary

Go's `html/template` package provides **context-aware escaping** — it automatically escapes output based on where the data appears in the HTML document (element content, attribute value, JavaScript block, CSS). This makes XSS (Cross-Site Scripting) protection a default, not an afterthought. Unlike `text/template`, which treats all output as plain text, `html/template` understands HTML structure.

## Context-Aware Escaping

The engine knows the **context** where data is inserted and applies appropriate escaping:

| Context | Raw Input | Escaped Output |
|---------|-----------|---------------|
| HTML body | `<script>alert('xss')</script>` | `&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;` |
| HTML attribute `href` | `javascript:evil()` | `#ZgotmplZ` (rejected entirely) |
| JavaScript block | `"; alert('xss');"` | `\"; alert(\'xss\');\"` |

## text/template vs html/template

```
// ❌ text/template — no context awareness, vulnerable to XSS
import "text/template"
t := template.New("user").Parse("Hello {{.Name}}")
// Input: <script>alert('xss')</script>
// Output: Hello <script>alert('xss')</script> ← DANGER

// ✅ html/template — automatic escaping per context
import "html/template"
t := template.New("user").Parse("Hello {{.Name}}")
// Input: <script>alert('xss')</script>
// Output: Hello &lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt; ← SAFE
```

## Static vs Active Templates

| Type | Description | Examples |
|------|-------------|----------|
| **Static (Logic-less)** | HTML + placeholders, engine swaps tokens with data | Mustache, CTemplate |
| **Active Templates** | HTML + programming constructs (if, range, variables) | Go `html/template`, JSP, ERB |

Go's `html/template` is an **active template engine** — supports conditionals, loops, and variables — while maintaining security through context-aware escaping.

## Security Model

- **Defense in depth**: Even if a developer forgets to escape, the engine does it automatically.
- **Whitelist approach**: Only known-safe output is allowed in sensitive contexts (e.g., URLs in `href`).
- **Template nesting**: Escaping is applied correctly even when templates include other templates.

## Best Practices

- **Always** use `html/template` for web output, never `text/template`.
- Don't bypass escaping with `template.HTML` unless the content is proven safe.
- Let the template engine handle context — don't pre-escape data before passing it.

---
- Foundation for [[go-web-ecosystem]] — security-first templating is a pillar of Go web development
- Related to [[go-http-handlers]] — handlers pass data to templates for rendering
