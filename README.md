# Prompt Engineering

## Project Overview
This project is a Streamlit web application that compares six prompt engineering techniques using a Hugging Face language model.

## Prompting Techniques
- **Zero-shot Prompting:** Generates an answer without examples.
- **One-shot Prompting:** Uses one example to guide the answer.
- **Few-shot Prompting:** Uses multiple examples to guide the answer.
- **Chain of Thought (CoT):** Encourages a structured explanation.
- **Manual Chain of Thought:** Guides the answer through predefined steps.
- **Tree of Thoughts (ToT):** Explores different approaches before selecting a suitable one.

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct
- PyTorch

## Project Files
- `app.py` – Creates the Streamlit user interface and compares responses.
- `llm.py` – Loads the Hugging Face model and generates responses.
- `prompt_template.py` – Defines the six prompting techniques.

## Installation

Install the required libraries:

```bash
python -m pip install streamlit transformers torch
```



## How It Works
1. Enter a task in the application.
2. The application creates a prompt for each technique.
3. The Hugging Face model generates six responses.
4. Compare the responses based on clarity, relevance, and usefulness.

## Objective
To understand how different prompt engineering techniques influence AI-generated responses and help users select suitable prompting approaches.

## Conclusion
This project demonstrates the use of six prompt engineering techniques in a single application and helps compare their generated responses.
