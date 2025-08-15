import os
from datetime import date
from pathlib import Path

import requests
from dateutil.relativedelta import relativedelta
from tqdm import tqdm

START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 12, 31)
OUTPUT_PATH = Path("data/nyc_taxi/raw")


def all_dates_between(start_date: date, end_date) -> list[date]:
    return [start_date - relativedelta(days=i) for i in range((end_date - start_date).days + 1)]


def fetch(year: int, month: int):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
    filename = f"yellow_tripdata_{date(year, month, 1).strftime('%Y-%m')}.parquet"
    return requests.get(f"{base_url}/{filename}")


def init():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def download_data(start_date: date, end_date: date):
    for dt in tqdm(all_dates_between(start_date, end_date), desc="downloading mock"):
        response = fetch(dt.year, dt.month)
        print(response)


def get_size_mb(path: str) -> int:
    return os.path.getsize(path) / (1024 * 1024)


def main():
    init()
    download_data(START_DATE, END_DATE)


if __name__ == "__main__":
    main()
