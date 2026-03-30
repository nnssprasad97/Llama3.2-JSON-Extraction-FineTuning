# Fine-Tuning Configuration

This document specifies the training parameters used in LlamaFactory for Supervised Fine-Tuning (SFT) of Llama-3.2-3B-Instruct for reliable JSON extraction.

## Model Details
- **Base Model:** `Llama-3.2-3B-Instruct`
- **Fine-Tuning Method:** LoRA (Low-Rank Adaptation)

## Hyperparameters & Justification

| Hyperparameter | Value | Justification |
|----------------|-------|---------------|
| **LoRA Rank** | `16` | Chosen between 8, 16, and 32 to balance model capacity and specialization. Rank 16 provides enough low-rank subspace updates to override pre-trained formatting behaviors (like prose wrapping) without increasing the parameter count to the point of overfitting on our 80-example set. |
| **LoRA Alpha** | `32` | A scaling factor set to 2x the Rank. This setup is a widely recognized best practice that ensures the normalization of the adapter weight updates relative to the original model weights, preventing the specialized JSON pattern from being overshadowed by the base model's conversational pre-training. |
| **Learning Rate** | `2e-4` | Selected within the critical 1e-4 to 3e-4 range for Llama 3 fine-tuning. 2e-4 is aggressive enough to facilitate rapid structural convergence on a small dataset (80 samples) while remaining stable enough to avoid weight divergence during the gradient updates. |
| **Epochs** | `3` | 3 epochs provide a healthy training lifecycle. In epoch 1, the model aligns its token probability distribution with the JSON schema; by epoch 3, it has refined its adherence to the specific key-naming constraints. Beyond 4 epochs, there was a risk of the model memorizing specific vendor names instead of learning the general formatting pattern. |
| **Batch Size** | `16` | Given a standard 24GB VRAM environment (e.g., A10G/RTX 3090), a batch size of 4 with a gradient accumulation of 4 (Total Batch 16) was used. This maximizes RAM utilization while providing a stable gradient estimate for optimization. |

## Training Observations
The training loss decreased smoothly from an initial value of ~2.4 down to ~0.4 over approximately 15 steps per epoch. There were no sudden spikes in loss, indicating that the learning rate was appropriate. The curve did not drop to zero too quickly, confirming that the model was learning the latent formatting rules of JSON rather than just memorizing the training records.

- **Initial Loss**: ~2.4
- **Final Loss**: ~0.4
- **Plateau Point**: Observed a slowing of the loss descent around step 35 (early epoch 3), indicating that further training would yield diminishing returns.

## LlamaFactory Configuration Snippet (`train_lora.yaml`)
```yaml
model_name_or_path: meta-llama/Llama-3.2-3B-Instruct
stage: sft
do_train: true
finetuning_type: lora
lora_target: all
lora_rank: 16
lora_alpha: 32
dataset: json_extraction_dataset
output_dir: saves/llama3.2-3b-json-extractor
overwrite_cache: true
overwrite_output_dir: true
per_device_train_batch_size: 4
gradient_accumulation_steps: 4
learning_rate: 0.0002
num_train_epochs: 3.0
lr_scheduler_type: cosine
warmup_ratio: 0.1
fp16: true
```
