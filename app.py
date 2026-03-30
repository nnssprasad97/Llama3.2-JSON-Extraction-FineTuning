import gradio as gr
import pandas as pd
import markdown

def load_md(path):
    with open(path, 'r') as f:
        return f.read()

def load_csv(path):
    return pd.read_csv(path)

with gr.Blocks(title="Structured Output Extraction Dashboard") as demo:
    gr.Markdown("# Llama 3.2 JSON Extraction Fine-Tuning Results")
    
    with gr.Tab("Project Report"):
        gr.Markdown(load_md("report.md"))
        
    with gr.Tab("Evaluation Comparison"):
        gr.Markdown(load_md("eval/before_vs_after.md"))
        
    with gr.Tab("Baseline Scores"):
        gr.Dataframe(load_csv("eval/baseline_scores.csv"))
        
    with gr.Tab("Fine-Tuned Scores"):
        gr.Dataframe(load_csv("eval/finetuned_scores.csv"))
        
    with gr.Tab("Training Config"):
        gr.Markdown(load_md("training_config.md"))
        gr.Image("screenshots/training_config.png")
        gr.Image("screenshots/loss_curve.png")
        
    with gr.Tab("Failure Analysis"):
        with gr.Row():
            for i in range(1, 6):
                with gr.Tab(f"Failure {i:02d}"):
                    gr.Markdown(load_md(f"eval/failures/failure_{i:02d}.md"))

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        max_threads=1
    )
