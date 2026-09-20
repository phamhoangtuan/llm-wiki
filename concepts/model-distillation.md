---
title: "Model Distillation"
type: concept
tags: [llm, ml, optimization, compression, teacher-student, production]
created: 2026-07-11
updated: 2026-07-11
sources: [building-llms-for-production]
aliases: [knowledge-distillation, distillation]
---

## Summary

**Model Distillation** is a compression technique where a smaller "student" model is trained to replicate the behavior of a larger, more capable "teacher" model. The student learns from the teacher's output distributions (soft targets) rather than from raw ground-truth labels, enabling it to capture nuanced reasoning patterns with far fewer parameters.

## Why Distill

| Problem | Distillation Solution |
|---------|----------------------|
| Large models are too slow for real-time APIs | Student model runs 10× faster with ~95% quality |
| High serving costs at scale | Smaller model fits on cheaper hardware |
| Edge/mobile deployment | Student can run on-device (phones, IoT) |
| Multiple specialized variants | One teacher, many lightweight students |

## The Distillation Process

```
Teacher Model (large, frozen) → Generates soft predictions on training data
                                      ↓
Student Model (small, trainable) → Trained to match teacher's probability distribution
                                      ↓
Distilled Model → Deployed for fast, cheap inference
```

### Soft Targets vs Hard Labels

- **Hard labels:** `[0, 1, 0]` — one-hot ground truth
- **Soft targets:** `[0.1, 0.8, 0.1]` — teacher's probability distribution

Soft targets encode *relational knowledge* between classes — the teacher's confidence that "cat" is somewhat like "dog" helps the student learn richer representations.

## Distillation Variants

| Variant | Description |
|---------|-------------|
| **Logit Distillation** | Student mimics teacher's output logits (class probabilities) |
| **Feature Distillation** | Student mimics intermediate layer representations (hidden states) |
| **Chain-of-Thought Distillation** | Student learns to reproduce teacher's reasoning steps, not just answers |
| **Self-Distillation** | Model distills knowledge from its own ensemble or earlier checkpoints |

## Trade-offs

| Aspect | Teacher | Student |
|--------|---------|---------|
| Size | Large (e.g., 70B parameters) | Small (e.g., 7B parameters) |
| Quality | Baseline | ~90–95% of teacher |
| Latency | High | Low |
| Cost | Expensive to serve | Cheap to serve |
| Training cost | High (pre-training) | Medium (distillation) |

## Key Takeaways

1. Distillation is the primary method for deploying large-model capabilities at small-model cost.
2. Soft targets encode richer information than hard labels, enabling better student learning.
3. Chain-of-Thought distillation is emerging as critical for reasoning tasks.
4. Distillation is complementary to quantization and pruning — often used together.

---

- Complements [[model-quantization]] — quantization shrinks precision; distillation shrinks architecture
- Complements [[model-pruning]] — pruning removes weights; distillation trains a smaller model from scratch
- Related to [[fine-tuning]] — a fine-tuned teacher can be distilled into a specialized student
- Related to [[apache-flink]] — model serving layers may use distilled models for low-latency inference
- Framework source: [[sources/building-llms-for-production]] — distillation as a deployment optimization pillar
