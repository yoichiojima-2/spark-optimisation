import tomllib
from datetime import date
from functools import cached_property

from dateutil.relativedelta import relativedelta
from pyspark.sql import SparkSession


class Config:
    @property
    def name(self):
        return self.pyproject["project"]["name"]

    @property
    def version(self):
        return self.pyproject["project"]["version"]

    @cached_property
    def pyproject(self):
        with open("pyproject.toml", "rb") as f:
            return tomllib.load(f)


def get_spark_session():
    config = Config()
    return SparkSession.builder.appName(config.name).getOrCreate()


def all_dates_between(start_date: date, end_date) -> list[date]:
    return [start_date + relativedelta(days=i) for i in range((end_date - start_date).days + 1)]


def is_end_of_month(dt: date) -> bool:
    return dt == dt + relativedelta(months=1, day=1, days=-1)


def end_of_months_between(start_date: date, end_date: date) -> list[date]:
    return [dt for dt in all_dates_between(start_date, end_date) if is_end_of_month(dt)]
