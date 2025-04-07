import typing
from typing import Any, Iterable

import geopandas
import pandas
import pyarrow
from _typeshed import Incomplete
from google.api_core import exceptions as exceptions
from google.api_core import retry as retries
from google.cloud import bigquery_storage as bigquery_storage
from google.cloud.bigquery._tqdm_helpers import wait_for_query as wait_for_query
from google.cloud.bigquery.client import Client as Client
from google.cloud.bigquery.dataset import Dataset as Dataset
from google.cloud.bigquery.dataset import DatasetListItem as DatasetListItem
from google.cloud.bigquery.dataset import DatasetReference as DatasetReference
from google.cloud.bigquery.encryption_configuration import EncryptionConfiguration as EncryptionConfiguration
from google.cloud.bigquery.enums import DefaultPandasDTypes as DefaultPandasDTypes
from google.cloud.bigquery.enums import KeyResultStatementKind as KeyResultStatementKind
from google.cloud.bigquery.external_config import ExternalConfig as ExternalConfig
from google.cloud.bigquery.job.base import _AsyncJob, _JobConfig
from google.cloud.bigquery.query import ArrayQueryParameter as ArrayQueryParameter
from google.cloud.bigquery.query import ConnectionProperty as ConnectionProperty
from google.cloud.bigquery.query import ScalarQueryParameter as ScalarQueryParameter
from google.cloud.bigquery.query import StructQueryParameter as StructQueryParameter
from google.cloud.bigquery.query import UDFResource as UDFResource
from google.cloud.bigquery.retry import DEFAULT_JOB_RETRY as DEFAULT_JOB_RETRY
from google.cloud.bigquery.retry import DEFAULT_RETRY as DEFAULT_RETRY
from google.cloud.bigquery.retry import POLLING_DEFAULT_VALUE as POLLING_DEFAULT_VALUE
from google.cloud.bigquery.routine import RoutineReference as RoutineReference
from google.cloud.bigquery.schema import SchemaField as SchemaField
from google.cloud.bigquery.table import RangePartitioning as RangePartitioning
from google.cloud.bigquery.table import RowIterator as RowIterator
from google.cloud.bigquery.table import TableReference as TableReference
from google.cloud.bigquery.table import TimePartitioning as TimePartitioning
from google.cloud.bigquery.table import _EmptyRowIterator

class BiEngineReason(typing.NamedTuple):
    code: str = ...
    reason: str = ...
    @classmethod
    def from_api_repr(cls, reason: dict[str, str]) -> BiEngineReason: ...

class BiEngineStats(typing.NamedTuple):
    mode: str = ...
    reasons: list[BiEngineReason] = ...
    @classmethod
    def from_api_repr(cls, stats: dict[str, Any]) -> BiEngineStats: ...

class DmlStats(typing.NamedTuple):
    inserted_row_count: int = ...
    deleted_row_count: int = ...
    updated_row_count: int = ...
    @classmethod
    def from_api_repr(cls, stats: dict[str, str]) -> DmlStats: ...

class IndexUnusedReason(typing.NamedTuple):
    code: str | None = ...
    message: str | None = ...
    baseTable: TableReference | None = ...
    indexName: str | None = ...
    @classmethod
    def from_api_repr(cls, reason): ...

class SearchStats(typing.NamedTuple):
    mode: str | None = ...
    reason: list[IndexUnusedReason] = ...
    @classmethod
    def from_api_repr(cls, stats: dict[str, Any]): ...

class ScriptOptions:
    def __init__(
        self,
        statement_timeout_ms: int | None = None,
        statement_byte_budget: int | None = None,
        key_result_statement: KeyResultStatementKind | None = None,
    ) -> None: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, Any]) -> ScriptOptions: ...
    def to_api_repr(self) -> dict[str, Any]: ...
    @property
    def statement_timeout_ms(self) -> int | None: ...
    @statement_timeout_ms.setter
    def statement_timeout_ms(self, value: int | None): ...
    @property
    def statement_byte_budget(self) -> int | None: ...
    @statement_byte_budget.setter
    def statement_byte_budget(self, value: int | None): ...
    @property
    def key_result_statement(self) -> KeyResultStatementKind | None: ...
    @key_result_statement.setter
    def key_result_statement(self, value: KeyResultStatementKind | None): ...

class QueryJobConfig(_JobConfig):
    def __init__(self, **kwargs) -> None: ...
    @property
    def destination_encryption_configuration(self): ...
    @destination_encryption_configuration.setter
    def destination_encryption_configuration(self, value) -> None: ...
    @property
    def allow_large_results(self): ...
    @allow_large_results.setter
    def allow_large_results(self, value) -> None: ...
    @property
    def connection_properties(self) -> list[ConnectionProperty]: ...
    @connection_properties.setter
    def connection_properties(self, value: Iterable[ConnectionProperty]): ...
    @property
    def create_disposition(self): ...
    @create_disposition.setter
    def create_disposition(self, value) -> None: ...
    @property
    def create_session(self) -> bool | None: ...
    @create_session.setter
    def create_session(self, value: bool | None): ...
    @property
    def default_dataset(self): ...
    @default_dataset.setter
    def default_dataset(self, value) -> None: ...
    @property
    def destination(self): ...
    @destination.setter
    def destination(self, value) -> None: ...
    @property
    def dry_run(self): ...
    @dry_run.setter
    def dry_run(self, value) -> None: ...
    @property
    def flatten_results(self): ...
    @flatten_results.setter
    def flatten_results(self, value) -> None: ...
    @property
    def maximum_billing_tier(self): ...
    @maximum_billing_tier.setter
    def maximum_billing_tier(self, value) -> None: ...
    @property
    def maximum_bytes_billed(self): ...
    @maximum_bytes_billed.setter
    def maximum_bytes_billed(self, value) -> None: ...
    @property
    def priority(self): ...
    @priority.setter
    def priority(self, value) -> None: ...
    @property
    def query_parameters(self): ...
    @query_parameters.setter
    def query_parameters(self, values) -> None: ...
    @property
    def range_partitioning(self): ...
    @range_partitioning.setter
    def range_partitioning(self, value) -> None: ...
    @property
    def udf_resources(self): ...
    @udf_resources.setter
    def udf_resources(self, values) -> None: ...
    @property
    def use_legacy_sql(self): ...
    @use_legacy_sql.setter
    def use_legacy_sql(self, value) -> None: ...
    @property
    def use_query_cache(self): ...
    @use_query_cache.setter
    def use_query_cache(self, value) -> None: ...
    @property
    def write_disposition(self): ...
    @write_disposition.setter
    def write_disposition(self, value) -> None: ...
    @property
    def table_definitions(self): ...
    @table_definitions.setter
    def table_definitions(self, values) -> None: ...
    @property
    def time_partitioning(self): ...
    @time_partitioning.setter
    def time_partitioning(self, value) -> None: ...
    @property
    def clustering_fields(self): ...
    @clustering_fields.setter
    def clustering_fields(self, value) -> None: ...
    @property
    def schema_update_options(self): ...
    @schema_update_options.setter
    def schema_update_options(self, values) -> None: ...
    @property
    def script_options(self) -> ScriptOptions: ...
    @script_options.setter
    def script_options(self, value: ScriptOptions | None): ...
    def to_api_repr(self) -> dict: ...

class QueryJob(_AsyncJob):
    def __init__(self, job_id, query, client, job_config: Incomplete | None = None) -> None: ...
    @property
    def allow_large_results(self): ...
    @property
    def configuration(self) -> QueryJobConfig: ...
    @property
    def connection_properties(self) -> list[ConnectionProperty]: ...
    @property
    def create_disposition(self): ...
    @property
    def create_session(self) -> bool | None: ...
    @property
    def default_dataset(self): ...
    @property
    def destination(self): ...
    @property
    def destination_encryption_configuration(self): ...
    @property
    def dry_run(self): ...
    @property
    def flatten_results(self): ...
    @property
    def priority(self): ...
    @property
    def search_stats(self) -> SearchStats | None: ...
    @property
    def query(self): ...
    @property
    def query_id(self) -> str | None: ...
    @property
    def query_parameters(self): ...
    @property
    def udf_resources(self): ...
    @property
    def use_legacy_sql(self): ...
    @property
    def use_query_cache(self): ...
    @property
    def write_disposition(self): ...
    @property
    def maximum_billing_tier(self): ...
    @property
    def maximum_bytes_billed(self): ...
    @property
    def range_partitioning(self): ...
    @property
    def table_definitions(self): ...
    @property
    def time_partitioning(self): ...
    @property
    def clustering_fields(self): ...
    @property
    def schema_update_options(self): ...
    def to_api_repr(self): ...
    @classmethod
    def from_api_repr(cls, resource: dict, client: Client) -> QueryJob: ...
    @property
    def query_plan(self): ...
    @property
    def schema(self) -> list[SchemaField] | None: ...
    @property
    def timeline(self): ...
    @property
    def total_bytes_processed(self): ...
    @property
    def total_bytes_billed(self): ...
    @property
    def billing_tier(self): ...
    @property
    def cache_hit(self): ...
    @property
    def ddl_operation_performed(self): ...
    @property
    def ddl_target_routine(self): ...
    @property
    def ddl_target_table(self): ...
    @property
    def num_dml_affected_rows(self) -> int | None: ...
    @property
    def slot_millis(self): ...
    @property
    def statement_type(self): ...
    @property
    def referenced_tables(self): ...
    @property
    def undeclared_query_parameters(self): ...
    @property
    def estimated_bytes_processed(self): ...
    @property
    def dml_stats(self) -> DmlStats | None: ...
    @property
    def bi_engine_stats(self) -> BiEngineStats | None: ...
    def result(
        self,
        page_size: int | None = None,
        max_results: int | None = None,
        retry: retries.Retry | None = ...,
        timeout: float | object | None = ...,
        start_index: int | None = None,
        job_retry: retries.Retry | None = ...,
    ) -> RowIterator | _EmptyRowIterator: ...
    def to_arrow(
        self,
        progress_bar_type: str | None = None,
        bqstorage_client: bigquery_storage.BigQueryReadClient | None = None,
        create_bqstorage_client: bool = True,
        max_results: int | None = None,
    ) -> pyarrow.Table: ...
    def to_dataframe(
        self,
        bqstorage_client: bigquery_storage.BigQueryReadClient | None = None,
        dtypes: dict[str, Any] | None = None,
        progress_bar_type: str | None = None,
        create_bqstorage_client: bool = True,
        max_results: int | None = None,
        geography_as_object: bool = False,
        bool_dtype: Any | None = ...,
        int_dtype: Any | None = ...,
        float_dtype: Any | None = None,
        string_dtype: Any | None = None,
        date_dtype: Any | None = ...,
        datetime_dtype: Any | None = None,
        time_dtype: Any | None = ...,
        timestamp_dtype: Any | None = None,
        range_date_dtype: Any | None = ...,
        range_datetime_dtype: Any | None = ...,
        range_timestamp_dtype: Any | None = ...,
    ) -> pandas.DataFrame: ...
    def to_geodataframe(
        self,
        bqstorage_client: bigquery_storage.BigQueryReadClient | None = None,
        dtypes: dict[str, Any] | None = None,
        progress_bar_type: str | None = None,
        create_bqstorage_client: bool = True,
        max_results: int | None = None,
        geography_column: str | None = None,
    ) -> geopandas.GeoDataFrame: ...
    def __iter__(self): ...

class QueryPlanEntryStep:
    kind: Incomplete
    substeps: Incomplete
    def __init__(self, kind, substeps) -> None: ...
    @classmethod
    def from_api_repr(cls, resource: dict) -> QueryPlanEntryStep: ...
    def __eq__(self, other): ...

class QueryPlanEntry:
    def __init__(self) -> None: ...
    @classmethod
    def from_api_repr(cls, resource: dict) -> QueryPlanEntry: ...
    @property
    def name(self): ...
    @property
    def entry_id(self): ...
    @property
    def start(self): ...
    @property
    def end(self): ...
    @property
    def input_stages(self): ...
    @property
    def parallel_inputs(self): ...
    @property
    def completed_parallel_inputs(self): ...
    @property
    def wait_ms_avg(self): ...
    @property
    def wait_ms_max(self): ...
    @property
    def wait_ratio_avg(self): ...
    @property
    def wait_ratio_max(self): ...
    @property
    def read_ms_avg(self): ...
    @property
    def read_ms_max(self): ...
    @property
    def read_ratio_avg(self): ...
    @property
    def read_ratio_max(self): ...
    @property
    def compute_ms_avg(self): ...
    @property
    def compute_ms_max(self): ...
    @property
    def compute_ratio_avg(self): ...
    @property
    def compute_ratio_max(self): ...
    @property
    def write_ms_avg(self): ...
    @property
    def write_ms_max(self): ...
    @property
    def write_ratio_avg(self): ...
    @property
    def write_ratio_max(self): ...
    @property
    def records_read(self): ...
    @property
    def records_written(self): ...
    @property
    def status(self): ...
    @property
    def shuffle_output_bytes(self): ...
    @property
    def shuffle_output_bytes_spilled(self): ...
    @property
    def steps(self): ...
    @property
    def slot_ms(self): ...

class TimelineEntry:
    def __init__(self) -> None: ...
    @classmethod
    def from_api_repr(cls, resource): ...
    @property
    def elapsed_ms(self): ...
    @property
    def active_units(self): ...
    @property
    def pending_units(self): ...
    @property
    def completed_units(self): ...
    @property
    def slot_millis(self): ...
