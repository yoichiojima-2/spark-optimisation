from pyspark.sql import DataFrame

from spark_optimisation.lib import get_spark_session


def read_parquet() -> DataFrame:
    path = "./artifacts/mock-1"
    return get_spark_session().read.parquet(path)


def main():
    df = read_parquet()
    df.show()


if __name__ == "__main__":
    main()
