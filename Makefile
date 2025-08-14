run:
	docker compose exec spark uv run python src/spark_optimisation/main.py

test:
	docker compose exec spark uv run pytest -vvv 

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down
	
install:
	uv sync
	uv run pip install -e .

tidy:
	uv run isort .
	uv run ruff format .
	uv run ruff check --fix .
	npx prettier --write .
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
