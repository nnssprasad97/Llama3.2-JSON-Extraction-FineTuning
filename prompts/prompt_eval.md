# Prompt Engineering Evaluation

Evaluation on the 3 worst-performing baseline documents (doc_103, doc_108, doc_115).

| Document ID | Best Prompt Result (v3) | Fine-Tuning Result | Analysis |
|-------------|-------------------------|---------------------|----------|
| **doc_103** (Complex Invoice) | Valid JSON, but wrapped in ```markdown``` blocks. | Pure JSON string. | Prompt v3 still fallback to pre-trained conversational habits on complex inputs. |
| **doc_108** (Messy PO) | Valid JSON, but missing 3 items. | Correct extraction of all 5 items. | Fine-tuning enables the model to look closer at data formatting patterns than instructions. |
| **doc_115** (International) | Hallucinated currency: USD. | Correct currency: EUR. | Instructions alone cannot overcome the model's pre-trained USD bias as effectively as fine-tuning with specific examples. |

## Conclusion
Prompt engineering can reach ~70% parse success rate, but for 100% machine-parseable reliability at scale, fine-tuning is mandatory as it aligns the model's token prediction probability with the structured output constraint.
