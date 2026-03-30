# Failure Analysis 02: Rare Currency Support

## Source Document Text
```
Supplier: Tokyo Logistics
PO Number: TK-999
Date: 2024-03-20
Total: ¥500,000
```

## Expected JSON
```json
{
  "buyer": "Global Corp",
  "supplier": "Tokyo Logistics",
  "po_number": "TK-999",
  "date": "2024-03-20",
  "delivery_date": null,
  "currency": "JPY",
  "total": 500000.00,
  "items": []
}
```

## Model's Actual Response
```json
{
  "buyer": "Global Corp",
  "supplier": "Tokyo Logistics",
  "po_number": "TK-999",
  "date": "2024-03-20",
  "delivery_date": null,
  "currency": "USD",
  "total": 500000.00,
  "items": []
}
```

## Failure Analysis
- **What went wrong:** The model correctly extracted the amount but hallucinated `USD` instead of `JPY`.
- **Why it likely failed:** The training set only has 5 non-USD examples. The model still biases towards the most frequent currency seen during pre-training and fine-tuning.
- **Proposed Data Fix:** Increase JPY, EUR, and GBP representation to at least 15% of the total dataset by synthesizing more international invoices.
