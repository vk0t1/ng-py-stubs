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
from ..commons.types.dataset_item import DatasetItem as DatasetItem
from .types.create_dataset_item_request import CreateDatasetItemRequest as CreateDatasetItemRequest
from .types.delete_dataset_item_response import DeleteDatasetItemResponse as DeleteDatasetItemResponse
from .types.paginated_dataset_items import PaginatedDatasetItems as PaginatedDatasetItems
from _typeshed import Incomplete

OMIT: Incomplete

class DatasetItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def create(self, *, request: CreateDatasetItemRequest, request_options: RequestOptions | None = None) -> DatasetItem: ...
    def get(self, id: str, *, request_options: RequestOptions | None = None) -> DatasetItem: ...
    def list(self, *, dataset_name: str | None = None, source_trace_id: str | None = None, source_observation_id: str | None = None, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasetItems: ...
    def delete(self, id: str, *, request_options: RequestOptions | None = None) -> DeleteDatasetItemResponse: ...

class AsyncDatasetItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def create(self, *, request: CreateDatasetItemRequest, request_options: RequestOptions | None = None) -> DatasetItem: ...
    async def get(self, id: str, *, request_options: RequestOptions | None = None) -> DatasetItem: ...
    async def list(self, *, dataset_name: str | None = None, source_trace_id: str | None = None, source_observation_id: str | None = None, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasetItems: ...
    async def delete(self, id: str, *, request_options: RequestOptions | None = None) -> DeleteDatasetItemResponse: ...
