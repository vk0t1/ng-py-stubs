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
from ..commons.types.comment import Comment as Comment
from .types.create_comment_request import CreateCommentRequest as CreateCommentRequest
from .types.create_comment_response import CreateCommentResponse as CreateCommentResponse
from .types.get_comments_response import GetCommentsResponse as GetCommentsResponse
from _typeshed import Incomplete

OMIT: Incomplete

class CommentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def create(self, *, request: CreateCommentRequest, request_options: RequestOptions | None = None) -> CreateCommentResponse: ...
    def get(self, *, page: int | None = None, limit: int | None = None, object_type: str | None = None, object_id: str | None = None, author_user_id: str | None = None, request_options: RequestOptions | None = None) -> GetCommentsResponse: ...
    def get_by_id(self, comment_id: str, *, request_options: RequestOptions | None = None) -> Comment: ...

class AsyncCommentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def create(self, *, request: CreateCommentRequest, request_options: RequestOptions | None = None) -> CreateCommentResponse: ...
    async def get(self, *, page: int | None = None, limit: int | None = None, object_type: str | None = None, object_id: str | None = None, author_user_id: str | None = None, request_options: RequestOptions | None = None) -> GetCommentsResponse: ...
    async def get_by_id(self, comment_id: str, *, request_options: RequestOptions | None = None) -> Comment: ...
