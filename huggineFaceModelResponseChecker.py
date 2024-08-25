from huggingface_hub import InferenceClient

client = InferenceClient(model="google/flan-t5-xxl")

try:
    response = client.text_generation("Translate to French: Hello, world!", max_new_tokens=50)
    print("Model responded:", response)
except Exception as e:
    print("Error during inference:", e)