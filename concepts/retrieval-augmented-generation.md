---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
tags: [llm, rag, vector-database, search, knowledge, production]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [rag, augmented-generation, grounded-generation]
---

## Summary

**Retrieval-Augmented Generation (RAG)** is an architecture pattern that grounds Large Language Model outputs in external, verifiable data sources. Instead of relying solely on parametric knowledge (what the model learned during training), RAG retrieves relevant documents from a knowledge base and injects them into the model's context window at inference time.

## Why RAG Matters

LLMs have two critical weaknesses that RAG directly addresses:

1. **Hallucinations** — Models generate plausible-sounding but false information.
2. **Knowledge cutoff** — Models don't know about events, documents, or data newer than their training date.

RAG solves both by tethering every generated answer to retrieved, inspectable source material.

## The RAG Pipeline

```
User Query → Retriever (Search/Vector DB) → Top-K Documents → Prompt Constructor → LLM → Grounded Answer
```

### 1. Ingestion & Indexing

- Chunk documents into passages
- Embed chunks into dense vectors (e.g., OpenAI embeddings, BGE, E5)
- Store in a vector database (e.g., Pinecone, Weaviate, Milvus, pgvector)

### 2. Retrieval

- Embed the user query into the same vector space
- Perform similarity search (ANN — Approximate Nearest Neighbors)
- Optionally apply hybrid search: combine vector similarity with keyword BM25

### 3. Re-ranking

- A secondary model re-scores retrieved passages for relevance
- Cross-encoders (e.g., BERT-based re-rankers) are more accurate but slower than bi-encoders
- Trade-off: latency vs. precision

### 4. Generation

- Inject retrieved passages into a system prompt template
- Instruct the model to answer using *only* the provided context
- Return citations or source references alongside the answer

## Key Components

| Component | Options | Role |
|-----------|---------|------|
| **Vector Database** | Pinecone, Weaviate, Milvus, Chroma, pgvector | Stores and searches embeddings |
| **Embedding Model** | OpenAI, Cohere, BGE, E5, GTE | Converts text to dense vectors |
| **Re-ranker** | Cohere Rerank, BERT cross-encoder | Improves retrieval precision |
| **Orchestrator** | LangChain, LlamaIndex, custom | Manages the full pipeline |

## Advanced Patterns

- **Self-RAG** — The model critiques its own retrieval: "Is this context sufficient?" If not, it retrieves again.
- **Corrective RAG** — Detect low-confidence retrievals and fall back to web search or alternative sources.
- **Graph RAG** — Use knowledge graphs (e.g., Neo4j) alongside vector search for structured relationship retrieval.

## When RAG Is Not Enough

RAG excels at factual grounding but struggles when:

- The task requires deep stylistic or behavioral adaptation (→ use [[fine-tuning]])
- The model needs to learn proprietary reasoning patterns not present in documents
- Latency constraints prevent retrieval overhead (→ consider caching or distilled models)

## Key Takeaways

1. RAG is the most effective defense against hallucinations in production LLM systems.
2. Retrieval quality matters more than generation quality — garbage in, garbage out.
3. Hybrid search (vector + keyword) + re-ranking yields the best retrieval precision.
4. RAG and fine-tuning are complementary: RAG for facts, fine-tuning for behavior.

---

- Complements [[fine-tuning]] — RAG grounds facts; fine-tuning shapes behavior and domain expertise
- Complements [[prompt-engineering]] — retrieved content is fed into carefully engineered prompt templates
- Related to [[llm-evaluation-metrics]] — Hit Rate measures retrieval quality; Faithfulness measures grounded generation quality
- Related to [[data-ingestion]] — RAG pipelines are a specialized form of data ingestion (document chunking, embedding, indexing)
- Related to [[apache-kafka]] — real-time document updates can stream through Kafka into vector indexes
- Framework source: [[sources/building-llms-for-production]] — RAG as one of four pillars of production LLM stack
