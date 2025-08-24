from datetime import date

from airflow.sdk import dag, task


@dag()
def taxi():
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)

    @task.bash
    def download():
        return f"docker-compose run spark 'uv run python -m spark_optimisation.taxi.raw --start-date {start_date} --end-date {end_date}'"

    @task.bash
    def cleanse():
        return f"docker-compose run spark 'uv run python -m spark_optimisation.taxi.cleanse --start-date {start_date} --end-date {end_date}'"

    download() >> cleanse()


taxi()
