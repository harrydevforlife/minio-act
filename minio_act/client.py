from typing import Any, Generator, List

from minio import Minio

from minio_act.bucket import Bucket
from minio_act.log import logger

class MinioClient:

    def __init__(self,
                 endpoint: str,
                 access_key: Any = None,
                 secret_key: Any = None,
                 session_token: Any =None,
                 secure: bool = True,
                 region: Any = None,
                 http_client: Any = None,
                 credentials: Any = None,
                 *args, **kwargs ):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.session_token = session_token
        self.secure = secure
        self.region = region
        self.http_client = http_client
        self.credentials = credentials
        self.client = self.client_connect()

    def client_connect(self):
        return Minio(
            endpoint=self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            session_token=self.session_token,
            secure=self.secure,
            region=self.region,
            http_client=self.http_client,
            credentials=self.credentials
        )
    
    def download_bucket(self, bucket_name: Any) -> None:
        self._download_bucket(bucket_name)

    def _download_bucket(self, bucket_name: Any) -> None:
        logger.info(f"Downloading bucket {str(bucket_name)} ...")
        for item in self.client.list_objects(bucket_name, recursive=True):
            self.client.fget_object(bucket_name, item.object_name, item.object_name)

    def bucket_exists(self, bucket_name: Any) -> bool:
        self._bucket_exists(bucket_name)

    def _bucket_exists(self, bucket_name: Any) -> bool:
        logger.info(f"Checking bucket {str(bucket_name)} exists ...")
        return self.client.bucket_exists(
            bucket_name=bucket_name
        )
    
    def list_bucket(self) -> List[str]:
        return self._list_bucket()

    def _list_bucket(self) -> List[str]:
        logger.info(f"Listing buckets ...")
        return self.client.list_buckets()
    
    def create_bucket(self, bucket_name: Any, region: Any, object_lock: bool = False) -> None:
        self._create_bucket(
            bucket_name=bucket_name,
            region=region,
            object_lock=object_lock
        )

    def _create_bucket(self, bucket_name: Any, region: Any, object_lock: bool = False) -> None:
        logger.info(f"Creating bucket {str(bucket_name)} ...")
        return self.client.make_bucket(
            bucket_name=bucket_name,
            location=region,
            object_lock=object_lock
        )
    
    def delete_bucket(self, bucket_name: Any) -> None:
        self._delete_bucket(bucket_name=bucket_name)
    
    def _delete_bucket(self, bucket_name: Any):
        logger.info(f"Deleting bucket {str(bucket_name)} ...")
        return self.client.remove_bucket(
            bucket_name=bucket_name
        )
    
    def delete_object(self, bucket_name: Any, object_name: Any, version_id: Any = None) -> None:
        self._delete_object(
            bucket_name=bucket_name,
            object_name=object_name,
            version_id=version_id
        )

    def _delete_object(self, bucket_name: Any, object_name: Any, version_id: Any = None) -> None:
        logger.info(f"Deleting {str(object_name)} in bucket {str(bucket_name)} ...")
        return self.client.remove_object(
            bucket_name=bucket_name,
            object_name=object_name,
            version_id=version_id
        )
    
    def delete_objects(self, bucket_name: Any, delete_object_list: List[Any], bypass_governance_mode: bool = False) -> Generator[Any, Any, None]:
        self._delete_objects(
            bucket_name=bucket_name,
            delete_object_list=delete_object_list,
            bypass_governance_mode=bypass_governance_mode
        )
    
    def _delete_objects(self, bucket_name: Any, delete_object_list: List[Any], bypass_governance_mode: bool = False) -> Generator[Any, Any, None]:
        logger.info(f"Deleting multiple objects in bucket {str(bucket_name)} ...")
        return self.client.remove_objects(
            bucket_name=bucket_name,
            delete_object_list=delete_object_list,
            bypass_governance_mode=bypass_governance_mode
        )





