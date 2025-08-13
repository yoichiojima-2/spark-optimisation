pre-commit:
	uv run ruff format .
	uv run ruff check --fix .
	npx prettier --write .
