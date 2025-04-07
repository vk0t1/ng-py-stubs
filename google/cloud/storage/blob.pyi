# mypy: ignore-errors

from _typeshed import Incomplete
from google.api_core.iam import Policy as Policy
from google.cloud import exceptions as exceptions
from google.cloud.exceptions import NotFound as NotFound
from google.cloud.storage._helpers import _PropertyMixin
from google.cloud.storage._media.requests import (
    ChunkedDownload as ChunkedDownload,
)
from google.cloud.storage._media.requests import (
    Download as Download,
)
from google.cloud.storage._media.requests import (
    MultipartUpload as MultipartUpload,
)
from google.cloud.storage._media.requests import (
    RawChunkedDownload as RawChunkedDownload,
)
from google.cloud.storage._media.requests import (
    RawDownload as RawDownload,
)
from google.cloud.storage._media.requests import (
    ResumableUpload as ResumableUpload,
)
from google.cloud.storage._opentelemetry_tracing import create_trace_span as create_trace_span
from google.cloud.storage._signing import (
    generate_signed_url_v2 as generate_signed_url_v2,
)
from google.cloud.storage._signing import (
    generate_signed_url_v4 as generate_signed_url_v4,
)
from google.cloud.storage.acl import ACL as ACL
from google.cloud.storage.acl import ObjectACL as ObjectACL
from google.cloud.storage.constants import (
    ARCHIVE_STORAGE_CLASS as ARCHIVE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    COLDLINE_STORAGE_CLASS as COLDLINE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    MULTI_REGIONAL_LEGACY_STORAGE_CLASS as MULTI_REGIONAL_LEGACY_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    NEARLINE_STORAGE_CLASS as NEARLINE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    REGIONAL_LEGACY_STORAGE_CLASS as REGIONAL_LEGACY_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    STANDARD_STORAGE_CLASS as STANDARD_STORAGE_CLASS,
)
from google.cloud.storage.exceptions import DataCorruption as DataCorruption
from google.cloud.storage.exceptions import InvalidResponse as InvalidResponse
from google.cloud.storage.fileio import BlobReader as BlobReader
from google.cloud.storage.fileio import BlobWriter as BlobWriter
from google.cloud.storage.retry import (
    DEFAULT_RETRY as DEFAULT_RETRY,
)
from google.cloud.storage.retry import (
    DEFAULT_RETRY_IF_ETAG_IN_JSON as DEFAULT_RETRY_IF_ETAG_IN_JSON,
)
from google.cloud.storage.retry import (
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED as DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
)
from google.cloud.storage.retry import (
    ConditionalRetryPolicy as ConditionalRetryPolicy,
)

class Blob(_PropertyMixin):
    STORAGE_CLASSES: Incomplete
    def __init__(
        self,
        name,
        bucket,
        chunk_size: Incomplete | None = None,
        encryption_key: Incomplete | None = None,
        kms_key_name: Incomplete | None = None,
        generation: Incomplete | None = None,
    ) -> None: ...
    @property
    def bucket(self): ...
    @property
    def chunk_size(self): ...
    @chunk_size.setter
    def chunk_size(self, value) -> None: ...
    @property
    def encryption_key(self): ...
    @encryption_key.setter
    def encryption_key(self, value) -> None: ...
    @staticmethod
    def path_helper(bucket_path, blob_name): ...
    @property
    def acl(self): ...
    @property
    def path(self): ...
    @property
    def client(self): ...
    @property
    def user_project(self): ...
    @property
    def public_url(self): ...
    @classmethod
    def from_uri(cls, uri, client: Incomplete | None = None): ...
    @classmethod
    def from_string(cls, uri, client: Incomplete | None = None): ...
    def generate_signed_url(
        self,
        expiration: Incomplete | None = None,
        api_access_endpoint: Incomplete | None = None,
        method: str = "GET",
        content_md5: Incomplete | None = None,
        content_type: Incomplete | None = None,
        response_disposition: Incomplete | None = None,
        response_type: Incomplete | None = None,
        generation: Incomplete | None = None,
        headers: Incomplete | None = None,
        query_parameters: Incomplete | None = None,
        client: Incomplete | None = None,
        credentials: Incomplete | None = None,
        version: Incomplete | None = None,
        service_account_email: Incomplete | None = None,
        access_token: Incomplete | None = None,
        virtual_hosted_style: bool = False,
        bucket_bound_hostname: Incomplete | None = None,
        scheme: str = "http",
    ): ...
    def exists(
        self,
        client: Incomplete | None = None,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
        soft_deleted: Incomplete | None = None,
    ): ...
    def delete(
        self,
        client: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ) -> None: ...
    def download_to_file(
        self,
        file_obj,
        client: Incomplete | None = None,
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
    def download_to_filename(
        self,
        filename,
        client: Incomplete | None = None,
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
    def download_as_bytes(
        self,
        client: Incomplete | None = None,
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
    ): ...
    def download_as_string(
        self,
        client: Incomplete | None = None,
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
        retry=...,
    ) -> bytes: ...
    def download_as_text(
        self,
        client: Incomplete | None = None,
        start: Incomplete | None = None,
        end: Incomplete | None = None,
        raw_download: bool = False,
        encoding: Incomplete | None = None,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    def upload_from_file(
        self,
        file_obj,
        rewind: bool = False,
        size: Incomplete | None = None,
        content_type: Incomplete | None = None,
        client: Incomplete | None = None,
        predefined_acl: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        checksum: str = "auto",
        retry=...,
    ) -> None: ...
    def upload_from_filename(
        self,
        filename,
        content_type: Incomplete | None = None,
        client: Incomplete | None = None,
        predefined_acl: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        checksum: str = "auto",
        retry=...,
    ) -> None: ...
    def upload_from_string(
        self,
        data,
        content_type: str = "text/plain",
        client: Incomplete | None = None,
        predefined_acl: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        checksum: str = "auto",
        retry=...,
    ) -> None: ...
    def create_resumable_upload_session(
        self,
        content_type: Incomplete | None = None,
        size: Incomplete | None = None,
        origin: Incomplete | None = None,
        client: Incomplete | None = None,
        timeout=...,
        checksum: str = "auto",
        predefined_acl: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ): ...
    def get_iam_policy(
        self,
        client: Incomplete | None = None,
        requested_policy_version: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    def set_iam_policy(self, policy, client: Incomplete | None = None, timeout=..., retry=...): ...
    def test_iam_permissions(self, permissions, client: Incomplete | None = None, timeout=..., retry=...): ...
    def make_public(
        self,
        client: Incomplete | None = None,
        timeout=...,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def make_private(
        self,
        client: Incomplete | None = None,
        timeout=...,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def compose(
        self,
        sources,
        client: Incomplete | None = None,
        timeout=...,
        if_generation_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_source_generation_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def rewrite(
        self,
        source,
        token: Incomplete | None = None,
        client: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        if_source_generation_match: Incomplete | None = None,
        if_source_generation_not_match: Incomplete | None = None,
        if_source_metageneration_match: Incomplete | None = None,
        if_source_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    def update_storage_class(
        self,
        new_class,
        client: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        if_source_generation_match: Incomplete | None = None,
        if_source_generation_not_match: Incomplete | None = None,
        if_source_metageneration_match: Incomplete | None = None,
        if_source_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ) -> None: ...
    def open(
        self,
        mode: str = "r",
        chunk_size: Incomplete | None = None,
        ignore_flush: Incomplete | None = None,
        encoding: Incomplete | None = None,
        errors: Incomplete | None = None,
        newline: Incomplete | None = None,
        **kwargs,
    ): ...
    cache_control: Incomplete
    content_disposition: Incomplete
    content_encoding: Incomplete
    content_language: Incomplete
    content_type: Incomplete
    crc32c: Incomplete
    @property
    def component_count(self): ...
    @property
    def etag(self): ...
    event_based_hold: Incomplete
    @property
    def generation(self): ...
    @property
    def id(self): ...
    md5_hash: Incomplete
    @property
    def media_link(self): ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, value) -> None: ...
    @property
    def metageneration(self): ...
    @property
    def owner(self): ...
    @property
    def retention_expiration_time(self): ...
    @property
    def self_link(self): ...
    @property
    def size(self): ...
    @property
    def kms_key_name(self): ...
    @kms_key_name.setter
    def kms_key_name(self, value) -> None: ...
    storage_class: Incomplete
    temporary_hold: Incomplete
    @property
    def time_deleted(self): ...
    @property
    def time_created(self): ...
    @property
    def updated(self): ...
    @property
    def custom_time(self): ...
    @custom_time.setter
    def custom_time(self, value) -> None: ...
    @property
    def retention(self): ...
    @property
    def soft_delete_time(self): ...
    @property
    def hard_delete_time(self): ...

class Retention(dict):
    def __init__(
        self,
        blob,
        mode: Incomplete | None = None,
        retain_until_time: Incomplete | None = None,
        retention_expiration_time: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def from_api_repr(cls, resource, blob): ...
    @property
    def blob(self): ...
    @property
    def mode(self): ...
    @mode.setter
    def mode(self, value) -> None: ...
    @property
    def retain_until_time(self): ...
    @retain_until_time.setter
    def retain_until_time(self, value) -> None: ...
    @property
    def retention_expiration_time(self): ...
