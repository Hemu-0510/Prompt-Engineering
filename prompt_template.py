
def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Act as a knowledgeable assistant.
Respond to the user's request clearly and accurately.

Request: {task}

Answer:
""".strip()

    elif technique == "One-shot":
        return f"""
Follow the response pattern in the example.

Example:
Question: What is an algorithm?
Answer: An algorithm is a sequence of steps used to solve a problem.

Now answer:
{task}

Answer:
""".strip()

    elif technique == "Few-shot":
        return f"""
Use these examples as a guide.

Question: What is a variable?
Answer: A variable stores a value in a program.

Question: What is a function?
Answer: A function is a reusable block of code.

Question: What is a loop?
Answer: A loop repeats a set of instructions.

Now respond to:
{task}

Answer:
""".strip()

    elif technique == "CoT":
        return f"""
Analyze the task carefully.
Provide a short explanation of the main steps
without revealing private internal reasoning.

Task: {task}

Final Answer:
""".strip()

    elif technique == "Manual CoT":
        return f"""
Use this guided solution format.

1. Identify the problem.
2. Find the relevant information.
3. Choose a suitable method.
4. Check the result.
5. Present the conclusion.

Task: {task}

Conclusion:
""".strip()

    elif technique == "ToT":
        return f"""
Explore up to three possible approaches to the task.
Briefly compare their strengths and limitations.
Choose the most suitable approach and explain why.

Task: {task}

Best Approach:
""".strip()

    else:
        raise ValueError("Unknown prompting technique")

