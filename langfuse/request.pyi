# mypy: ignore-errors
import httpx
from _typeshed import Incomplete
from langfuse.serializer import EventSerializer as EventSerializer
from typing import Any

class LangfuseClient:
    def __init__(
        self, public_key: str, secret_key: str, base_url: str, version: str, timeout: int, session: httpx.Client
    ) -> None: ...
    def generate_headers(self): ...
    def batch_post(self, **kwargs) -> httpx.Response: ...
    def post(self, **kwargs) -> httpx.Response: ...

class APIError(Exception):
    message: Incomplete
    status: Incomplete
    details: Incomplete
    def __init__(self, status: int | str, message: str, details: Any = None) -> None: ...

class APIErrors(Exception):
    errors: Incomplete
    def __init__(self, errors: list[APIError]) -> None: ...
