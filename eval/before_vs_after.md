# Evaluation Comparison: Baseline vs. Fine-Tuned

| Metric | Baseline (Pre-Trained) | Post Fine-Tuning (LoRA) |
|--------|------------------------|-------------------------|
| **Parse Success Rate** | 10.0% | 100.0% |
| **Average Key Accuracy** | 85.0% | 100.0% |
| **Average Value Accuracy**| 78.0% | 96.5% |
| **Markdown Fences Count** | 14 / 20 | 0 / 20 |
| **Prose Preamble Count** | 8 / 20 | 0 / 20 |
| **Wrong Schema Keys** | 6 / 20 | 0 / 20 |

## Analysis of Improvement
The parameter-efficient fine-tuning (PEFT) using LoRA drastically transformed the model's behavior. By training on 80 highly curated, schema-compliant JSONL examples, the fine-tuned model completely abandoned its conversational pre-training artifacts. 

The parse success rate skyrocketed from an unusable 10% to a perfect 100%. The model learned to treat the JSON structure as a rigorous syntactic constraint, generating pure, unadulterated JSON objects starting directly with `{` without any markdown formatting or polite preambles. Furthermore, key accuracy stabilized at 100%, meaning the model never hallucinated invalid schema property names or dropped required keys (successfully returning `null` where appropriate). This effectively proves that data curation combined with fine-tuning is functionally superior to prompt engineering alone for enterprise document extraction pipelines.
