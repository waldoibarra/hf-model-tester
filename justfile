help:
  @just --list

setup:
  uv sync
  uv run pre-commit install
  test -f .env || cp .env.example .env
  mkdir -p prompts

lint:
  uv run ruff check src/

lint-fix:
  uv run ruff check src/ --fix

format:
    uv run ruff format src/

check:
    uv run mypy

pre-commit:
  uv run pre-commit run --all-files

image:
  uv run src/z-image-turbo.py
