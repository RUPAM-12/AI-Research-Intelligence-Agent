import ollama

MODEL = "qwen3:4b"   # change to llama3 if you installed that

def ask_llm(prompt, memory=None):

    messages = []

    if memory:
        messages.extend(memory.get())

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    return response["message"]["content"]
