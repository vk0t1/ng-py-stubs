# mypy: ignore-errors

from collections.abc import Generator

from _typeshed import Incomplete
from google.api_core import datetime_helpers as datetime_helpers
from google.api_core.iam import Policy as Policy
from google.cloud.exceptions import NotFound as NotFound
from google.cloud.storage._helpers import _PropertyMixin
from google.cloud.storage._opentelemetry_tracing import create_trace_span as create_trace_span
from google.cloud.storage._signing import (
    generate_signed_url_v2 as generate_signed_url_v2,
)
from google.cloud.storage._signing import (
    generate_signed_url_v4 as generate_signed_url_v4,
)
from google.cloud.storage.acl import BucketACL as BucketACL
from google.cloud.storage.acl import DefaultObjectACL as DefaultObjectACL
from google.cloud.storage.blob import Blob as Blob
from google.cloud.storage.constants import (
    ARCHIVE_STORAGE_CLASS as ARCHIVE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    COLDLINE_STORAGE_CLASS as COLDLINE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    DUAL_REGION_LOCATION_TYPE as DUAL_REGION_LOCATION_TYPE,
)
from google.cloud.storage.constants import (
    DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS as DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    MULTI_REGION_LOCATION_TYPE as MULTI_REGION_LOCATION_TYPE,
)
from google.cloud.storage.constants import (
    MULTI_REGIONAL_LEGACY_STORAGE_CLASS as MULTI_REGIONAL_LEGACY_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    NEARLINE_STORAGE_CLASS as NEARLINE_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    PUBLIC_ACCESS_PREVENTION_INHERITED as PUBLIC_ACCESS_PREVENTION_INHERITED,
)
from google.cloud.storage.constants import (
    REGION_LOCATION_TYPE as REGION_LOCATION_TYPE,
)
from google.cloud.storage.constants import (
    REGIONAL_LEGACY_STORAGE_CLASS as REGIONAL_LEGACY_STORAGE_CLASS,
)
from google.cloud.storage.constants import (
    STANDARD_STORAGE_CLASS as STANDARD_STORAGE_CLASS,
)
from google.cloud.storage.notification import (
    NONE_PAYLOAD_FORMAT as NONE_PAYLOAD_FORMAT,
)
from google.cloud.storage.notification import (
    BucketNotification as BucketNotification,
)
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
    DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED as DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
)

class LifecycleRuleConditions(dict):
    def __init__(
        self,
        age: Incomplete | None = None,
        created_before: Incomplete | None = None,
        is_live: Incomplete | None = None,
        matches_storage_class: Incomplete | None = None,
        number_of_newer_versions: Incomplete | None = None,
        days_since_custom_time: Incomplete | None = None,
        custom_time_before: Incomplete | None = None,
        days_since_noncurrent_time: Incomplete | None = None,
        noncurrent_time_before: Incomplete | None = None,
        matches_prefix: Incomplete | None = None,
        matches_suffix: Incomplete | None = None,
        _factory: bool = False,
    ) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...
    @property
    def age(self): ...
    @property
    def created_before(self): ...
    @property
    def is_live(self): ...
    @property
    def matches_prefix(self): ...
    @property
    def matches_storage_class(self): ...
    @property
    def matches_suffix(self): ...
    @property
    def number_of_newer_versions(self): ...
    @property
    def days_since_custom_time(self): ...
    @property
    def custom_time_before(self): ...
    @property
    def days_since_noncurrent_time(self): ...
    @property
    def noncurrent_time_before(self): ...

class LifecycleRuleDelete(dict):
    def __init__(self, **kw) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...

class LifecycleRuleSetStorageClass(dict):
    def __init__(self, storage_class, **kw) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...

class LifecycleRuleAbortIncompleteMultipartUpload(dict):
    def __init__(self, **kw) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...

class IAMConfiguration(dict):
    def __init__(
        self,
        bucket,
        public_access_prevention=...,
        uniform_bucket_level_access_enabled=...,
        uniform_bucket_level_access_locked_time=...,
        bucket_policy_only_enabled=...,
        bucket_policy_only_locked_time=...,
    ) -> None: ...
    @classmethod
    def from_api_repr(cls, resource, bucket): ...
    @property
    def bucket(self): ...
    @property
    def public_access_prevention(self): ...
    @public_access_prevention.setter
    def public_access_prevention(self, value) -> None: ...
    @property
    def uniform_bucket_level_access_enabled(self): ...
    @uniform_bucket_level_access_enabled.setter
    def uniform_bucket_level_access_enabled(self, value) -> None: ...
    @property
    def uniform_bucket_level_access_locked_time(self): ...
    @property
    def bucket_policy_only_enabled(self): ...
    @bucket_policy_only_enabled.setter
    def bucket_policy_only_enabled(self, value) -> None: ...
    @property
    def bucket_policy_only_locked_time(self): ...

class Bucket(_PropertyMixin):
    STORAGE_CLASSES: Incomplete
    def __init__(
        self,
        client,
        name: Incomplete | None = None,
        user_project: Incomplete | None = None,
        generation: Incomplete | None = None,
    ) -> None: ...
    @property
    def client(self): ...
    @property
    def rpo(self): ...
    @rpo.setter
    def rpo(self, value) -> None: ...
    @property
    def user_project(self): ...
    @property
    def generation(self): ...
    @property
    def soft_delete_time(self): ...
    @property
    def hard_delete_time(self): ...
    @classmethod
    def from_uri(cls, uri, client: Incomplete | None = None): ...
    @classmethod
    def from_string(cls, uri, client: Incomplete | None = None): ...
    def blob(
        self,
        blob_name: str,
        chunk_size: Incomplete | None = None,
        encryption_key: Incomplete | None = None,
        kms_key_name: Incomplete | None = None,
        generation: Incomplete | None = None,
    ) -> Blob: ...
    def notification(
        self,
        topic_name: Incomplete | None = None,
        topic_project: Incomplete | None = None,
        custom_attributes: Incomplete | None = None,
        event_types: Incomplete | None = None,
        blob_name_prefix: Incomplete | None = None,
        payload_format=...,
        notification_id: Incomplete | None = None,
    ): ...
    def exists(
        self,
        client: Incomplete | None = None,
        timeout=...,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ): ...
    def create(
        self,
        client: Incomplete | None = None,
        project: Incomplete | None = None,
        location: Incomplete | None = None,
        predefined_acl: Incomplete | None = None,
        predefined_default_object_acl: Incomplete | None = None,
        enable_object_retention: bool = False,
        timeout=...,
        retry=...,
    ) -> None: ...
    def update(
        self,
        client: Incomplete | None = None,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def reload(
        self,
        client: Incomplete | None = None,
        projection: str = "noAcl",
        timeout=...,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
        soft_deleted: Incomplete | None = None,
    ) -> None: ...
    def patch(
        self,
        client: Incomplete | None = None,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    @property
    def acl(self): ...
    @property
    def default_object_acl(self): ...
    @staticmethod
    def path_helper(bucket_name): ...
    @property
    def path(self): ...
    def get_blob(
        self,
        blob_name,
        client: Incomplete | None = None,
        encryption_key: Incomplete | None = None,
        generation: Incomplete | None = None,
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
        soft_deleted: Incomplete | None = None,
        **kwargs,
    ): ...
    def list_blobs(
        self,
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
        client: Incomplete | None = None,
        timeout=...,
        retry=...,
        match_glob: Incomplete | None = None,
        include_folders_as_prefixes: Incomplete | None = None,
        soft_deleted: Incomplete | None = None,
        page_size: Incomplete | None = None,
    ): ...
    def list_notifications(self, client: Incomplete | None = None, timeout=..., retry=...): ...
    def get_notification(self, notification_id, client: Incomplete | None = None, timeout=..., retry=...): ...
    def delete(
        self,
        force: bool = False,
        client: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ) -> None: ...
    def delete_blob(
        self,
        blob_name,
        client: Incomplete | None = None,
        generation: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ) -> None: ...
    def delete_blobs(
        self,
        blobs,
        on_error: Incomplete | None = None,
        client: Incomplete | None = None,
        preserve_generation: bool = False,
        timeout=...,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def copy_blob(
        self,
        blob,
        destination_bucket,
        new_name: Incomplete | None = None,
        client: Incomplete | None = None,
        preserve_acl: bool = True,
        source_generation: Incomplete | None = None,
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
    def rename_blob(
        self,
        blob,
        new_name,
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
    def move_blob(
        self,
        blob,
        new_name,
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
    def restore_blob(
        self,
        blob_name,
        client: Incomplete | None = None,
        generation: Incomplete | None = None,
        copy_source_acl: Incomplete | None = None,
        projection: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
    ): ...
    @property
    def cors(self): ...
    @cors.setter
    def cors(self, entries) -> None: ...
    default_event_based_hold: Incomplete
    @property
    def default_kms_key_name(self): ...
    @default_kms_key_name.setter
    def default_kms_key_name(self, value) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, mapping) -> None: ...
    @property
    def etag(self): ...
    @property
    def id(self): ...
    @property
    def iam_configuration(self): ...
    @property
    def soft_delete_policy(self): ...
    @property
    def lifecycle_rules(self) -> Generator[Incomplete]: ...
    @lifecycle_rules.setter
    def lifecycle_rules(self, rules) -> None: ...
    def clear_lifecycle_rules(self) -> None: ...
    def clear_lifecyle_rules(self): ...
    def add_lifecycle_delete_rule(self, **kw) -> None: ...
    def add_lifecycle_set_storage_class_rule(self, storage_class, **kw) -> None: ...
    def add_lifecycle_abort_incomplete_multipart_upload_rule(self, **kw) -> None: ...
    @property
    def location(self): ...
    @location.setter
    def location(self, value) -> None: ...
    @property
    def data_locations(self): ...
    @property
    def location_type(self): ...
    def get_logging(self): ...
    def enable_logging(self, bucket_name, object_prefix: str = "") -> None: ...
    def disable_logging(self) -> None: ...
    @property
    def metageneration(self): ...
    @property
    def owner(self): ...
    @property
    def project_number(self): ...
    @property
    def retention_policy_effective_time(self): ...
    @property
    def retention_policy_locked(self): ...
    @property
    def retention_period(self): ...
    @retention_period.setter
    def retention_period(self, value) -> None: ...
    @property
    def self_link(self): ...
    @property
    def storage_class(self): ...
    @storage_class.setter
    def storage_class(self, value) -> None: ...
    @property
    def time_created(self): ...
    @property
    def updated(self): ...
    @property
    def versioning_enabled(self): ...
    @versioning_enabled.setter
    def versioning_enabled(self, value) -> None: ...
    @property
    def requester_pays(self): ...
    @requester_pays.setter
    def requester_pays(self, value) -> None: ...
    @property
    def autoclass_enabled(self): ...
    @autoclass_enabled.setter
    def autoclass_enabled(self, value) -> None: ...
    @property
    def autoclass_toggle_time(self): ...
    @property
    def autoclass_terminal_storage_class(self): ...
    @autoclass_terminal_storage_class.setter
    def autoclass_terminal_storage_class(self, value) -> None: ...
    @property
    def autoclass_terminal_storage_class_update_time(self): ...
    @property
    def object_retention_mode(self): ...
    @property
    def hierarchical_namespace_enabled(self): ...
    @hierarchical_namespace_enabled.setter
    def hierarchical_namespace_enabled(self, value) -> None: ...
    def configure_website(
        self, main_page_suffix: Incomplete | None = None, not_found_page: Incomplete | None = None
    ) -> None: ...
    def disable_website(self): ...
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
        recursive: bool = False,
        future: bool = False,
        client: Incomplete | None = None,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def make_private(
        self,
        recursive: bool = False,
        future: bool = False,
        client: Incomplete | None = None,
        timeout=...,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    def generate_upload_policy(
        self, conditions, expiration: Incomplete | None = None, client: Incomplete | None = None
    ): ...
    def lock_retention_policy(self, client: Incomplete | None = None, timeout=..., retry=...) -> None: ...
    def generate_signed_url(
        self,
        expiration: Incomplete | None = None,
        api_access_endpoint: Incomplete | None = None,
        method: str = "GET",
        headers: Incomplete | None = None,
        query_parameters: Incomplete | None = None,
        client: Incomplete | None = None,
        credentials: Incomplete | None = None,
        version: Incomplete | None = None,
        virtual_hosted_style: bool = False,
        bucket_bound_hostname: Incomplete | None = None,
        scheme: str = "http",
    ): ...

class SoftDeletePolicy(dict):
    def __init__(self, bucket, **kw) -> None: ...
    @classmethod
    def from_api_repr(cls, resource, bucket): ...
    @property
    def bucket(self): ...
    @property
    def retention_duration_seconds(self): ...
    @retention_duration_seconds.setter
    def retention_duration_seconds(self, value) -> None: ...
    @property
    def effective_time(self): ...
