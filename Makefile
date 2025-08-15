run:
	docker compose exec -e PYTHONPATH=/home/src spark uv run python -m spark_optimisation.main

test:
	docker compose exec -e PYTHONPATH=/home/src spark uv run pytest -vvv 

mock:
	docker compose exec -e PYTHONPATH=/home/src spark uv run python bin/write_mock.py

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
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .venv -exec rm -rf {} +
	find . -type d -name build -exec rm -rf {} +
	find . -type d -name logs -exec rm -rf {} +
	find . -type f -name uv.lock -exec rm -f {} +

