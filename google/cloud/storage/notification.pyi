# mypy: ignore-errors

from _typeshed import Incomplete
from google.api_core.exceptions import NotFound as NotFound
from google.cloud.storage._opentelemetry_tracing import create_trace_span as create_trace_span
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY

OBJECT_FINALIZE_EVENT_TYPE: str
OBJECT_METADATA_UPDATE_EVENT_TYPE: str
OBJECT_DELETE_EVENT_TYPE: str
OBJECT_ARCHIVE_EVENT_TYPE: str
JSON_API_V1_PAYLOAD_FORMAT: str
NONE_PAYLOAD_FORMAT: str

class BucketNotification:
    def __init__(
        self,
        bucket,
        topic_name: Incomplete | None = None,
        topic_project: Incomplete | None = None,
        custom_attributes: Incomplete | None = None,
        event_types: Incomplete | None = None,
        blob_name_prefix: Incomplete | None = None,
        payload_format=...,
        notification_id: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def from_api_repr(cls, resource, bucket): ...
    @property
    def bucket(self): ...
    @property
    def topic_name(self): ...
    @property
    def topic_project(self): ...
    @property
    def custom_attributes(self): ...
    @property
    def event_types(self): ...
    @property
    def blob_name_prefix(self): ...
    @property
    def payload_format(self): ...
    @property
    def notification_id(self): ...
    @property
    def etag(self): ...
    @property
    def self_link(self): ...
    @property
    def client(self): ...
    @property
    def path(self): ...
    def create(self, client: Incomplete | None = None, timeout=..., retry: Incomplete | None = None) -> None: ...
    def exists(self, client: Incomplete | None = None, timeout=..., retry=...): ...
    def reload(self, client: Incomplete | None = None, timeout=..., retry=...) -> None: ...
    def delete(self, client: Incomplete | None = None, timeout=..., retry=...) -> None: ...
