from spark_optimisation.lib import get_spark_session


def main():
    path = "./artifacts/mock-1"
    df = get_spark_session().read.parquet(path)
    keys = ["y", "m"]
    (df.groupBy(*keys).count().sort(*keys).show())


if __name__ == "__main__":
    main()
