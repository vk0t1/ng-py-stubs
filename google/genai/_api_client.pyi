# mypy: ignore-errors

import io
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any, AsyncIterator

import google.auth.credentials
import httpx
from _typeshed import Incomplete
from google.auth.credentials import Credentials as Credentials
from google.auth.transport.requests import Request as Request

from . import _common
from . import errors as errors
from . import version as version
from .types import HttpOptions as HttpOptions
from .types import HttpOptionsDict as HttpOptionsDict
from .types import HttpOptionsOrDict as HttpOptionsOrDict

logger: Incomplete
CHUNK_SIZE: Incomplete

@dataclass
class HttpRequest:
    headers: dict[str, str]
    url: str
    method: str
    data: dict[str, object] | bytes
    timeout: float | None = ...

class BaseResponse(_common.BaseModel):
    http_headers: dict[str, str] | None
    json_payload: Any | None

class HttpResponse:
    status_code: int
    headers: Incomplete
    response_stream: Incomplete
    byte_stream: Incomplete
    def __init__(
        self,
        headers: dict[str, str] | httpx.Headers,
        response_stream: Any | str = None,
        byte_stream: Any | bytes = None,
    ) -> None: ...
    segment_iterator: Incomplete
    def __aiter__(self): ...
    async def __anext__(self): ...
    @property
    def json(self) -> Any: ...
    def segments(self) -> Generator[Incomplete, Incomplete]: ...
    async def async_segments(self) -> AsyncIterator[Any]: ...
    def byte_segments(self) -> Generator[Incomplete, Incomplete]: ...

class SyncHttpxClient(httpx.Client):
    def __init__(self, **kwargs: Any) -> None: ...
    def __del__(self) -> None: ...

class AsyncHttpxClient(httpx.AsyncClient):
    def __init__(self, **kwargs: Any) -> None: ...
    def __del__(self) -> None: ...

class BaseApiClient:
    vertexai: Incomplete
    project: Incomplete
    location: Incomplete
    api_key: Incomplete
    def __init__(
        self,
        vertexai: bool | None = None,
        api_key: str | None = None,
        credentials: google.auth.credentials.Credentials | None = None,
        project: str | None = None,
        location: str | None = None,
        http_options: HttpOptionsOrDict | None = None,
    ) -> None: ...
    def get_read_only_http_options(self) -> dict[str, Any]: ...
    def request(
        self,
        http_method: str,
        path: str,
        request_dict: dict[str, object],
        http_options: HttpOptionsOrDict | None = None,
    ): ...
    def request_streamed(
        self,
        http_method: str,
        path: str,
        request_dict: dict[str, object],
        http_options: HttpOptionsOrDict | None = None,
    ): ...
    async def async_request(
        self,
        http_method: str,
        path: str,
        request_dict: dict[str, object],
        http_options: HttpOptionsOrDict | None = None,
    ) -> dict[str, object]: ...
    async def async_request_streamed(
        self,
        http_method: str,
        path: str,
        request_dict: dict[str, object],
        http_options: HttpOptionsOrDict | None = None,
    ): ...
    def upload_file(self, file_path: str | io.IOBase, upload_url: str, upload_size: int) -> HttpResponse: ...
    def download_file(self, path: str, http_options): ...
    async def async_upload_file(
        self, file_path: str | io.IOBase, upload_url: str, upload_size: int
    ) -> HttpResponse: ...
    async def async_download_file(self, path: str, http_options): ...
