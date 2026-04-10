import os
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent.parent


def read_prompt(filename: str = "prompt.md") -> str:
    relative_path = "prompts/" + os.getenv("PROMPT_FILE", filename)
    path = PROMPTS_DIR / relative_path

    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")

    content = path.read_text().strip()

    if not content:
        raise ValueError(f"Prompt file is empty: {path}")

    print(f"Using prompt file: {relative_path}")

    return content
