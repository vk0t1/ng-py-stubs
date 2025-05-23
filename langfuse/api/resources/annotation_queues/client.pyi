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
from .types.annotation_queue import AnnotationQueue as AnnotationQueue
from .types.annotation_queue_item import AnnotationQueueItem as AnnotationQueueItem
from .types.annotation_queue_status import AnnotationQueueStatus as AnnotationQueueStatus
from .types.create_annotation_queue_item_request import CreateAnnotationQueueItemRequest as CreateAnnotationQueueItemRequest
from .types.delete_annotation_queue_item_response import DeleteAnnotationQueueItemResponse as DeleteAnnotationQueueItemResponse
from .types.paginated_annotation_queue_items import PaginatedAnnotationQueueItems as PaginatedAnnotationQueueItems
from .types.paginated_annotation_queues import PaginatedAnnotationQueues as PaginatedAnnotationQueues
from .types.update_annotation_queue_item_request import UpdateAnnotationQueueItemRequest as UpdateAnnotationQueueItemRequest
from _typeshed import Incomplete

OMIT: Incomplete

class AnnotationQueuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def list_queues(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedAnnotationQueues: ...
    def get_queue(self, queue_id: str, *, request_options: RequestOptions | None = None) -> AnnotationQueue: ...
    def list_queue_items(self, queue_id: str, *, status: AnnotationQueueStatus | None = None, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedAnnotationQueueItems: ...
    def get_queue_item(self, queue_id: str, item_id: str, *, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    def create_queue_item(self, queue_id: str, *, request: CreateAnnotationQueueItemRequest, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    def update_queue_item(self, queue_id: str, item_id: str, *, request: UpdateAnnotationQueueItemRequest, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    def delete_queue_item(self, queue_id: str, item_id: str, *, request_options: RequestOptions | None = None) -> DeleteAnnotationQueueItemResponse: ...

class AsyncAnnotationQueuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def list_queues(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedAnnotationQueues: ...
    async def get_queue(self, queue_id: str, *, request_options: RequestOptions | None = None) -> AnnotationQueue: ...
    async def list_queue_items(self, queue_id: str, *, status: AnnotationQueueStatus | None = None, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedAnnotationQueueItems: ...
    async def get_queue_item(self, queue_id: str, item_id: str, *, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    async def create_queue_item(self, queue_id: str, *, request: CreateAnnotationQueueItemRequest, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    async def update_queue_item(self, queue_id: str, item_id: str, *, request: UpdateAnnotationQueueItemRequest, request_options: RequestOptions | None = None) -> AnnotationQueueItem: ...
    async def delete_queue_item(self, queue_id: str, item_id: str, *, request_options: RequestOptions | None = None) -> DeleteAnnotationQueueItemResponse: ...
