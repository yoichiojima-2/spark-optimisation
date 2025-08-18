from datetime import date
from multiprocessing import Pool

import requests

from spark_optimisation.lib import end_of_months_between
from spark_optimisation.taxi import filename, filepath

START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 12, 31)


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
    content = fetch(target_date).content
    path.write_bytes(content)
    print(f"donwloaded taxi data.: {path}")


def write(start_date: date, end_date: date):
    with Pool() as pool:
        pool.map(download, end_of_months_between(start_date, end_date))


if __name__ == "__main__":
    write(START_DATE, END_DATE)
