# Data Curation Log

| example_id | document_type | source | kept_or_rejected | reason | schema_issues_found |
|------------|---------------|--------|------------------|--------|---------------------|
| 001 | Invoice | CORD v2 | Kept | Clear vendor name and date in YYYY-MM-DD format. Matched schema exactly. | None |
| 002 | Invoice | CORD v2 | Kept | Includes due_date, testing null-safety for optional fields. | None |
| 003 | Invoice | CORD v2 | Kept | Diverse layout featuring multi-line table headers. | None |
| 004 | Invoice | CORD v2 | Kept | Non-USD currency (EUR) example. | None |
| 005 | Invoice | CORD v2 | Kept | Complex line items with varying quantities for stress testing. | None |
| 006 | Invoice | CORD v2 | Kept | Manual review confirmed numeric subtotal matches sum of line items. | None |
| 007 | Invoice | CORD v2 | Kept | Missing optional tax field; model must learn to output null. | None |
| 008 | Invoice | CORD v2 | Kept | Missing due_date field; verifies null handling for temporal keys. | None |
| 009 | Invoice | CORD v2 | Kept | Large line_items array (5 items) to verify list extraction. | None |
| 010 | Invoice | CORD v2 | Kept | Non-standard layout with vendor details in footer. | None |
| 011 | Invoice | CORD v2 | Kept | GBP Currency example with varied symbol placement. | None |
| 012 | Invoice | CORD v2 | Kept | JPY example with high numeric values (no decimals). | None |
| 013 | Invoice | CORD v2 | Kept | Verified YYYY-MM-DD date format conversion from MM/DD/YY. | None |
| 014 | Invoice | CORD v2 | Kept | All optional fields present; testing "best case" scenario. | None |
| 015 | Invoice | CORD v2 | Kept | Minimal invoice with single line item but complex vendor name. | None |
| 016 | Invoice | CORD v2 | Kept | Invoice from regional supplier with INR currency. | None |
| 017 | Invoice | CORD v2 | Kept | Multiple tax rows collapsed into single schema field correctly. | None |
| 018 | Invoice | CORD v2 | Kept | Clear OCR text with no ambiguity in line item descriptions. | None |
| 019 | Invoice | CORD v2 | Kept | Discount listed as absolute value; verified subtotal logic. | None |
| 020 | Invoice | CORD v2 | Kept | Long vendor name spanning two lines on document. | None |
| 021 | Invoice | CORD v2 | Kept | Validated that floats remain floats and are not quoted as strings. | None |
| 022 | Invoice | CORD v2 | Kept | Verified invoice_number with special characters (e.g. #, -, /). | None |
| 023 | Invoice | CORD v2 | Kept | Handled date with text month (e.g. March 26) into YYYY-MM-DD. | None |
| 024 | Invoice | CORD v2 | Kept | Verified currency ISO codes match ground truth document. | None |
| 025 | Invoice | CORD v2 | Kept | Checked that items array is never null, even if empty (req. schema). | None |
| 026-050 | Invoice | CORD v2 | Kept | Verified schema compliance for remaining 25 invoice samples. | None |
| 051 | Purchase Order | DocumentIE | Kept | Standard PO format with buyer and supplier clearly separated. | None |
| 052 | Purchase Order | DocumentIE | Kept | Delivery date null; testing PO specific null handling. | None |
| 053 | Purchase Order | DocumentIE | Kept | Multi-item purchase order (4 assets) for bulk order testing. | None |
| 054 | Purchase Order | DocumentIE | Kept | Currency JPY example for PO extraction. | None |
| 055 | Purchase Order | DocumentIE | Kept | Supplier name with international characters handled. | None |
| 056 | Purchase Order | DocumentIE | Kept | PO number with non-numeric prefix (PO-ABC-123). | None |
| 057 | Purchase Order | DocumentIE | Kept | Total field includes shipping fees as part of items or total. | None |
| 058 | Purchase Order | DocumentIE | Kept | Checked for consistent date formats across all 30 POs. | None |
| 059 | Purchase Order | DocumentIE | Kept | Buyer address ignored; focused strictly on required keys. | None |
| 060 | Purchase Order | DocumentIE | Kept | Supplier contact info ignored; verified schema mapping. | None |
| 061-080 | Purchase Order | DocumentIE | Kept | Batch validation of structural integrity and key naming. | None |
| 081 | Invoice | CORD v2 | Rejected | Illegible text in date field; source was low resolution. | Date format mismatch |
| 082 | Invoice | CORD v2 | Rejected | Line items missing unit price; incomplete data for schema. | Missing required key |
| 083 | PO | DocumentIE | Rejected | Ambiguous buyer/supplier swap. | Logic error |
