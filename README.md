# Hugging Face Model Testing

Testing harness for evaluating different models across various asset types (images, audio, video, text).

## Usage

Required environment variables:

- `MODEL_NAME` - Hugging Face model ID (required)
- `PROMPT_FILE` - Prompt filename in `prompts/` (optional, defaults to `prompt.md`)

Copy the example `.env` file, then change/fill the values.

```bash
cp .env.example .env
```

### Image Generation

```bash
uv run src/z-image-turbo.py
```
