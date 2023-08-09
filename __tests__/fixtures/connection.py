import pytest

from minio_act.client import MinioClient

@pytest.fixture(scope="session")
def minio_connection():
    yield MinioClient(
        endpoint="play.min.io",
        access_key="fPzyqVjlvdMnqsCnYmaj",
        secret_key="J3N0wtEevHdGbVFiqDvA7FVJv7L9IKEnQG99jBi3",
        secure=False
    )


