from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, to_date, hour, when, unix_timestamp
)

# spark session
spark = (
    SparkSession.builder
        .appName("silver-trips-transform")
        .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
        .config("spark.hadoop.fs.s3a.access.key", "minio")
        .config("spark.hadoop.fs.s3a.secret.key", "minio123")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .getOrCreate()
)

# Read bronze data (no need to specify schema - it's already in parquet)
bronze_df = spark.read.parquet("s3a://bronze/yellow_tripdata/2023/01/")

print(f"Bronze records: {bronze_df.count()}")

# DQ checks - using correct column names
clean_df = (
    bronze_df
    .filter(col("tpep_pickup_datetime").isNotNull())  # Changed from pickup_datetime
    .filter(col("tpep_dropoff_datetime").isNotNull())  # Changed from dropoff_datetime
    .filter(col("trip_distance") > 0)
    .filter(col("fare_amount") >= 0)
    .filter(col("tpep_dropoff_datetime") >= col("tpep_pickup_datetime"))  # Changed column names
)

print(f"After DQ checks: {clean_df.count()}")

# Feature engineering - using correct column names
enriched_df = (
    clean_df
    .withColumn("trip_duration_minutes",
                (unix_timestamp("tpep_dropoff_datetime") - unix_timestamp("tpep_pickup_datetime")) / 60  # Convert to minutes
    )
    .withColumn("pickup_date", to_date("tpep_pickup_datetime"))
    .withColumn("pickup_hour", hour("tpep_pickup_datetime"))
    .withColumn("time_of_day",
                when(col("pickup_hour").between(5, 11), "morning")
                .when(col("pickup_hour").between(12, 16), "afternoon")
                .when(col("pickup_hour").between(17, 21), "evening")
                .otherwise("night"))
)

print(f"Final enriched records: {enriched_df.count()}")

# Write silver (partitioned)
print("Writing to silver layer...")
(enriched_df.write
    .mode("overwrite")
    .partitionBy("pickup_date")
    .parquet("s3a://silver/yellow_tripdata/")
)

print("Silver layer write completed!")
spark.stop()