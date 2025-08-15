run:
	docker compose exec spark uv run python src/spark_optimisation/main.py

test:
	docker compose exec spark uv run pytest -vvv 

mock:
	docker compose exec spark uv run python bin/write_mock.py

build-container:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

tidy:
	uv run isort .
	uv run ruff format .
	uv run ruff check --fix .
	npx prettier --write .
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
