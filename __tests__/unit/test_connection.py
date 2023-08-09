import pytest

from minio_act.client import MinioClient

@pytest.mark.usefixtures("minio_connection")
def test_connection(minio_connection):
    minio = MinioClient(
        endpoint="play.min.io:9000",
        access_key="fPzyqVjlvdMnqsCnYmaj",
        secret_key="J3N0wtEevHdGbVFiqDvA7FVJv7L9IKEnQG99jBi3",
    )
    assert True
