import os
import pytest

from minio_act.client import MinioClient

@pytest.mark.usefixtures("minio_connection")
def test_connection(minio_connection):
    minio = MinioClient(
        endpoint=os.getenv("AWS_S3_ENDPOINT"),
        access_key=os.getenv("AWS_ACCESS_KEY"),
        secret_key=os.getenv("AWS_SECRET_KEY"),
        secure=False
    )
    assert True
