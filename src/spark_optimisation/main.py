from spark_optimisation.lib import get_spark_session


def main():
    path = "./artifacts/mock-1"
    df = get_spark_session().read.parquet(path)
    df.show()


if __name__ == "__main__":
    main()
