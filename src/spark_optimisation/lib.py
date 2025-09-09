import tomllib
from functools import cached_property

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
