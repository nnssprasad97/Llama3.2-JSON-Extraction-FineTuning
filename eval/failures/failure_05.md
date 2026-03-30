# Failure Analysis 05: Missing Table Headers

## Source Document Text
```
Acme Corp
INV-03-01
2024-03-26
Widget A 10 10.00
Widget B 5 5.00
25.00
```

## Expected JSON
```json
{
  "vendor": "Acme Corp",
  "invoice_number": "INV-03-01",
  "date": "2024-03-26",
  "total": 25.00,
  "line_items": [
    {"description": "Widget A", "quantity": 10, "unit_price": 10.00},
    {"description": "Widget B", "quantity": 5, "unit_price": 5.00}
  ]
}
```

## Model's Actual Response
```json
{
  "vendor": "Acme Corp",
  "invoice_number": "INV-03-01",
  "date": "2024-03-26",
  "total": 25.00,
  "line_items": [
    {"description": "Widget A", "quantity": 10, "unit_price": 10.00},
    {"description": "Widget B", "quantity": 5, "unit_price": 5.00},
    {"description": "Unknown Item", "quantity": 1, "unit_price": 25.00}
  ]
}
```

## Failure Analysis
- **What went wrong:** The model correctly extracted all fields but incorrectly included the total as an item.
- **Why it likely failed:** The lack of table headers makes it difficult for the model to distinguish between items and totals.
- **Proposed Data Fix:** Add 5-10 examples of documents without table headers (e.g. handwritten notes or simple receipts) to help the model learn to correctly identify the total and other summary fields.
