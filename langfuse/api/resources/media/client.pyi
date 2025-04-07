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
from .types.get_media_response import GetMediaResponse as GetMediaResponse
from .types.get_media_upload_url_request import GetMediaUploadUrlRequest as GetMediaUploadUrlRequest
from .types.get_media_upload_url_response import GetMediaUploadUrlResponse as GetMediaUploadUrlResponse
from .types.patch_media_body import PatchMediaBody as PatchMediaBody
from _typeshed import Incomplete

OMIT: Incomplete

class MediaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def get(self, media_id: str, *, request_options: RequestOptions | None = None) -> GetMediaResponse: ...
    def patch(self, media_id: str, *, request: PatchMediaBody, request_options: RequestOptions | None = None) -> None: ...
    def get_upload_url(self, *, request: GetMediaUploadUrlRequest, request_options: RequestOptions | None = None) -> GetMediaUploadUrlResponse: ...

class AsyncMediaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def get(self, media_id: str, *, request_options: RequestOptions | None = None) -> GetMediaResponse: ...
    async def patch(self, media_id: str, *, request: PatchMediaBody, request_options: RequestOptions | None = None) -> None: ...
    async def get_upload_url(self, *, request: GetMediaUploadUrlRequest, request_options: RequestOptions | None = None) -> GetMediaUploadUrlResponse: ...
