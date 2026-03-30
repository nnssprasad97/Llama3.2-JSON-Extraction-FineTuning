# Baseline Evaluation Summary

- **Total Documents:** 20
- **Parse Success Rate:** 10.0%

## Error Breakdown Analysis
The baseline Llama 3.2 3B Instruct model struggles significantly with reliable zero-shot structured extraction. While the model correctly identifies the semantic entities within the text, its formatting is highly inconsistent:

1. **Conversational Preamble (8/20):** The model often introduces the output with phrases like "Certainly! Here is the extracted information...", which instantly breaks standard JSON parsers.
2. **Markdown Code Fences (14/20):** The model defaults to wrapping the JSON object in ```json code blocks, requiring regex stripping in a production pipeline.
3. **Missing or Inconsistent Keys (6/20):** Key schema adherence is poor, with the model frequently dropping required `null` assignments or hallucinating alternative key names (e.g. `total_amount` instead of `total`).

Overall, a 10% parse success rate indicates the baseline model cannot be deployed in an automated ETL pipeline without extensive middleware parsing logic.
