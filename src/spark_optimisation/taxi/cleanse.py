from datetime import date
from pathlib import Path

from pyspark.sql.types import StructType, StructField, IntegerType, TimestampNTZType, LongType, DoubleType, StringType

from spark_optimisation.taxi import raw


def path():
    p = Path("artifacts/taxi/cleansed")
    p.mkdir(parents=True, exist_ok=True)
    return p


def get_static_schema():
    """Define a static schema for taxi data to ensure consistency across partitions."""
    return StructType([
        StructField("VendorID", IntegerType(), True),
        StructField("tpep_pickup_datetime", TimestampNTZType(), True),
        StructField("tpep_dropoff_datetime", TimestampNTZType(), True),
        StructField("passenger_count", LongType(), True),
        StructField("trip_distance", DoubleType(), True),
        StructField("RatecodeID", LongType(), True),
        StructField("store_and_fwd_flag", StringType(), True),
        StructField("PULocationID", IntegerType(), True),
        StructField("DOLocationID", IntegerType(), True),
        StructField("payment_type", LongType(), True),
        StructField("fare_amount", DoubleType(), True),
        StructField("extra", DoubleType(), True),
        StructField("mta_tax", DoubleType(), True),
        StructField("tip_amount", DoubleType(), True),
        StructField("tolls_amount", DoubleType(), True),
        StructField("improvement_surcharge", DoubleType(), True),
        StructField("total_amount", DoubleType(), True),
        StructField("congestion_surcharge", DoubleType(), True),
        StructField("Airport_fee", DoubleType(), True),
    ])


def cleanse(target_date: date):
    df = raw.read(target_date)
    static_schema = get_static_schema()
    
    # Cast the dataframe to the static schema to ensure consistent types
    df_casted = df.select([df[field.name].cast(field.dataType).alias(field.name) for field in static_schema.fields])
    
    df_casted.write.parquet(str(path() / f"{target_date.strftime('y=%Y/m=%m')}"), mode="overwrite")


def cleanses(start_date: date, end_date: date):
    for dt in raw.end_of_months_between(start_date, end_date):
        cleanse(dt)


if __name__ == "__main__":
    print("cleansing taxi data...")
    from spark_optimisation.taxi.cli import parse_args

    args = parse_args()
    cleanses(args.start_date, args.end_date)

    print("done: cleansing taxi data")
