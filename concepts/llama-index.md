---
title: "LlamaIndex"
type: concept
tags: [llm, rag, indexing, retrieval, data]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [gpt-index]
---

## Summary

**LlamaIndex** (formerly GPT Index) is an open-source data framework for connecting LLMs with external data sources. Unlike [[langchain|LangChain]] which is a general orchestration framework, LlamaIndex specializes in **indexing, retrieval, and query optimization** — making it the preferred choice for building sophisticated [[retrieval-augmented-generation|RAG]] systems over private or domain-specific data.

## Core Capabilities

| Feature | Description |
|---------|-------------|
| **Data Ingestion** | Load 100+ data sources: PDFs, SQL databases, Notion, Slack, APIs |
| **Indexing** | Multiple index types: vector, tree, keyword, knowledge graph |
| **Query Routing** | Automatically choose the best index for a given query |
| **Response Synthesis** | Combine retrieved nodes into coherent answers with citations |
| **Evaluation** | Built-in RAG evaluation metrics (relevance, faithfulness) |

## Index Types

| Index | Best For |
|-------|----------|
| **Vector Index** | Semantic similarity search over documents |
| **Tree Index** | Hierarchical summarization (top-down querying) |
| **Keyword Index** | Exact-match and BM25 retrieval |
| **Knowledge Graph Index** | Structured relationship queries |
| **Composable** | Combine multiple indices for complex use cases |

## LlamaIndex vs LangChain

| Aspect | LlamaIndex | [[langchain|LangChain]] |
|--------|-----------|------------------------|
| Primary focus | Data retrieval and indexing | General LLM workflow orchestration |
| RAG depth | Deep — advanced chunking, re-ranking, query transformation | Surface — basic document loaders and vector stores |
| Agent support | Limited | Extensive |
| When to use | Enterprise RAG, complex document search | Multi-tool agents, general LLM apps |

## When to Use LlamaIndex

- Building RAG over large, heterogeneous document collections
- Need advanced retrieval strategies (multi-step query transformation, re-ranking)
- Querying structured + unstructured data together (SQL tables + PDFs)
- Want built-in evaluation and observability for RAG quality

## Key Takeaways

1. LlamaIndex is the most capable open-source framework for production RAG systems.
2. Its indexing abstractions handle the hard parts of document ingestion, chunking, and retrieval.
3. Use LlamaIndex for retrieval-heavy apps; use LangChain for agent-heavy, tool-orchestration apps.

---

- Alternative to [[langchain]] — LlamaIndex is retrieval-specialized; LangChain is general-purpose
- Core enabler of [[retrieval-augmented-generation]] — LlamaIndex provides the indexing and retrieval layer
- Related to [[prompt-engineering]] — retrieved content is injected into prompts via LlamaIndex's response synthesis
- Related to [[llm-evaluation-metrics]] — LlamaIndex includes built-in RAG evaluation tools
- Benchmark source: [[sources/building-llms-for-production]] — Peters & Bouchard compare LlamaIndex and LangChain
