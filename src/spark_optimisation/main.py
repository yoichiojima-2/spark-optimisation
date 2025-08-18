from datetime import date

from pyspark.sql import functions as F

from . import taxi


def main():
    df = taxi.read(date(2024, 1, 1))
    df.printSchema()
    df.show(5)
    keys = ["tpep_pickup_date"]
    df.withColumn("tpep_pickup_date", F.to_date(F.col("tpep_pickup_datetime"))).groupBy(*keys).count().sort(*keys).show(50)


if __name__ == "__main__":
    main()
