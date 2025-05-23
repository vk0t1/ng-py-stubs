import datetime as dt
import typing
from ...core.api_error import ApiError as ApiError
from ...core.client_wrapper import AsyncClientWrapper as AsyncClientWrapper, SyncClientWrapper as SyncClientWrapper
from ...core.datetime_utils import serialize_datetime as serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder as jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1 as pydantic_v1
from ...core.request_options import RequestOptions as RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError as AccessDeniedError
from ..commons.errors.error import Error as Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError as MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError as NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError as UnauthorizedError
from ..commons.types.trace_with_full_details import TraceWithFullDetails as TraceWithFullDetails
from .types.delete_trace_response import DeleteTraceResponse as DeleteTraceResponse
from .types.traces import Traces as Traces
from _typeshed import Incomplete

OMIT: Incomplete

class TraceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def get(self, trace_id: str, *, request_options: RequestOptions | None = None) -> TraceWithFullDetails: ...
    def delete(self, trace_id: str, *, request_options: RequestOptions | None = None) -> DeleteTraceResponse: ...
    def list(self, *, page: int | None = None, limit: int | None = None, user_id: str | None = None, name: str | None = None, session_id: str | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, order_by: str | None = None, tags: str | typing.Sequence[str] | None = None, version: str | None = None, release: str | None = None, environment: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> Traces: ...
    def delete_multiple(self, *, trace_ids: typing.Sequence[str], request_options: RequestOptions | None = None) -> DeleteTraceResponse: ...

class AsyncTraceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def get(self, trace_id: str, *, request_options: RequestOptions | None = None) -> TraceWithFullDetails: ...
    async def delete(self, trace_id: str, *, request_options: RequestOptions | None = None) -> DeleteTraceResponse: ...
    async def list(self, *, page: int | None = None, limit: int | None = None, user_id: str | None = None, name: str | None = None, session_id: str | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, order_by: str | None = None, tags: str | typing.Sequence[str] | None = None, version: str | None = None, release: str | None = None, environment: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> Traces: ...
    async def delete_multiple(self, *, trace_ids: typing.Sequence[str], request_options: RequestOptions | None = None) -> DeleteTraceResponse: ...
