# mypy: ignore-errors

from typing import Any

import httpx
from _typeshed import Incomplete

from .replay_api_client import ReplayResponse as ReplayResponse

class APIError(Exception):
    code: int
    response: ReplayResponse | httpx.Response
    status: str | None
    message: str | None
    details: Incomplete
    def __init__(
        self, code: int, response_json: Any, response: ReplayResponse | httpx.Response | None = None
    ) -> None: ...
    @classmethod
    def raise_for_response(cls, response: ReplayResponse | httpx.Response): ...
    @classmethod
    async def raise_for_async_response(cls, response: ReplayResponse | httpx.Response): ...

class ClientError(APIError): ...
class ServerError(APIError): ...
class UnknownFunctionCallArgumentError(ValueError): ...
class UnsupportedFunctionError(ValueError): ...
class FunctionInvocationError(ValueError): ...
class ExperimentalWarning(Warning): ...
