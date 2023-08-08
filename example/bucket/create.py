import os

from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint=os.getenv("AWS_S3_ENDPOINT"),
    access_key=os.getenv("AWS_ACCESS_KEY"),
    secret_key=os.getenv("AWS_SECRET_KEY"),
    secure=False
)
minio_src.create_bucket(
    bucket_name="minio-bk",
    region="ap-southeast-1"
)
