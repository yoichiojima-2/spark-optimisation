from datetime import date
from pathlib import Path

from spark_optimisation.taxi import raw


def path():
    p = Path("artifacts/taxi/cleansed")
    p.mkdir(parents=True, exist_ok=True)
    return p


def cleanse(target_date: date):
    df = raw.read(target_date)
    df.write.parquet(str(path() / f"{target_date.strftime('y=%Y/m=%m')}"))


def cleanses(start_date: date, end_date: date):
    for dt in raw.end_of_months_between(start_date, end_date):
        cleanse(dt)


if __name__ == "__main__":
    from spark_optimisation.taxi.cli import parse_args

    args = parse_args()
    cleanses(args.start_date, args.end_date)
