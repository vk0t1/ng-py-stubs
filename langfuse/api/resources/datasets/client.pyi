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
from ..commons.types.dataset import Dataset as Dataset
from ..commons.types.dataset_run_with_items import DatasetRunWithItems as DatasetRunWithItems
from .types.create_dataset_request import CreateDatasetRequest as CreateDatasetRequest
from .types.delete_dataset_run_response import DeleteDatasetRunResponse as DeleteDatasetRunResponse
from .types.paginated_dataset_runs import PaginatedDatasetRuns as PaginatedDatasetRuns
from .types.paginated_datasets import PaginatedDatasets as PaginatedDatasets
from _typeshed import Incomplete

OMIT: Incomplete

class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper) -> None: ...
    def list(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasets: ...
    def get(self, dataset_name: str, *, request_options: RequestOptions | None = None) -> Dataset: ...
    def create(self, *, request: CreateDatasetRequest, request_options: RequestOptions | None = None) -> Dataset: ...
    def get_run(self, dataset_name: str, run_name: str, *, request_options: RequestOptions | None = None) -> DatasetRunWithItems: ...
    def delete_run(self, dataset_name: str, run_name: str, *, request_options: RequestOptions | None = None) -> DeleteDatasetRunResponse: ...
    def get_runs(self, dataset_name: str, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasetRuns: ...

class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper) -> None: ...
    async def list(self, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasets: ...
    async def get(self, dataset_name: str, *, request_options: RequestOptions | None = None) -> Dataset: ...
    async def create(self, *, request: CreateDatasetRequest, request_options: RequestOptions | None = None) -> Dataset: ...
    async def get_run(self, dataset_name: str, run_name: str, *, request_options: RequestOptions | None = None) -> DatasetRunWithItems: ...
    async def delete_run(self, dataset_name: str, run_name: str, *, request_options: RequestOptions | None = None) -> DeleteDatasetRunResponse: ...
    async def get_runs(self, dataset_name: str, *, page: int | None = None, limit: int | None = None, request_options: RequestOptions | None = None) -> PaginatedDatasetRuns: ...
