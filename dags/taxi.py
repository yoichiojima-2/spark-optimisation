from datetime import date

from airflow.sdk import dag, task_group
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from spark_optimisation.lib import end_of_months_between


@dag()
def taxi():
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)

    @task_group
    def download():
        for d in end_of_months_between(start_date, end_date):
            DockerOperator(
                task_id=f'download_{d}',
                image='spark-optimisation-spark:latest',
                command=f'uv run python -m spark_optimisation.taxi.raw --start-date {d} --end-date {d}',
                working_dir='/app',
                network_mode='spark-optimisation_spark-airflow',
                mounts=[Mount(source="/Users/yo/Developer/repo/spark-optimisation", target="/app", type="bind")],
                auto_remove=True,
                docker_url='unix://var/run/docker.sock',
            )

    @task_group
    def cleanse():
        for d in end_of_months_between(start_date, end_date):
            DockerOperator(
                task_id=f'cleanse_{d}',
                image='spark-optimisation-spark:latest',
                command=f'uv run python -m spark_optimisation.taxi.cleanse --start-date {d} --end-date {d}',
                working_dir='/app',
                network_mode='spark-optimisation_spark-airflow',
                mounts=[Mount(source="/Users/yo/Developer/repo/spark-optimisation", target="/app", type="bind")],
                auto_remove=True,
                docker_url='unix://var/run/docker.sock',
            )

    download() >> cleanse()


taxi()
