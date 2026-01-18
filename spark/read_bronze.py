from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
        .appName("check-bronze-data")
        .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
        .config("spark.hadoop.fs.s3a.access.key", "minio")
        .config("spark.hadoop.fs.s3a.secret.key", "minio123")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .getOrCreate()
)

# Read without schema to see actual columns
bronze_df = spark.read.parquet("s3a://bronze/yellow_tripdata/2023/01")

print("=== SCHEMA ===")
bronze_df.printSchema()

print("\n=== COLUMN NAMES ===")
print(bronze_df.columns)

print("\n=== SAMPLE DATA (5 rows) ===")
bronze_df.show(5, truncate=False)

print("\n=== TOTAL RECORD COUNT ===")
print(f"Total records: {bronze_df.count()}")

spark.stop()