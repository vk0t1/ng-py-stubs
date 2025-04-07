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
from ..commons.types.session_with_traces import SessionWithTraces as SessionWithTraces
from .types.paginated_sessions import PaginatedSessions as PaginatedSessions

class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def list(self, *, page: int | None = None, limit: int | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, environment: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> PaginatedSessions: ...
    def get(self, session_id: str, *, request_options: RequestOptions | None = None) -> SessionWithTraces: ...

class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def list(self, *, page: int | None = None, limit: int | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, environment: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> PaginatedSessions: ...
    async def get(self, session_id: str, *, request_options: RequestOptions | None = None) -> SessionWithTraces: ...
