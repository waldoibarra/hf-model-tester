# Hugging Face Model Testing

Testing harness for evaluating different models across various asset types (currently images only).

## Pre-requesites

Install:

- [just](https://github.com/casey/just)
- [pyenv](https://github.com/pyenv/pyenv)
- [uv](https://docs.astral.sh/uv/)
- Python 3.12

```bash
brew install just pyenv uv
pyenv install
pyenv versions
```

## Setup

```bash
just setup
```

This installs dependencies, creates the `.env` file (if it doesn't exist), creates the `prompts/`
directory, and sets up pre-commit hooks.

## Usage

Required environment variables:

- `MODEL_NAME` - Hugging Face model ID (required)
- `PROMPT_FILE` - Prompt filename in `prompts/` (optional, defaults to `prompt.md`)

Edit `.env` to set your values.

### Prompts

Place your prompt in `prompts/prompt.md` (or set `PROMPT_FILE` in `.env` to use a different file).

### Image Generation

```bash
just image
```

## Development

### Code Quality Tools

This project uses several tools to maintain code quality:

```bash
just lint
just lint-fix
just format
just check
```

### Pre-commit Hooks

Pre-commit hooks run automatically on every commit after running `just setup`.
They run ruff and mypy to ensure code quality.

To run manually:

```bash
just pre-commit
```

## Project Structure

```
├── src/              # Source code
│   └── lib/          # Shared utilities
├── prompts/          # Prompt files
├── assets/images/    # Generated images
├── .env.example      # Environment template
├── justfile          # Task runner
└── pyproject.toml    # Project config
```
