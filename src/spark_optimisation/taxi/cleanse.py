from pathlib import Path
from datetime import date
from spark_optimisation.taxi import raw


def path():
    return Path("artifacts/taxi/cleaned")

def cleanse(target_date: date):
    df = raw.read(target_date)
    df.write.parquet(str(path() / f"taxi/{target_date.strftime('y=%Y/m=%m')}"))

def cleanses(start_date: date, end_date: date):
    for dt in raw.end_of_months_between(start_date, end_date):
        cleanse(dt)