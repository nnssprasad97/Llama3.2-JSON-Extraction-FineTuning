# Purchase Order JSON Schema

This document defines the structured output format for extracted purchase order data.

## Schema Definition

| Key             | Data Type         | Description                                                      |
|-----------------|-------------------|------------------------------------------------------------------|
| `buyer`         | `string`          | This field captures the legal name of the entity issuing the purchase order and is mandatory. |
| `supplier`      | `string`          | This field contains the legal name of the entity providing the requested goods or services and is required. |
| `po_number`     | `string`          | This field is used for recording the unique identifier assigned to the purchase order and is required. |
| `date`          | `string`          | This field specifies the date of PO issuance in YYYY-MM-DD format and is required as a primary key. |
| `delivery_date` | `string` / `null` | This field contains the expected delivery date in YYYY-MM-DD format; if missing from the PO, it should be set to null. |
| `currency`      | `string`          | This field captures the 3-letter ISO 4217 code for the purchase order value and is a mandatory requirement. |
| `total`         | `float`           | This float field represents the final amount agreed upon for the purchase order and is required for budgeting. |
| `items`         | `array`           | This array contains a list of individual assets or services being ordered and must be included in all responses. |

### `items` Object

| Key          | Data Type | Description                              |
|--------------|-----------|------------------------------------------|
| `item_name`  | `string`  | This string field provides a text description of the specific asset or service being purchased. |
| `quantity`   | `integer` | This integer field indicates the number of units being requested for the specific item. |
| `unit_price` | `float`   | This float field specifies the cost per unit of the item as quoted on the purchase order. |

## Example Output

```json
{
  "buyer": "Global Tech Solutions",
  "supplier": "Supply Chain Pro Inc.",
  "po_number": "PO-12345-X",
  "date": "2024-03-20",
  "delivery_date": "2024-04-15",
  "currency": "USD",
  "total": 5000.00,
  "items": [
    {
      "item_name": "High-End Server Router",
      "quantity": 2,
      "unit_price": 2500.00
    }
  ]
}
```
