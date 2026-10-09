
import torch
from transformers import pipeline

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device=0 if torch.cuda.is_available() else -1
)

def generate_response(prompt):
    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=False,
        return_full_text=False
    )

    return result[0]["generated_text"]

