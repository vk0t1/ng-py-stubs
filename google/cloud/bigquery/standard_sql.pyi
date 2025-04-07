from typing import Any, Iterable

from google.cloud.bigquery.enums import StandardSqlTypeNames as StandardSqlTypeNames

class StandardSqlDataType:
    def __init__(
        self,
        type_kind: StandardSqlTypeNames | None = ...,
        array_element_type: StandardSqlDataType | None = None,
        struct_type: StandardSqlStructType | None = None,
        range_element_type: StandardSqlDataType | None = None,
    ) -> None: ...
    @property
    def type_kind(self) -> StandardSqlTypeNames | None: ...
    @type_kind.setter
    def type_kind(self, value: StandardSqlTypeNames | None): ...
    @property
    def array_element_type(self) -> StandardSqlDataType | None: ...
    @array_element_type.setter
    def array_element_type(self, value: StandardSqlDataType | None): ...
    @property
    def struct_type(self) -> StandardSqlStructType | None: ...
    @struct_type.setter
    def struct_type(self, value: StandardSqlStructType | None): ...
    @property
    def range_element_type(self) -> StandardSqlDataType | None: ...
    @range_element_type.setter
    def range_element_type(self, value: StandardSqlDataType | None): ...
    def to_api_repr(self) -> dict[str, Any]: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, Any]): ...
    def __eq__(self, other): ...

class StandardSqlField:
    def __init__(self, name: str | None = None, type: StandardSqlDataType | None = None) -> None: ...
    @property
    def name(self) -> str | None: ...
    @name.setter
    def name(self, value: str | None): ...
    @property
    def type(self) -> StandardSqlDataType | None: ...
    @type.setter
    def type(self, value: StandardSqlDataType | None): ...
    def to_api_repr(self) -> dict[str, Any]: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, Any]): ...
    def __eq__(self, other): ...

class StandardSqlStructType:
    def __init__(self, fields: Iterable[StandardSqlField] | None = None) -> None: ...
    @property
    def fields(self) -> list[StandardSqlField]: ...
    @fields.setter
    def fields(self, value: Iterable[StandardSqlField]): ...
    def to_api_repr(self) -> dict[str, Any]: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, Any]) -> StandardSqlStructType: ...
    def __eq__(self, other): ...

class StandardSqlTableType:
    def __init__(self, columns: Iterable[StandardSqlField]) -> None: ...
    @property
    def columns(self) -> list[StandardSqlField]: ...
    @columns.setter
    def columns(self, value: Iterable[StandardSqlField]): ...
    def to_api_repr(self) -> dict[str, Any]: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, Any]) -> StandardSqlTableType: ...
    def __eq__(self, other): ...
