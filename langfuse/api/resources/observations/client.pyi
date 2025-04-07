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
from ..commons.types.observations_view import ObservationsView as ObservationsView
from .types.observations_views import ObservationsViews as ObservationsViews

class ObservationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def get(self, observation_id: str, *, request_options: RequestOptions | None = None) -> ObservationsView: ...
    def get_many(self, *, page: int | None = None, limit: int | None = None, name: str | None = None, user_id: str | None = None, type: str | None = None, trace_id: str | None = None, parent_observation_id: str | None = None, environment: str | typing.Sequence[str] | None = None, from_start_time: dt.datetime | None = None, to_start_time: dt.datetime | None = None, version: str | None = None, request_options: RequestOptions | None = None) -> ObservationsViews: ...

class AsyncObservationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def get(self, observation_id: str, *, request_options: RequestOptions | None = None) -> ObservationsView: ...
    async def get_many(self, *, page: int | None = None, limit: int | None = None, name: str | None = None, user_id: str | None = None, type: str | None = None, trace_id: str | None = None, parent_observation_id: str | None = None, environment: str | typing.Sequence[str] | None = None, from_start_time: dt.datetime | None = None, to_start_time: dt.datetime | None = None, version: str | None = None, request_options: RequestOptions | None = None) -> ObservationsViews: ...
