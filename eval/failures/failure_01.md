# Failure Analysis 01: Multi-Column Overlap

## Source Document Text
```
Vendor: OfficeMax
Item     Qty     Price    Total
Product A 2       10.00   20.00
Product B 1       5.00    5.00
Disc -2.00 Subtotal 23.00
```

## Expected JSON
```json
{
  "vendor": "OfficeMax",
  "invoice_number": "UNKNOWN",
  "date": "2024-03-26",
  "subtotal": 23.00,
  "total": 23.00,
  "line_items": [
    {"description": "Product A", "quantity": 2, "unit_price": 10.00},
    {"description": "Product B", "quantity": 1, "unit_price": 5.00},
    {"description": "Discount", "quantity": 1, "unit_price": -2.00}
  ]
}
```

## Model's Actual Response
```json
{
  "vendor": "OfficeMax",
  "invoice_number": null,
  "subtotal": 25.00,
  "total": 25.00,
  "line_items": [
    {"description": "Product A", "quantity": 2, "unit_price": 10.00},
    {"description": "Product B", "quantity": 1, "unit_price": 5.00}
  ]
}
```

## Failure Analysis
- **What went wrong:** The model failed to extract the negative 'Discount' item and incorrectly calculated the subtotal by ignoring the discount row.
- **Why it likely failed:** Negative values and non-standard row labels (e.g., 'Disc') are underrepresented in the current training set of 80 examples.
- **Proposed Data Fix:** Add 10-15 examples from the SROIE dataset specifically featuring discounts, tax exemptions, and line-item credits to the JSONL dataset.
