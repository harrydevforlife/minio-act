from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint="play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    secure=False
)
buckets = minio_src.list_bucket()

for bucket in buckets:
    print(bucket.name, bucket.creation_date)