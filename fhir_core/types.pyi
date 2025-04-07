# mypy: ignore-errors

import abc
import dataclasses
import re
import typing

from _typeshed import Incomplete
from annotated_types import SLOTS, BaseMetadata, GroupedMetadata
from pydantic import GetCoreSchemaHandler
from pydantic.types import UUID4
from pydantic_core import core_schema

from .constraints import TYPES_ID_MAX_LENGTH, TYPES_STRING_ALLOW_EMPTY_STR
from .fhirabstractmodel import FHIRAbstractModel

__all__ = [
    "FhirBase",
    "create_fhir_type",
    "create_fhir_element_or_resource_type",
    "BooleanType",
    "StringType",
    "Base64BinaryType",
    "CodeType",
    "IdType",
    "IntegerType",
    "Integer64Type",
    "DecimalType",
    "UnsignedIntType",
    "PositiveIntType",
    "CanonicalType",
    "UriType",
    "OidType",
    "UuidType",
    "UrlType",
    "MarkdownType",
    "XhtmlType",
    "DateType",
    "DateTimeType",
    "InstantType",
    "TimeType",
]

class FhirBase(metaclass=abc.ABCMeta):
    @classmethod
    def get_model_klass(cls) -> type[FHIRAbstractModel]: ...
    @classmethod
    def produce_inner_schema(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema | None: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type["FhirBase"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...
    @classmethod
    def fhir_model_validator(
        cls, value: str | bytes | dict | FHIRAbstractModel, model_klass: type[FHIRAbstractModel]
    ): ...
    def __hash__(self) -> int: ...

class FhirElementOrResourceBase(FhirBase):
    @classmethod
    def fhir_model_validator(
        cls, value: str | bytes | dict | FHIRAbstractModel, model_klass: type[FHIRAbstractModel]
    ): ...

@dataclasses.dataclass(frozen=True, **SLOTS)
class String(GroupedMetadata):
    allow_empty_str = TYPES_STRING_ALLOW_EMPTY_STR
    __visit_name__ = ...
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...

@dataclasses.dataclass(frozen=True, **SLOTS)
class Base64Binary:
    __visit_name__ = ...
    regex = ...
    def __hash__(self) -> int: ...

@dataclasses.dataclass(frozen=True, **SLOTS)
class Code(GroupedMetadata):
    __visit_name__ = ...
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...
    def __hash__(self) -> int: ...

@dataclasses.dataclass(frozen=True, **SLOTS)
class Id(GroupedMetadata):
    pattern = ...
    min_length = ...
    max_length = TYPES_ID_MAX_LENGTH
    __visit_name__ = ...
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...

@dataclasses.dataclass(**SLOTS)
class Decimal:
    pattern = ...
    __visit_name__ = ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type["Decimal"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...
    def __hash__(self) -> int: ...

@dataclasses.dataclass(frozen=True, **SLOTS)
class Integer(GroupedMetadata):
    pattern = ...
    min_length: int = ...
    max_length: int = ...
    __visit_name__ = ...
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...

class Integer64(GroupedMetadata):
    pattern: Incomplete
    min_length: int
    max_length: int
    __visit_name__: str
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...

class UnsignedInt(Integer):
    regex: Incomplete
    __visit_name__: str
    min_length: int

class PositiveInt(UnsignedInt):
    regex: Incomplete
    __visit_name__: str
    min_length: int

@dataclasses.dataclass(frozen=True, **SLOTS)
class PatternConstraint(GroupedMetadata):
    pattern: re.Pattern
    def __iter__(self) -> typing.Iterator[BaseMetadata]: ...

class Uri(PatternConstraint):
    __visit_name__: str
    pattern: Incomplete

class Oid(PatternConstraint):
    __visit_name__: str
    pattern: Incomplete

class Uuid:
    __visit_name__: str

class Canonical(Uri):
    __visit_name__: str

@dataclasses.dataclass(frozen=True, **SLOTS)
class Url:
    path_pattern = ...
    __visit_name__ = ...
    @classmethod
    def produce_inner_schema(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema | None: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...

class Markdown(PatternConstraint):
    __visit_name__: str
    pattern: Incomplete

class Xhtml:
    __visit_name__: str

@dataclasses.dataclass(frozen=True, **SLOTS)
class Date:
    pattern = ...
    __visit_name__ = ...
    @classmethod
    def produce_inner_schema(cls): ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...

class DateTime(Date):
    pattern: Incomplete
    __visit_name__: str
    @classmethod
    def produce_inner_schema(cls): ...

class Instant(DateTime):
    pattern: Incomplete
    __visit_name__: str

@dataclasses.dataclass(frozen=True, **SLOTS)
class Time:
    pattern = ...
    __visit_name__ = ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: typing.Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...

BooleanType = bool
StringType: Incomplete
Base64BinaryType: Incomplete
CodeType: Incomplete
IdType: Incomplete
DecimalType: Incomplete
IntegerType: Incomplete
Integer64Type: Incomplete
UnsignedIntType: Incomplete
PositiveIntType: Incomplete
UriType: Incomplete
CanonicalType: Incomplete
OidType: Incomplete
UuidType = UUID4
UrlType: Incomplete
MarkdownType: Incomplete
XhtmlType: Incomplete
DateType: Incomplete
DateTimeType: Incomplete
InstantType: Incomplete
TimeType: Incomplete

def create_fhir_type(klass_name: str, model_klass: str) -> type[FhirBase]: ...
def create_fhir_element_or_resource_type(klass_name: str, model_klass: str) -> type[FhirBase]: ...
