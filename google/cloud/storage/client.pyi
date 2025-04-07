# mypy: ignore-errors

from _typeshed import Incomplete
from google.api_core import page_iterator as page_iterator
from google.auth.credentials import AnonymousCredentials as AnonymousCredentials
from google.cloud.client import ClientWithProject as ClientWithProject
from google.cloud.exceptions import NotFound as NotFound
from google.cloud.storage._http import Connection as Connection
from google.cloud.storage._opentelemetry_tracing import create_trace_span as create_trace_span
from google.cloud.storage._signing import ensure_signed_credentials as ensure_signed_credentials
from google.cloud.storage._signing import get_expiration_seconds_v4 as get_expiration_seconds_v4
from google.cloud.storage._signing import get_v4_now_dtstamps as get_v4_now_dtstamps
from google.cloud.storage.acl import BucketACL as BucketACL
from google.cloud.storage.acl import DefaultObjectACL as DefaultObjectACL
from google.cloud.storage.batch import Batch as Batch
from google.cloud.storage.blob import Blob as Blob
from google.cloud.storage.bucket import Bucket as Bucket
from google.cloud.storage.hmac_key import HMACKeyMetadata as HMACKeyMetadata
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY

class Client(ClientWithProject):
    SCOPE: Incomplete
    project: Incomplete
    def __init__(
        self,
        project=...,
        credentials: Incomplete | None = None,
        _http: Incomplete | None = None,
        client_info: Incomplete | None = None,
        client_options: Incomplete | None = None,
        use_auth_w_custom_endpoint: bool = True,
        extra_headers={},
        *,
        api_key: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def create_anonymous_client(cls): ...
    @property
    def universe_domain(self): ...
    @property
    def api_endpoint(self): ...
    @property
    def current_batch(self): ...
    def get_service_account_email(self, project: Incomplete | None = None, timeout=..., retry=...): ...
    def bucket(self, bucket_name, user_project: Incomplete | None = None, generation: Incomplete | None = None): ...
    def batch(self, raise_exception: bool = True): ...
    def get_bucket(
        self,
        bucket_or_name,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
        *,
        generation: Incomplete | None = None,
        soft_deleted: Incomplete | None = None,
    ): ...
    def lookup_bucket(
        self,
        bucket_name,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ): ...
    def create_bucket(
        self,
        bucket_or_name,
        requester_pays: Incomplete | None = None,
        project: Incomplete | None = None,
        user_project: Incomplete | None = None,
        location: Incomplete | None = None,
        data_locations: Incomplete | None = None,
        predefined_acl: Incomplete | None = None,
        predefined_default_object_acl: Incomplete | None = None,
        enable_object_retention: bool = False,
        timeout=...,
        retry=...,
    ): ...
    def download_blob_to_file(
        self,
        blob_or_uri,
        file_obj,
        start: Incomplete | None = None,
        end: Incomplete | None = None,
        raw_download: bool = False,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        checksum: str = "auto",
        retry=...,
    ) -> None: ...
    def list_blobs(
        self,
        bucket_or_name,
        max_results: Incomplete | None = None,
        page_token: Incomplete | None = None,
        prefix: Incomplete | None = None,
        delimiter: Incomplete | None = None,
        start_offset: Incomplete | None = None,
        end_offset: Incomplete | None = None,
        include_trailing_delimiter: Incomplete | None = None,
        versions: Incomplete | None = None,
        projection: str = "noAcl",
        fields: Incomplete | None = None,
        page_size: Incomplete | None = None,
        timeout=...,
        retry=...,
        match_glob: Incomplete | None = None,
        include_folders_as_prefixes: Incomplete | None = None,
        soft_deleted: Incomplete | None = None,
    ): ...
    def list_buckets(
        self,
        max_results: Incomplete | None = None,
        page_token: Incomplete | None = None,
        prefix: Incomplete | None = None,
        projection: str = "noAcl",
        fields: Incomplete | None = None,
        project: Incomplete | None = None,
        page_size: Incomplete | None = None,
        timeout=...,
        retry=...,
        *,
        soft_deleted: Incomplete | None = None,
    ): ...
    def restore_bucket(
        self,
        bucket_name,
        generation,
        projection: str = "noAcl",
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    def create_hmac_key(
        self,
        service_account_email,
        project_id: Incomplete | None = None,
        user_project: Incomplete | None = None,
        timeout=...,
        retry: Incomplete | None = None,
    ): ...
    def list_hmac_keys(
        self,
        max_results: Incomplete | None = None,
        service_account_email: Incomplete | None = None,
        show_deleted_keys: Incomplete | None = None,
        project_id: Incomplete | None = None,
        user_project: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    def get_hmac_key_metadata(
        self, access_id, project_id: Incomplete | None = None, user_project: Incomplete | None = None, timeout=...
    ): ...
    def generate_signed_post_policy_v4(
        self,
        bucket_name,
        blob_name,
        expiration,
        conditions: Incomplete | None = None,
        fields: Incomplete | None = None,
        credentials: Incomplete | None = None,
        virtual_hosted_style: bool = False,
        bucket_bound_hostname: Incomplete | None = None,
        scheme: str = "http",
        service_account_email: Incomplete | None = None,
        access_token: Incomplete | None = None,
    ): ...
