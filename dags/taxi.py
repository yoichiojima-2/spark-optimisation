from datetime import date

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sdk import dag
from dateutil.relativedelta import relativedelta
from docker.types import Mount


def all_dates_between(start_date: date, end_date) -> list[date]:
    return [start_date + relativedelta(days=i) for i in range((end_date - start_date).days + 1)]


def is_end_of_month(dt: date) -> bool:
    return dt == dt + relativedelta(months=1, day=1, days=-1)


def end_of_months_between(start_date: date, end_date: date) -> list[date]:
    return [dt for dt in all_dates_between(start_date, end_date) if is_end_of_month(dt)]


@dag()
def taxi():
    start_date = date(2023, 1, 1)
    end_date = date(2024, 12, 31)

    for d in end_of_months_between(start_date, end_date):
        download = DockerOperator(
            task_id=f"download_{d}",
            image="spark-optimisation-spark:latest",
            command=f"uv run python -m spark_optimisation.taxi.raw --start-date {d} --end-date {d}",
            working_dir="/app",
            network_mode="spark-optimisation_spark-airflow",
            mounts=[Mount(source="/Users/yo/Developer/repo/spark-optimisation", target="/app", type="bind")],
            auto_remove="success",
            docker_url="unix://var/run/docker.sock",
            environment={"PYTHONPATH": "/app/src:/app"},
            retries=3,
        )

        cleanse = DockerOperator(
            task_id=f"cleanse_{d}",
            image="spark-optimisation-spark:latest",
            command=f"uv run python -m spark_optimisation.taxi.cleanse --start-date {d} --end-date {d}",
            working_dir="/app",
            network_mode="spark-optimisation_spark-airflow",
            mounts=[Mount(source="/Users/yo/Developer/repo/spark-optimisation", target="/app", type="bind")],
            auto_remove="success",
            docker_url="unix://var/run/docker.sock",
            environment={"PYTHONPATH": "/app/src:/app"},
            retries=3,
        )

        download >> cleanse


taxi()
