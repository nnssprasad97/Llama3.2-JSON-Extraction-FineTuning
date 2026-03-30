# Invoice JSON Schema

This document defines the structured output format for extracted invoice data. All training and evaluation examples must conform to this schema exactly.

## Schema Definition

| Key              | Data Type         | Description                                                      |
|------------------|-------------------|------------------------------------------------------------------|
| `vendor`         | `string`          | This field contains the legal name of the entity providing the goods or services and is required in all responses. |
| `invoice_number` | `string`          | This field captures the unique alphanumeric identifier for the invoice and is required for machine-parseable tracking. |
| `date`           | `string`          | This field specifies the date of invoice issuance in YYYY-MM-DD format and is required for accounting chronologies. |
| `due_date`       | `string` / `null` | This field contains the payment deadline in YYYY-MM-DD format; if the document does not specify a due date, it should be set to null. |
| `currency`       | `string`          | This field captures the 3-letter ISO 4217 code (e.g., USD, EUR) for the invoice amount and is a mandatory requirement. |
| `subtotal`       | `float`           | This float field represents the total cost of all line items before tax and is required for auditing. |
| `tax`            | `float` / `null`  | This float field captures the total tax amount applied; if no tax is listed on the invoice, it should be set to null. |
| `total`          | `float`           | This float field represents the final amount payable including all taxes and is required for financial reconciliation. |
| `line_items`     | `array`           | This array contains a list of individual items or services purchased and must be included even if the list is empty. |

### `line_items` Object

| Key            | Data Type | Description                                                      |
|----------------|-----------|------------------------------------------------------------------|
| `description`  | `string`  | This field provides a brief text description of the specific product or service rendered. |
| `quantity`     | `integer` | This integer field indicates the number of units of the specific line item purchased. |
| `unit_price`   | `float`   | This float field specifies the cost per single unit of the line item described. |

## Example Output

```json
{
  "vendor": "Acme Corp",
  "invoice_number": "INV-2024-001",
  "date": "2024-03-26",
  "due_date": "2024-04-26",
  "currency": "USD",
  "subtotal": 100.00,
  "tax": 8.00,
  "total": 108.00,
  "line_items": [
    {
      "description": "Widget A",
      "quantity": 2,
      "unit_price": 50.00
    }
  ]
}
```
