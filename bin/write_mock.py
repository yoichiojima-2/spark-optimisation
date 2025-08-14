from spark_optimisation import mock_df


def write_mock():
    path = "./artifacts/mock"
    df = mock_df()
    df.write.parquet(path, partitionBy=["y", "m", "d"], mode="overwrite")
    print(f"done writting mock: {path}")


if __name__ == "__main__":
    write_mock()
