from pathlib import Path
import os

PROMPTS_DIR = Path(__file__).resolve().parent.parent.parent / "prompts"


def read_prompt(filename: str = "prompt.md") -> str:
    path = PROMPTS_DIR / os.getenv("PROMPT_FILE", filename)

    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")

    content = path.read_text().strip()

    if not content:
        raise ValueError(f"Prompt file is empty: {path}")

    return content
