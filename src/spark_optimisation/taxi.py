from datetime import date
from pathlib import Path

from spark_optimisation.lib import get_spark_session


def filename(target_date: date) -> str:
    return f"yellow_tripdata_{target_date.strftime('%Y-%m')}.parquet"


def filepath(target_date: date) -> Path:
    return Path("artifacts/nyc-taxi/raw") / filename(target_date)


def read(target_date: date):
    spark = get_spark_session()
    path = filepath(target_date)
    return spark.read.parquet(str(path))
