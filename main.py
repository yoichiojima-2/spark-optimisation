import tomllib
from pyspark.sql import SparkSession


class Config:
    def __init__(self):
        self.config = self.load()

    @property
    def name(self):
        return self.config["name"]

    @property
    def version(self):
        return self.config["version"]

    def load(self):
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
            print(config)
            return config["project"]


def get_spark_session():
    config = Config()
    return SparkSession.builder.appName(config.name).getOrCreate()


def main():
    spark = get_spark_session()
    print(f"Spark session created: {spark}")
    print("Hello from spark-optimisation!")

    # Test Spark with some basic operations
    print("\n=== Testing Spark Operations ===")

    # Create a simple DataFrame
    data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35), (4, "Diana", 28), (5, "Eve", 32)]
    columns = ["id", "name", "age"]

    df = spark.createDataFrame(data, columns)
    print("\n1. Created DataFrame:")
    df.show()

    # Basic operations
    print("2. DataFrame Schema:")
    df.printSchema()

    print("3. Count of records:", df.count())

    print("\n4. Filter (age > 30):")
    df.filter(df.age > 30).show()

    print("5. Average age:")
    df.agg({"age": "avg"}).show()

    print("\n6. Group by age ranges:")
    from pyspark.sql import functions as F

    df.withColumn("age_group", F.when(F.col("age") < 30, "Under 30").otherwise("30 and over")).groupBy(
        "age_group"
    ).count().show()

    # Stop Spark session
    spark.stop()
    print("\n=== Spark session closed successfully ===")


if __name__ == "__main__":
    main()
