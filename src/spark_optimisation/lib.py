import tomllib
from functools import cached_property
from pyspark.sql import DataFrame, SparkSession


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


def mock_df() -> DataFrame:
    data = [
        ("user-id-1", "2025", "01", "01"),
        ("user-id-2", "2025", "02", "01"),
        ("user-id-3", "2025", "03", "01"),
        ("user-id-4", "2025", "04", "01"),
    ]
    columns = ["id", "y", "m", "d"]
    return get_spark_session().createDataFrame(data, columns)
