import pytest

from minio_act.client import MinioClient

@pytest.mark.usefixtures("minio_connection")
def test_connection(minio_connection):
    minio = MinioClient(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=False
    )
    assert True
