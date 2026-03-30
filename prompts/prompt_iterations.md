# Prompt Engineering Iterations

This document logs the development of extraction prompts for the baseline model (Llama-3.2-3B-Instruct).

## Prompt v1: Basic Instruction
```text
Extract the vendor, invoice date, number, total, and line items from this text. Return JSON.
[TEXT]
```
- **Result:** Frequently outputs Markdown fences and conversational prose. Parse success: ~25%.

## Prompt v2: Format Constraint
```text
Extract invoice details. You must output ONLY valid JSON using the following keys: vendor, invoice_number, date, total, line_items. No markdown, no prose.
[TEXT]
```
- **Result:** Improved but still occasionally wraps in code fences when the text is long. Parse success: ~50%.

## Prompt v3: Few-Shot (Best Prompt)
```text
Task: Extract structured data from business documents.
Constraints: Output ONLY a single JSON object. Do not include markdown triple backticks. Do not explain.

Example Input:
Vendor: ABC Inc
Total: 50.00
Date: 01/01/2024

Example Output:
{"vendor": "ABC Inc", "total": 50.00, "date": "2024-01-01", "currency": "USD"}

Input:
[TEXT]

Output:
```
- **Result:** Most reliable prompting method. Still fails on complex POs where the model defaults to pre-trained behavior. Parse success: 65-70%.
