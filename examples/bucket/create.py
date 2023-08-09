from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint="play.min.io:9000",
    access_key="fPzyqVjlvdMnqsCnYmaj",
    secret_key="J3N0wtEevHdGbVFiqDvA7FVJv7L9IKEnQG99jBi3",
)
minio_src.create_bucket(
    bucket_name="minio-bk",
    region="us-east-1"
)
