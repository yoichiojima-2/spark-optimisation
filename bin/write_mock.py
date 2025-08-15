from pyspark.sql import DataFrame

from spark_optimisation import get_spark_session


def mock_df() -> DataFrame:
    data = [
        ("user-id-1", "2025", "01", "01"),
        ("user-id-2", "2025", "02", "01"),
        ("user-id-3", "2025", "03", "01"),
        ("user-id-4", "2025", "04", "01"),
    ]
    columns = ["id", "y", "m", "d"]
    return get_spark_session().createDataFrame(data, columns)


def write_mock():
    path = "./artifacts/mock-1"
    df = mock_df()
    df.write.parquet(path, partitionBy=["y", "m", "d"], mode="overwrite")
    print(f"done writting mock: {path}")


if __name__ == "__main__":
    write_mock()
