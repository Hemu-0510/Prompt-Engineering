import streamlit as st
from llm import generate_response
from prompt_template import build_prompt

st.set_page_config(
    page_title="Prompt Engineering",
    page_icon="💡",
    layout="centered"
)

st.title("Prompt Engineering")
st.write("Explore different prompt engineering techniques using AI.")

technique = st.selectbox(
    "Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)

user_input = st.text_area(
    "Enter your task or question",
    placeholder="Example: Explain Artificial Intelligence"
)

if st.button("Generate Response"):
    if user_input.strip():

        prompt = build_prompt(technique, user_input)

        with st.spinner("Generating response..."):
            try:
                response = generate_response(prompt)

                st.subheader("Generated Prompt")
                st.code(prompt)

                st.subheader("AI Response")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a task or question.")

