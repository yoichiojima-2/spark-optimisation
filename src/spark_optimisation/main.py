from pyspark.sql import DataFrame
from spark_optimisation import get_spark_session


def read_parquet() -> DataFrame:
    path = "./artifacts/mock"
    get_spark_session().read.parquet(path)
    return


def main():
    ...
    # start_date, end_date = date(2025, 2, 1), date(2025, 3, 31)
    # date_col = F.to_date(F.concat_ws("-", F.col("y"), F.col("m"), F.col("d"))).alias("date")


if __name__ == "__main__":
    main()
