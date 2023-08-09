import pytest


@pytest.mark.usefixtures("minio_connection")
@pytest.fixture()
def prepare_bucket(minio_connection):
    yield minio_connection
    minio_connection.delete_bucket("minio-act-testing")

@pytest.mark.usefixtures("prepare_bucket")
def test_create_bucket(prepare_bucket):
    prepare_bucket.create_bucket(
        bucket_name="minio-act-testing",
        region="us-east-1"
    )
    assert True
