from typing import Any

import packaging.version
from _typeshed import Incomplete
from google.cloud.bigquery import exceptions as exceptions

class PyarrowVersions:
    def __init__(self) -> None: ...
    @property
    def installed_version(self) -> packaging.version.Version: ...
    @property
    def use_compliant_nested_type(self) -> bool: ...
    def try_import(self, raise_if_error: bool = False) -> Any: ...

PYARROW_VERSIONS: Incomplete

class BQStorageVersions:
    def __init__(self) -> None: ...
    @property
    def installed_version(self) -> packaging.version.Version: ...
    @property
    def is_read_session_optional(self) -> bool: ...
    def try_import(self, raise_if_error: bool = False) -> Any: ...

BQ_STORAGE_VERSIONS: Incomplete

class PandasVersions:
    def __init__(self) -> None: ...
    @property
    def installed_version(self) -> packaging.version.Version: ...
    def try_import(self, raise_if_error: bool = False) -> Any: ...

PANDAS_VERSIONS: Incomplete
SUPPORTS_RANGE_PYARROW: Incomplete

def extract_runtime_version(): ...
