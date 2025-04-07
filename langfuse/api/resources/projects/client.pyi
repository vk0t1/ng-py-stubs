from ...core.api_error import ApiError as ApiError
from ...core.client_wrapper import AsyncClientWrapper as AsyncClientWrapper, SyncClientWrapper as SyncClientWrapper
from ...core.pydantic_utilities import pydantic_v1 as pydantic_v1
from ...core.request_options import RequestOptions as RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError as AccessDeniedError
from ..commons.errors.error import Error as Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError as MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError as NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError as UnauthorizedError
from .types.projects import Projects as Projects

class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def get(self, *, request_options: RequestOptions | None = None) -> Projects: ...

class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def get(self, *, request_options: RequestOptions | None = None) -> Projects: ...
