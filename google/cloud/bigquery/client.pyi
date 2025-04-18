import datetime
from typing import IO, Any, Iterable, Mapping, Sequence

import google.api_core
import google.api_core.client_options
import requests
from _typeshed import Incomplete
from google import resumable_media as resumable_media
from google.api_core import page_iterator as page_iterator
from google.api_core import retry as retries
from google.api_core.iam import Policy as Policy
from google.auth.credentials import Credentials as Credentials
from google.cloud import exceptions as exceptions
from google.cloud.bigquery import enums as enums
from google.cloud.bigquery import job as job
from google.cloud.bigquery._helpers import TimeoutType as TimeoutType
from google.cloud.bigquery._http import Connection as Connection
from google.cloud.bigquery.dataset import Dataset as Dataset
from google.cloud.bigquery.dataset import DatasetListItem as DatasetListItem
from google.cloud.bigquery.dataset import DatasetReference as DatasetReference
from google.cloud.bigquery.enums import AutoRowIDs as AutoRowIDs
from google.cloud.bigquery.format_options import ParquetOptions as ParquetOptions
from google.cloud.bigquery.job import CopyJob as CopyJob
from google.cloud.bigquery.job import CopyJobConfig as CopyJobConfig
from google.cloud.bigquery.job import ExtractJob as ExtractJob
from google.cloud.bigquery.job import ExtractJobConfig as ExtractJobConfig
from google.cloud.bigquery.job import LoadJob as LoadJob
from google.cloud.bigquery.job import LoadJobConfig as LoadJobConfig
from google.cloud.bigquery.job import QueryJob as QueryJob
from google.cloud.bigquery.job import QueryJobConfig as QueryJobConfig
from google.cloud.bigquery.model import Model as Model
from google.cloud.bigquery.model import ModelReference as ModelReference
from google.cloud.bigquery.opentelemetry_tracing import create_span as create_span
from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT as DEFAULT_GET_JOB_TIMEOUT
from google.cloud.bigquery.retry import DEFAULT_JOB_RETRY as DEFAULT_JOB_RETRY
from google.cloud.bigquery.retry import DEFAULT_RETRY as DEFAULT_RETRY
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from google.cloud.bigquery.retry import POLLING_DEFAULT_VALUE as POLLING_DEFAULT_VALUE
from google.cloud.bigquery.routine import Routine as Routine
from google.cloud.bigquery.routine import RoutineReference as RoutineReference
from google.cloud.bigquery.schema import SchemaField as SchemaField
from google.cloud.bigquery.table import RowIterator as RowIterator
from google.cloud.bigquery.table import Table as Table
from google.cloud.bigquery.table import TableListItem as TableListItem
from google.cloud.bigquery.table import TableReference as TableReference
from google.cloud.client import ClientWithProject as ClientWithProject
from google.resumable_media.requests import MultipartUpload as MultipartUpload
from google.resumable_media.requests import ResumableUpload as ResumableUpload

pyarrow: Incomplete
pandas: Incomplete
ResumableTimeoutType = None | float | tuple[float, float]
PathType: Incomplete
TIMEOUT_HEADER: str

class Project:
    project_id: Incomplete
    numeric_id: Incomplete
    friendly_name: Incomplete
    def __init__(self, project_id, numeric_id, friendly_name) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...

class Client(ClientWithProject):
    SCOPE: Incomplete
    def __init__(
        self,
        project: str | None = None,
        credentials: Credentials | None = None,
        _http: requests.Session | None = None,
        location: str | None = None,
        default_query_job_config: QueryJobConfig | None = None,
        default_load_job_config: LoadJobConfig | None = None,
        client_info: google.api_core.client_info.ClientInfo | None = None,
        client_options: google.api_core.client_options.ClientOptions | dict[str, Any] | None = None,
    ) -> None: ...
    @property
    def location(self): ...
    @property
    def default_query_job_config(self) -> QueryJobConfig | None: ...
    @default_query_job_config.setter
    def default_query_job_config(self, value: QueryJobConfig | None): ...
    @property
    def default_load_job_config(self): ...
    @default_load_job_config.setter
    def default_load_job_config(self, value: LoadJobConfig): ...
    def close(self) -> None: ...
    def get_service_account_email(
        self, project: str | None = None, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> str: ...
    def list_projects(
        self,
        max_results: int | None = None,
        page_token: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def list_datasets(
        self,
        project: str | None = None,
        include_all: bool = False,
        filter: str | None = None,
        max_results: int | None = None,
        page_token: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def dataset(self, dataset_id: str, project: str | None = None) -> DatasetReference: ...
    def create_dataset(
        self,
        dataset: str | Dataset | DatasetReference | DatasetListItem,
        exists_ok: bool = False,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Dataset: ...
    def create_routine(
        self, routine: Routine, exists_ok: bool = False, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Routine: ...
    def create_table(
        self,
        table: str | Table | TableReference | TableListItem,
        exists_ok: bool = False,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Table: ...
    def get_dataset(
        self, dataset_ref: DatasetReference | str, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Dataset: ...
    def get_iam_policy(
        self,
        table: Table | TableReference | TableListItem | str,
        requested_policy_version: int = 1,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Policy: ...
    def set_iam_policy(
        self,
        table: Table | TableReference | TableListItem | str,
        policy: Policy,
        updateMask: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        *,
        fields: Sequence[str] = (),
    ) -> Policy: ...
    def test_iam_permissions(
        self,
        table: Table | TableReference | TableListItem | str,
        permissions: Sequence[str],
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> dict[str, Any]: ...
    def get_model(
        self, model_ref: ModelReference | str, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Model: ...
    def get_routine(
        self, routine_ref: Routine | RoutineReference | str, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Routine: ...
    def get_table(
        self,
        table: Table | TableReference | TableListItem | str,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Table: ...
    def update_dataset(
        self, dataset: Dataset, fields: Sequence[str], retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Dataset: ...
    def update_model(
        self, model: Model, fields: Sequence[str], retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Model: ...
    def update_routine(
        self, routine: Routine, fields: Sequence[str], retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Routine: ...
    def update_table(
        self, table: Table, fields: Sequence[str], retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> Table: ...
    def list_models(
        self,
        dataset: Dataset | DatasetReference | DatasetListItem | str,
        max_results: int | None = None,
        page_token: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def list_routines(
        self,
        dataset: Dataset | DatasetReference | DatasetListItem | str,
        max_results: int | None = None,
        page_token: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def list_tables(
        self,
        dataset: Dataset | DatasetReference | DatasetListItem | str,
        max_results: int | None = None,
        page_token: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def delete_dataset(
        self,
        dataset: Dataset | DatasetReference | DatasetListItem | str,
        delete_contents: bool = False,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        not_found_ok: bool = False,
    ) -> None: ...
    def delete_model(
        self,
        model: Model | ModelReference | str,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        not_found_ok: bool = False,
    ) -> None: ...
    def delete_job_metadata(
        self,
        job_id: str | LoadJob | CopyJob | ExtractJob | QueryJob,
        project: str | None = None,
        location: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        not_found_ok: bool = False,
    ): ...
    def delete_routine(
        self,
        routine: Routine | RoutineReference | str,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        not_found_ok: bool = False,
    ) -> None: ...
    def delete_table(
        self,
        table: Table | TableReference | TableListItem | str,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        not_found_ok: bool = False,
    ) -> None: ...
    def job_from_resource(
        self, resource: dict
    ) -> job.CopyJob | job.ExtractJob | job.LoadJob | job.QueryJob | job.UnknownJob: ...
    def create_job(
        self, job_config: dict, retry: retries.Retry = ..., timeout: TimeoutType = ...
    ) -> job.LoadJob | job.CopyJob | job.ExtractJob | job.QueryJob: ...
    def get_job(
        self,
        job_id: str | job.LoadJob | job.CopyJob | job.ExtractJob | job.QueryJob,
        project: str | None = None,
        location: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> job.LoadJob | job.CopyJob | job.ExtractJob | job.QueryJob | job.UnknownJob: ...
    def cancel_job(
        self,
        job_id: str,
        project: str | None = None,
        location: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> job.LoadJob | job.CopyJob | job.ExtractJob | job.QueryJob: ...
    def list_jobs(
        self,
        project: str | None = None,
        parent_job: QueryJob | str | None = None,
        max_results: int | None = None,
        page_token: str | None = None,
        all_users: bool | None = None,
        state_filter: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        min_creation_time: datetime.datetime | None = None,
        max_creation_time: datetime.datetime | None = None,
        page_size: int | None = None,
    ) -> page_iterator.Iterator: ...
    def load_table_from_uri(
        self,
        source_uris: str | Sequence[str],
        destination: Table | TableReference | TableListItem | str,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: LoadJobConfig | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> job.LoadJob: ...
    def load_table_from_file(
        self,
        file_obj: IO[bytes],
        destination: Table | TableReference | TableListItem | str,
        rewind: bool = False,
        size: int | None = None,
        num_retries: int = ...,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: LoadJobConfig | None = None,
        timeout: ResumableTimeoutType = ...,
    ) -> job.LoadJob: ...
    def load_table_from_dataframe(
        self,
        dataframe: pandas.DataFrame,
        destination: Table | TableReference | str,
        num_retries: int = ...,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: LoadJobConfig | None = None,
        parquet_compression: str = "snappy",
        timeout: ResumableTimeoutType = ...,
    ) -> job.LoadJob: ...
    def load_table_from_json(
        self,
        json_rows: Iterable[dict[str, Any]],
        destination: Table | TableReference | TableListItem | str,
        num_retries: int = ...,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: LoadJobConfig | None = None,
        timeout: ResumableTimeoutType = ...,
    ) -> job.LoadJob: ...
    def copy_table(
        self,
        sources: Table | TableReference | TableListItem | str | Sequence[Table | TableReference | TableListItem | str],
        destination: Table | TableReference | TableListItem | str,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: CopyJobConfig | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> job.CopyJob: ...
    def extract_table(
        self,
        source: Table | TableReference | TableListItem | Model | ModelReference | str,
        destination_uris: str | Sequence[str],
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        job_config: ExtractJobConfig | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        source_type: str = "Table",
    ) -> job.ExtractJob: ...
    def query(
        self,
        query: str,
        job_config: QueryJobConfig | None = None,
        job_id: str | None = None,
        job_id_prefix: str | None = None,
        location: str | None = None,
        project: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
        job_retry: retries.Retry = ...,
        api_method: str | enums.QueryApiMethod = ...,
    ) -> job.QueryJob: ...
    def query_and_wait(
        self,
        query,
        *,
        job_config: QueryJobConfig | None = None,
        location: str | None = None,
        project: str | None = None,
        api_timeout: TimeoutType = ...,
        wait_timeout: float | None | object = ...,
        retry: retries.Retry = ...,
        job_retry: retries.Retry = ...,
        page_size: int | None = None,
        max_results: int | None = None,
    ) -> RowIterator: ...
    def insert_rows(
        self,
        table: Table | TableReference | str,
        rows: Iterable[tuple] | Iterable[Mapping[str, Any]],
        selected_fields: Sequence[SchemaField] | None = None,
        **kwargs,
    ) -> Sequence[dict[str, Any]]: ...
    def insert_rows_from_dataframe(
        self,
        table: Table | TableReference | str,
        dataframe,
        selected_fields: Sequence[SchemaField] | None = None,
        chunk_size: int = 500,
        **kwargs: dict,
    ) -> Sequence[Sequence[dict]]: ...
    def insert_rows_json(
        self,
        table: Table | TableReference | TableListItem | str,
        json_rows: Sequence[Mapping[str, Any]],
        row_ids: Iterable[str | None] | AutoRowIDs | None = ...,
        skip_invalid_rows: bool | None = None,
        ignore_unknown_values: bool | None = None,
        template_suffix: str | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Sequence[dict]: ...
    def list_partitions(
        self,
        table: Table | TableReference | TableListItem | str,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> Sequence[str]: ...
    def list_rows(
        self,
        table: Table | TableListItem | TableReference | str,
        selected_fields: Sequence[SchemaField] | None = None,
        max_results: int | None = None,
        page_token: str | None = None,
        start_index: int | None = None,
        page_size: int | None = None,
        retry: retries.Retry = ...,
        timeout: TimeoutType = ...,
    ) -> RowIterator: ...
    def schema_from_json(self, file_or_path: PathType) -> list[SchemaField]: ...
    def schema_to_json(self, schema_list: Sequence[SchemaField], destination: PathType): ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
