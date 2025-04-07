import datetime as dt
import typing
from ...core.api_error import ApiError as ApiError
from ...core.client_wrapper import AsyncClientWrapper as AsyncClientWrapper, SyncClientWrapper as SyncClientWrapper
from ...core.datetime_utils import serialize_datetime as serialize_datetime
from ...core.pydantic_utilities import pydantic_v1 as pydantic_v1
from ...core.request_options import RequestOptions as RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError as AccessDeniedError
from ..commons.errors.error import Error as Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError as MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError as NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError as UnauthorizedError
from .types.daily_metrics import DailyMetrics as DailyMetrics

class MetricsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def daily(self, *, page: int | None = None, limit: int | None = None, trace_name: str | None = None, user_id: str | None = None, tags: str | typing.Sequence[str] | None = None, environment: str | typing.Sequence[str] | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, request_options: RequestOptions | None = None) -> DailyMetrics: ...

class AsyncMetricsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def daily(self, *, page: int | None = None, limit: int | None = None, trace_name: str | None = None, user_id: str | None = None, tags: str | typing.Sequence[str] | None = None, environment: str | typing.Sequence[str] | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, request_options: RequestOptions | None = None) -> DailyMetrics: ...
