import pytest


@pytest.mark.usefixtures("minio_connection")
@pytest.fixture()
def prepare_bucket(minio_connection):
    minio_connection.create_bucket(
        bucket_name="minio-act-testing",
        region="us-east-1"
    )
    yield minio_connection

@pytest.mark.usefixtures("prepare_bucket")
def test_create_bucket(prepare_bucket):
    prepare_bucket.delete_bucket(
        bucket_name="minio-act-testing"
    )
    assert True
