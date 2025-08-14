import tomllib
from datetime import date

from functools import cached_property
from pyspark.sql import SparkSession, DataFrame, functions as F


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


spark = get_spark_session()


def mock_df() -> DataFrame:
    data = [
        ("user-id-1", "2025", "01", "01"),
        ("user-id-2", "2025", "02", "01"),
        ("user-id-3", "2025", "03", "01"),
        ("user-id-4", "2025", "04", "01"),
    ]
    columns = ["id", "y", "m", "d"]
    return spark.createDataFrame(data, columns)


def read_parquet() -> DataFrame:
    spark = get_spark_session()
    path = "./artifacts/data"
    spark.read.parquet(path)
    return


def main():
    start_date, end_date = date(2025, 2, 1), date(2025, 3, 31)
    date_col = F.to_date(F.concat_ws("-", F.col("y"), F.col("m"), F.col("d"))).alias("date")
    mock_df().filter(date_col.between(start_date, end_date)).show()


if __name__ == "__main__":
    main()
