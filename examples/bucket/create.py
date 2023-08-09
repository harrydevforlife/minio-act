from minio_act.client import MinioClient

minio_src = MinioClient(
    endpoint="play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    secure=False
)
minio_src.create_bucket(
    bucket_name="minio-bk",
    region="ap-southeast-1"
)
