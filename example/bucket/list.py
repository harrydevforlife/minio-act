import os

from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint=os.getenv("AWS_S3_ENDPOINT"),
    access_key=os.getenv("AWS_ACCESS_KEY"),
    secret_key=os.getenv("AWS_SECRET_KEY"),
    secure=False
)
buckets = minio_src.list_bucket()

for bucket in buckets:
    print(bucket.name, bucket.creation_date)