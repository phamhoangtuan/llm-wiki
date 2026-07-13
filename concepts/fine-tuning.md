---
title: "Fine-Tuning"
type: concept
tags: [llm, ml, training, lora, domain-adaptation, production]
created: 2026-07-11
updated: 2026-07-13
sources: [building-llms-for-production, hands-on-large-language-models]
aliases: [model-fine-tuning, instruction-tuning, supervised-fine-tuning]
---

## Summary

**Fine-Tuning** is the process of adapting a pre-trained general-purpose Large Language Model to a specific task or domain by continuing training on a smaller, targeted dataset. It embeds domain expertise, stylistic preferences, and specialized reasoning patterns directly into the model's weights, producing outputs that prompt engineering and RAG alone cannot achieve.

## When to Fine-Tune

Fine-tuning is warranted when:

- Prompt engineering and RAG are insufficient — the model needs deep domain fluency
- Consistent stylistic or behavioral output is required across many queries
- Latency constraints prevent long RAG prompts or multi-step retrieval
- Proprietary reasoning patterns must be learned (e.g., legal clause extraction, medical diagnosis workflows)

## Techniques

### Full Fine-Tuning

- Update all model parameters on domain-specific data
- **Pros:** Maximum adaptation capacity
- **Cons:** Requires large GPU clusters, risks catastrophic forgetting of general knowledge

### Parameter-Efficient Fine-Tuning (PEFT)

| Method | Mechanism | Cost |
|--------|-----------|------|
| **LoRA** | Low-Rank Adaptation — injects small trainable rank-decomposition matrices into each layer | ~10,000× fewer parameters than full fine-tuning |
| **QLoRA** | Quantized LoRA — runs LoRA on 4-bit quantized base models | Trainable on a single consumer GPU (e.g., RTX 4090) |
| **Adapter Layers** | Add small bottleneck layers; freeze base model | Minimal overhead at inference |
| **Prefix Tuning** | Learnable continuous vectors prepended to input | < 0.1% of model parameters |

All PEFT methods share a key advantage: the frozen base model stays on disk/VRAM while only the tiny adapters are swapped for different tasks. One base model can serve dozens of domains by switching adapters at runtime.

## Instruction Tuning

A special case of fine-tuning where the model is trained on `(instruction, input, output)` triples to improve following of natural language commands. Forms the basis of "Instruct" model variants (e.g., Llama-2-Chat, GPT-3.5-turbo).

## Fine-Tuning vs RAG vs Prompt Engineering

| Method | Knowledge Depth | Cost | Speed | Best For |
|--------|--------------|------|-------|----------|
| Prompt Engineering | Shallow | Zero | Instant | Format, tone, simple constraints |
| RAG | Medium (document-bound) | Low | Seconds | Factual grounding, dynamic data |
| Fine-Tuning | Deep (weight-bound) | High | Fast inference | Domain expertise, style, reasoning |

## Risks

- **Catastrophic forgetting** — model may lose general knowledge if fine-tuned too aggressively
- **Overfitting** — small datasets can cause the model to memorize rather than generalize
- **Data quality dependency** — fine-tuning amplifies biases and errors present in training data
- **Infrastructure cost** — serving multiple fine-tuned model variants increases deployment complexity

## Key Takeaways

1. Fine-tuning is the deepest lever for controlling model behavior — it changes the model itself.
2. LoRA and QLoRA make fine-tuning accessible without data-center GPUs.
3. It is complementary to RAG: fine-tune for behavior, RAG for facts.
4. Data quality and evaluation rigor are more important than model size for fine-tuning success.

---

- Complements [[retrieval-augmented-generation]] — fine-tuning shapes behavior; RAG supplies facts
- Related to [[prompt-engineering]] — the three primary methods for controlling LLM output
- Related to [[lora]] — LoRA is the most practical path to fine-tuning for engineers without data-center GPUs
- Related to [[peft]] — PEFT is the umbrella of parameter-efficient techniques that make fine-tuning accessible
- Related to [[model-distillation]] — distillation can produce a smaller model that approximates a fine-tuned teacher
- Related to [[data-quality-monitoring]] — fine-tuning datasets require the same rigorous quality validation as production data
- Accelerated by [[flash-attention]] — Flash Attention speeds up fine-tuning forward/backward passes by 2–4×
- Framework sources: [[sources/building-llms-for-production]], [[sources/hands-on-large-language-models]]
