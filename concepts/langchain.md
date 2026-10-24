---
title: "LangChain"
type: concept
tags: [llm, framework, agents, orchestration, python]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: []
---

## Summary

**LangChain** is an open-source Python/JS framework for building applications powered by Large Language Models. It provides modular components for chaining together LLM calls, integrating external tools (APIs, databases, search engines), and building autonomous agents that can plan and execute multi-step workflows.

## Core Components

| Component | Purpose |
|-----------|---------|
| **Chains** | Sequences of calls — LLM → tool → LLM → output |
| **Agents** | Dynamic reasoning loops where the LLM decides which tool to use next |
| **Tools** | Pre-built integrations (Google Search, Wikipedia, SQL databases, APIs) |
| **Memory** | Conversational context persistence across multiple interactions |
| **Document Loaders** | Ingest PDFs, web pages, databases for [[retrieval-augmented-generation|RAG]] |
| **Vector Stores** | Connectors for Pinecone, Weaviate, Chroma, pgvector |

## LangChain vs LlamaIndex

| Aspect | LangChain | [[llama-index|LlamaIndex]] |
|--------|-----------|------------------------|
| Focus | General LLM orchestration | Data indexing and retrieval |
| Strength | Multi-step workflows, tool use | Private data ingestion, advanced search |
| When to use | Complex agents, many tools | RAG on enterprise documents |
| Abstraction level | High (opinionated chains) | Medium (flexible pipelines) |

## When to Use LangChain

- Building chatbots that need to call APIs, query databases, or use calculators
- Creating autonomous research agents
- Orchestrating multi-step LLM workflows with conditional logic
- Prototyping LLM applications quickly with pre-built components

## When NOT to Use LangChain

- Simple prompt-and-response apps (adds unnecessary complexity)
- When you need fine-grained control over every LLM call
- Production systems where minimizing dependencies matters
- When [[llama-index|LlamaIndex]]'s retrieval focus is a better fit

## Key Takeaways

1. LangChain is the most popular general-purpose framework for building LLM-powered applications.
2. It shines for agent workflows and multi-tool orchestration.
3. For retrieval-heavy applications, LlamaIndex is often a better choice.
4. In production, evaluate whether LangChain's abstractions justify its dependency overhead.

---

- Alternative to [[llama-index]] — LangChain is general orchestration; LlamaIndex is retrieval-specialized
- Related to [[prompt-engineering]] — LangChain chains are engineered prompt sequences
- Related to [[agent-loop]] — LangChain agents implement the Perceive-Plan-Act-Observe cycle
- Related to [[retrieval-augmented-generation]] — LangChain provides RAG pipeline components
- Benchmark source: [[sources/building-llms-for-production]] — Peters & Bouchard compare LangChain and LlamaIndex
