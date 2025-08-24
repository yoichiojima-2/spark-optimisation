from datetime import date
from multiprocessing import Pool
from pathlib import Path

import requests

from spark_optimisation.lib import end_of_months_between, get_spark_session


def filename(target_date: date) -> str:
    return f"yellow_tripdata_{target_date.strftime('%Y-%m')}.parquet"


def filepath(target_date: date) -> Path:
    return Path("artifacts/taxi/raw") / filename(target_date)


def fetch(target_date: date):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
    response = requests.get(f"{base_url}/{filename(target_date)}")
    if response.status_code == 200:
        return response
    else:
        raise Exception(f"Failed to fetch data for {target_date}: {response.status_code}")


def download(target_date: date):
    path = filepath(target_date)
    print(f"donwloading taxi data...: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    content = fetch(target_date).content
    path.write_bytes(content)
    print(f"donwloaded taxi data.: {path}")


def downloads(start_date: date, end_date: date):
    with Pool() as pool:
        pool.map(download, end_of_months_between(start_date, end_date))


def read(target_date: date):
    spark = get_spark_session()
    path = filepath(target_date)
    return spark.read.parquet(str(path))


if __name__ == "__main__":
    from spark_optimisation.taxi.cli import parse_args

    args = parse_args()
    downloads(args.start_date, args.end_date)
