from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint="play.min.io:9000",
    access_key="fPzyqVjlvdMnqsCnYmaj",
    secret_key="J3N0wtEevHdGbVFiqDvA7FVJv7L9IKEnQG99jBi3",
)
buckets = minio_src.list_bucket()

for bucket in buckets:
    print(bucket.name, " "*3, bucket.creation_date)