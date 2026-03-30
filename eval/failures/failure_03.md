# Failure Analysis 03: Date Format Ambiguity

## Source Document Text
```
Invoice Date: 01/02/2024
Due Date: 02/03/2024
```

## Expected JSON (for US format)
```json
{
  "date": "2024-01-02",
  "due_date": "2024-02-03"
}
```

## Model's Actual Response (assumed DD/MM)
```json
{
  "date": "2024-02-01",
  "due_date": "2024-03-02"
}
```

## Failure Analysis
- **What went wrong:** The model used DD-MM-YYYY instead of MM-DD-YYYY for a document likely sourced from a region with the opposite convention.
- **Why it likely failed:** Ambiguous date formats (e.g., 01/02) are difficult for the model without explicit country context.
- **Proposed Data Fix:** Add 5-10 examples that include country or address information (e.g. 'Los Angeles, CA' vs 'London, UK') to help the model learn the regional context for date formats.
