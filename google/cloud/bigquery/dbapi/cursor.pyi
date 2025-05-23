from typing import NamedTuple

from _typeshed import Incomplete
from google.cloud.bigquery import job as job
from google.cloud.bigquery.dbapi import exceptions as exceptions
from google.cloud.bigquery_storage import ArrowSerializationOptions as ArrowSerializationOptions

class Column(NamedTuple):
    name: Incomplete
    type_code: Incomplete
    display_size: Incomplete
    internal_size: Incomplete
    precision: Incomplete
    scale: Incomplete
    null_ok: Incomplete

class Cursor:
    connection: Incomplete
    description: Incomplete
    rowcount: int
    arraysize: Incomplete
    def __init__(self, connection) -> None: ...
    @property
    def query_job(self) -> job.QueryJob | None: ...
    def close(self) -> None: ...
    def execute(
        self,
        operation,
        parameters: Incomplete | None = None,
        job_id: Incomplete | None = None,
        job_config: Incomplete | None = None,
    ) -> None: ...
    def executemany(self, operation, seq_of_parameters) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def fetchall(self): ...
    def setinputsizes(self, sizes) -> None: ...
    def setoutputsize(self, size, column: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
