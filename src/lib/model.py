import os


def get_model_name() -> str:
    model_name = os.getenv("MODEL_NAME")

    if not model_name:
        raise ValueError("MODEL_NAME environment variable is not set")

    print(f"Using local model: {model_name}")

    return model_name
