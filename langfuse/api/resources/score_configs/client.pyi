from ...core.api_error import ApiError as ApiError
from ...core.client_wrapper import AsyncClientWrapper as AsyncClientWrapper, SyncClientWrapper as SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder as jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1 as pydantic_v1
from ...core.request_options import RequestOptions as RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError as AccessDeniedError
from ..commons.errors.error import Error as Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError as MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError as NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError as UnauthorizedError
from ..commons.types.score_config import ScoreConfig as ScoreConfig
from .types.create_score_config_request import CreateScoreConfigRequest as CreateScoreConfigRequest
from .types.score_configs import ScoreConfigs as ScoreConfigs
from _typeshed import Incomplete

OMIT: Incomplete

class ScoreConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def create(self, *, request: CreateScoreConfigRequest, request_options: RequestOptions | None = None) -> ScoreConfig: ...
    def get(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> ScoreConfigs: ...
    def get_by_id(self, config_id: str, *, request_options: RequestOptions | None = None) -> ScoreConfig: ...

class AsyncScoreConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def create(self, *, request: CreateScoreConfigRequest, request_options: RequestOptions | None = None) -> ScoreConfig: ...
    async def get(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> ScoreConfigs: ...
    async def get_by_id(self, config_id: str, *, request_options: RequestOptions | None = None) -> ScoreConfig: ...
