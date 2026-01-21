from transformers import pipeline

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

def generate_answer(prompt):
    return llm(prompt)[0]["generated_text"]
