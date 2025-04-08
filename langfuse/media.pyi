from langfuse.api import MediaContentType as MediaContentType
from langfuse.types import ParsedMediaReference as ParsedMediaReference
from typing import Any, Literal, TypeVar

T = TypeVar('T')

class LangfuseMedia:
    obj: object
    def __init__(self, *, obj: object | None = None, base64_data_uri: str | None = None, content_type: MediaContentType | str | None = None, content_bytes: bytes | None = None, file_path: str | None = None) -> None: ...
    @staticmethod
    def parse_reference_string(reference_string: str) -> ParsedMediaReference: ...
    @staticmethod
    def resolve_media_references(*, obj: T, langfuse_client: Any, resolve_with: Literal['base64_data_uri'], max_depth: int = 10, content_fetch_timeout_seconds: int = 10) -> T: ...
