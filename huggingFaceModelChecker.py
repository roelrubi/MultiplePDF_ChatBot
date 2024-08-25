from huggingface_hub import HfApi

api = HfApi()
model_id = "google/flan-t5-xxl"

try:
    model_info = api.model_info(model_id)
    print(f"Model {model_id} is available.")
    print(f"Last modified: {model_info.lastModified}")
    print(f"Tags: {model_info.tags}")
except Exception as e:
    print(f"Error checking model: {e}")