run:
	docker compose exec spark uv run python -m main

test:
	docker compose exec spark uv run pytest -vvv .

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

tidy:
	uv run ruff format .
	uv run ruff check --fix .
	npx prettier --write .
