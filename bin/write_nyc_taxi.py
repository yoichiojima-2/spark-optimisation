from datetime import date
from pathlib import Path

import requests
from tqdm import tqdm

from spark_optimisation.lib import end_of_months_between


START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 3, 31)
OUTPUT_PATH = Path("data/nyc_taxi/raw")


def init():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def fetch(year: int, month: int):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
    filename = f"yellow_tripdata_{date(year, month, 1).strftime('%Y-%m')}.parquet"
    response = requests.get(f"{base_url}/{filename}")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for {year}-{month}: {response.status_code}")
    return response


def main(start_date: date, end_date: date):
    init()
    for dt in tqdm(end_of_months_between(start_date, end_date), desc="downloading nyc taxi data"):
        content = fetch(dt.year, dt.month).content
        OUTPUT_PATH.write_bytes(content)
        print(f"Downloaded and saved data for {dt.strftime('%Y-%m')}")


if __name__ == "__main__":
    main(START_DATE, END_DATE)
