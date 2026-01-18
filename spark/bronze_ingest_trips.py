from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit
import os

spark = (
    SparkSession.builder
    .appName("bronze-ingest")
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262")  # ADD THIS LINE
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
    .config("spark.hadoop.fs.s3a.access.key", "minio")
    .config("spark.hadoop.fs.s3a.secret.key", "minio123")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .getOrCreate()
)

df = spark.read.parquet("data/bronze/yellow_tripdata_2023-01.parquet")
df = (
    df.withColumn("ingestion_timestamp", current_timestamp())
      .withColumn("data_source", lit("TLC"))
)
df.write.mode("overwrite").parquet("s3a://bronze/yellow_tripdata/2023/01")
spark.stop()