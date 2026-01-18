from minio import Minio
import os
from dotenv import load_dotenv

load_dotenv()
client = Minio(
            os.getenv("MINIO_ENDPOINT"),
            access_key=os.getenv("MINIO_ACCESS_KEY"),
            secret_key=os.getenv("MINIO_SECRET_KEY"),
            secure=False
)
bucket = os.getenv("MINIO_BUCKET")
if not client.bucket_exists(bucket):
    client.make_bucket(bucket)
    print(f"Bucket '{bucket}' created")
else:
    print(f"Bucket '{bucket}' already exists")