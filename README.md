# Structured Output Fine-Tuning Task (Llama 3.2 3B)

**Description:** Fine-tuning Llama 3.2 3B Instruct using Parameter-Efficient Fine-Tuning (LoRA) for highly reliable JSON extraction from commercial documents (invoices, POs).
**Topics:** `llm`, `fine-tuning`, `llama`, `json-extraction`, `lora`
**Model Link:** [HuggingFace - Llama-3.2-3B-Instruct (base)](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

This repository contains the complete workflow for fine-tuning Llama 3.2 for reliable JSON extraction from business documents.

## Project Structure
- `schema/`: JSON schema definitions for invoices and POs.
- `data/`: Curated JSONL training data (80 examples) and curation log.
- `eval/`: Baseline and post-fine-tuning evaluation metrics and side-by-side comparison.
- `screenshots/`: Training configuration and loss curve.
- `prompts/`: Logging of prompt engineering iterations.
- `report.md`: Final analysis report.

## How to View Results (Docker)
The evaluator can view all findings through a consolidated dashboard:

1.  Build and start the container:
    ```bash
    docker-compose up --build
    ```
2.  Open your browser to: `http://localhost:7861`

The dashboard allows you to browse the evaluation data, training parameters, and final project report.
