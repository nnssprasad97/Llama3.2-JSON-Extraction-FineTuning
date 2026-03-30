# Failure Analysis 04: OCR Noise and Illegibility

## Source Document Text
```
V?nd?r: Acme Corp
Invo?ce: INV-03-24
D?te: 2024-03-26
```

## Expected JSON
```json
{
  "vendor": "Acme Corp",
  "invoice_number": "INV-03-24",
  "date": "2024-03-26"
}
```

## Model's Actual Response
```json
{
  "vendor": "Acme Corp",
  "invoice_number": "INV-03-24",
  "date": "2024-02-26"
}
```

## Failure Analysis
- **What went wrong:** The model correctly extracted the vendor name but incorrectly extracted the date (hallucinated 26th Feb instead of 26th March).
- **Why it likely failed:** The OCR noise in the source document leads to higher uncertainty in the extraction, making the model prone to hallucination.
- **Proposed Data Fix:** Add 10-15 examples of noisy OCR text (simulated or real-world) in the training data to help the model learn to handle messy text and avoid hallucination.
