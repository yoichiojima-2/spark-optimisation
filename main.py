import tomllib
from pyspark.sql import SparkSession


class Config:
    def __init__(self):
        self.config = self.read_config()

    @property
    def name(self):
        return self.config["name"]

    @property
    def version(self):
        return self.config["version"]

    def read_config(self):
        with open("pyproject.toml", "r") as f:
            pyproject = tomllib.load(f)
        return pyproject["project"]["version"]


def get_spark_session():
    config = Config()
    return SparkSession.builder.appName(config.name).getOrCreate()


def main():
    spark = get_spark_session()
    print(spark)
    print("Hello from spark-optimisation!")


if __name__ == "__main__":
    main()
