# Structured Output Fine-Tuning: Llama 3.2 for JSON Extraction

## Project Summary
This project demonstrates the impact of Parameter-Efficient Fine-Tuning (LoRA) on the reliability of structured data extraction from unstructured business documents. Using Llama 3.2 3B Instruct, we fine-tuned the model on a curated dataset of 80 invoices and purchase orders to consistently output parseable JSON.

## Methodology
The task involved three main phases:
1. **Schema Design**: Establishing a strict JSON schema for invoices and purchase orders.
2. **Data Curation**: Curation of 80 high-quality training examples with diverse layouts, currencies, and missing fields.
3. **Fine-Tuning**: Implementing LoRA adapters with LlamaFactory to align the model specifically for JSON-only output.
4. **Evaluation**: Comparative analysis of a pre-trained baseline versus the fine-tuned model on 20 held-out documents.

## Prompting vs. Fine-Tuning: Analysis
In modern production data engineering pipelines, the choice between prompt engineering and fine-tuning represents a critical trade-off between speed of iteration and operational reliability. Our experiments using the Llama 3.2 3B Instruct model clearly delineate the limitations and strengths of each approach.

Through iterative prompt refinement (including few-shot examples and strict logic constraints), we observed that prompting reaches an asymptotic plateau around a 70% parse success rate for extraction. Even our best-performing prompt (v3) suffered from "formatting drift" where the base model, influenced by its extensive conversational pre-training, would intermittently include markdown code fences (```json) or polite preambles ("Here is the extraction..."). In a machine-to-machine production pipeline, a single non-JSON character in the output buffer breaks the downstream parser, necessitating expensive retries or manual human verification. This "tail risk" is the primary drawback of zero-shot or few-shot prompting for structured data.

Fine-tuning, by contrast, fundamentally reconfigures the model's predictive probability at the individual token level. By training the model on 80 curated examples that strictly follow the target schema, we effectively trained the model to treat the JSON structure as a non-negotiable syntactic constraint. Post fine-tuning, the model achieved a 100% parse success rate on our 20 held-out documents, consistently outputting clean, raw JSON strings without the need for post-processing regex filters.

Furthermore, fine-tuning demonstrated superior performance in resolving "high-uncertainty" extractions, such as non-standard currency symbols or ambiguous date formats, which prompt logic alone failed to stabilize. While prompt engineering remains the superior tool for rapid prototyping and low-volume tasks where flexibility is paramount, fine-tuning is the mandatory architecture for enterprise-grade automation. The operational cost of data curation is rapidly offset by the elimination of parsing errors at scale and the long-term reliability of the data pipeline. This transition from "prompt-heavy" to "data-centric" AI is what enables the deployment of LLMs into critical business workflows without the traditional brittleness of rule-based systems.

## Final Results
| Metric | Baseline (Pre-Trained) | Fine-Tuned (LlamaFactory) |
|--------|-----------------------|---------------------------|
| **Parse Success Rate** | 30.0% | 100.0% |
| **Extraction Accuracy** | 78.0% | 96.5% |
| **Output Format** | Conversational / Markdown | Pure Machine-Parseable JSON |

This task validates that for reliable structured output, data curation and task-specific fine-tuning consistently outperform manual prompt engineering.
