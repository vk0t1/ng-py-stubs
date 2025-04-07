from collections.abc import Generator
from typing import Any

from _typeshed import Incomplete
from google.cloud.bigquery import schema as schema
from google.cloud.bigquery_storage_v1.types import ArrowSerializationOptions as ArrowSerializationOptions

pandas_import_exception: Incomplete
pandas_import_exception = exc
pandas_gbq_import_exception: Incomplete
pandas_gbq_import_exception = exc
date_dtype_name: Incomplete
time_dtype_name: Incomplete
db_dtypes_import_exception: Incomplete
db_dtypes_import_exception = exc
pyarrow: Incomplete

class _DownloadState:
    done: bool
    started_workers: int
    finished_workers: int
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...

BQ_FIELD_TYPE_TO_ARROW_FIELD_METADATA: Incomplete

def bq_to_arrow_struct_data_type(field): ...
def bq_to_arrow_range_data_type(field): ...
def bq_to_arrow_data_type(field): ...
def bq_to_arrow_field(bq_field, array_type: Incomplete | None = None): ...
def bq_to_arrow_schema(bq_schema): ...
def default_types_mapper(
    date_as_object: bool = False,
    bool_dtype: Any | None = None,
    int_dtype: Any | None = None,
    float_dtype: Any | None = None,
    string_dtype: Any | None = None,
    date_dtype: Any | None = None,
    datetime_dtype: Any | None = None,
    time_dtype: Any | None = None,
    timestamp_dtype: Any | None = None,
    range_date_dtype: Any | None = None,
    range_datetime_dtype: Any | None = None,
    range_timestamp_dtype: Any | None = None,
): ...
def bq_to_arrow_array(series, bq_field): ...
def get_column_or_index(dataframe, name): ...
def list_columns_and_indexes(dataframe): ...
def dataframe_to_bq_schema(dataframe, bq_schema): ...
def augment_schema(dataframe, current_bq_schema): ...
def dataframe_to_arrow(dataframe, bq_schema): ...
def dataframe_to_parquet(
    dataframe, bq_schema, filepath, parquet_compression: str = "SNAPPY", parquet_use_compliant_nested_type: bool = True
) -> None: ...
def download_arrow_row_iterator(pages, bq_schema) -> Generator[Incomplete]: ...
def download_dataframe_row_iterator(pages, bq_schema, dtypes) -> Generator[Incomplete]: ...
def download_arrow_bqstorage(
    project_id,
    table,
    bqstorage_client,
    preserve_order: bool = False,
    selected_fields: Incomplete | None = None,
    max_queue_size=...,
    max_stream_count: Incomplete | None = None,
): ...
def download_dataframe_bqstorage(
    project_id,
    table,
    bqstorage_client,
    column_names,
    dtypes,
    preserve_order: bool = False,
    selected_fields: Incomplete | None = None,
    max_queue_size=...,
    max_stream_count: Incomplete | None = None,
): ...
def dataframe_to_json_generator(dataframe) -> Generator[Incomplete]: ...
def verify_pandas_imports() -> None: ...
def determine_requested_streams(preserve_order: bool, max_stream_count: int | None) -> int: ...
