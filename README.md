# spark-optimisation

Experiments around Spark job optimisation.

**Status:** early scaffolding. What's here so far is the groundwork — a
Dockerised Spark + Airflow environment and an ingestion pipeline for the
[NYC yellow taxi trip data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
that will serve as the workload for optimisation experiments. No optimisation
experiments are committed yet.

## What's in the box

- `src/spark_optimisation/taxi/raw.py` — downloads monthly yellow-taxi parquet
  files to `artifacts/taxi/raw/`
- `src/spark_optimisation/taxi/cleanse.py` — casts the raw data to a static
  schema and writes partitioned parquet to `artifacts/taxi/cleansed/`
- `dags/taxi.py` — Airflow DAG that runs the cleanse step per month via
  `DockerOperator`
- `docker-compose.yml` — Spark container, Jupyter Lab, and a full local
  Airflow stack (Postgres, Redis, scheduler, workers)

## Usage

Requires Docker.

```bash
make build-container
make up            # start Spark, Jupyter, and Airflow

make run           # run the example job (reads raw taxi data, aggregates by pickup date)
make test          # run pytest inside the Spark container

make down          # stop everything
```

Download raw data inside the Spark container:

```bash
docker compose exec spark uv run python -m spark_optimisation.taxi.raw \
  --start-date 2024-01-01 --end-date 2024-12-31
```

The Airflow UI is available at `http://localhost:8080` once the stack is up.
