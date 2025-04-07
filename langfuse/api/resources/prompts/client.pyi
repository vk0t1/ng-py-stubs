import datetime as dt
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
from .types.create_prompt_request import CreatePromptRequest as CreatePromptRequest
from .types.prompt import Prompt as Prompt
from .types.prompt_meta_list_response import PromptMetaListResponse as PromptMetaListResponse
from _typeshed import Incomplete

OMIT: Incomplete

class PromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def get(self, prompt_name: str, *, version: int | None = None, label: str | None = None, request_options: RequestOptions | None = None) -> Prompt: ...
    def list(self, *, name: str | None = None, label: str | None = None, tag: str | None = None, page: int | None = None, limit: int | None = None, from_updated_at: dt.datetime | None = None, to_updated_at: dt.datetime | None = None, request_options: RequestOptions | None = None) -> PromptMetaListResponse: ...
    def create(self, *, request: CreatePromptRequest, request_options: RequestOptions | None = None) -> Prompt: ...

class AsyncPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def get(self, prompt_name: str, *, version: int | None = None, label: str | None = None, request_options: RequestOptions | None = None) -> Prompt: ...
    async def list(self, *, name: str | None = None, label: str | None = None, tag: str | None = None, page: int | None = None, limit: int | None = None, from_updated_at: dt.datetime | None = None, to_updated_at: dt.datetime | None = None, request_options: RequestOptions | None = None) -> PromptMetaListResponse: ...
    async def create(self, *, request: CreatePromptRequest, request_options: RequestOptions | None = None) -> Prompt: ...
