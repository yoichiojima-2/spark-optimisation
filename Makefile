UV = docker compose exec spark uv
DOCKER = docker
NPX = npx

.PHONY: install run test ipython mock taxi build-container up down tidy clean

run:
	${UV} run python -m spark_optimisation.main

test:
	${UV} run pytest -vvv

ipython:
	${UV} run ipython

mock:
	${UV} run python bin/write_mock.py

taxi:
	${UV} run python bin/make_taxi.py

build-container:
	${DOCKER} compose build

up:
	${DOCKER} compose up -d

down:
	${DOCKER} compose down

restart:
	${DOCKER} compose restart

tidy:
	${UV} run isort .
	${UV} run ruff format .
	${UV} run ruff check --fix .
	${NPX} prettier --write .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .venv -exec rm -rf {} +
	find . -type d -name build -exec rm -rf {} +
	find . -type d -name logs -exec rm -rf {} +
	find . -type d -name *.egg-info -exec rm -rf {} +
	find . -type d -name .ipynb_checkpoints -exec rm -rf {} +
	find . -type f -name uv.lock -exec rm -f {} +

