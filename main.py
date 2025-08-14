import tomllib
from functools import cached_property
from pyspark.sql import SparkSession, functions as F


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


def main():
    spark = get_spark_session()
    print(spark)


if __name__ == "__main__":
    main()
