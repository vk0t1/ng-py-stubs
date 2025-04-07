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
from ..commons.types.score import Score as Score
from ..commons.types.score_data_type import ScoreDataType as ScoreDataType
from ..commons.types.score_source import ScoreSource as ScoreSource
from .types.create_score_request import CreateScoreRequest as CreateScoreRequest
from .types.create_score_response import CreateScoreResponse as CreateScoreResponse
from .types.get_scores_response import GetScoresResponse as GetScoresResponse
from _typeshed import Incomplete

OMIT: Incomplete

class ScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def create(self, *, request: CreateScoreRequest, request_options: RequestOptions | None = None) -> CreateScoreResponse: ...
    def get(self, *, page: int | None = None, limit: int | None = None, user_id: str | None = None, name: str | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, environment: str | typing.Sequence[str] | None = None, source: ScoreSource | None = None, operator: str | None = None, value: float | None = None, score_ids: str | None = None, config_id: str | None = None, queue_id: str | None = None, data_type: ScoreDataType | None = None, trace_tags: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> GetScoresResponse: ...
    def get_by_id(self, score_id: str, *, request_options: RequestOptions | None = None) -> Score: ...
    def delete(self, score_id: str, *, request_options: RequestOptions | None = None) -> None: ...

class AsyncScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def create(self, *, request: CreateScoreRequest, request_options: RequestOptions | None = None) -> CreateScoreResponse: ...
    async def get(self, *, page: int | None = None, limit: int | None = None, user_id: str | None = None, name: str | None = None, from_timestamp: dt.datetime | None = None, to_timestamp: dt.datetime | None = None, environment: str | typing.Sequence[str] | None = None, source: ScoreSource | None = None, operator: str | None = None, value: float | None = None, score_ids: str | None = None, config_id: str | None = None, queue_id: str | None = None, data_type: ScoreDataType | None = None, trace_tags: str | typing.Sequence[str] | None = None, request_options: RequestOptions | None = None) -> GetScoresResponse: ...
    async def get_by_id(self, score_id: str, *, request_options: RequestOptions | None = None) -> Score: ...
    async def delete(self, score_id: str, *, request_options: RequestOptions | None = None) -> None: ...
