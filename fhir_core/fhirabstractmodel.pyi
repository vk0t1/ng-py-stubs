# mypy: ignore-errors

import typing
from collections import OrderedDict

from _typeshed import Incomplete
from pydantic import BaseModel
from pydantic import SerializationInfo as SerializationInfo
from pydantic.fields import FieldInfo as FieldInfo
from pydantic.main import TupleGenerator as TupleGenerator
from pydantic_core import InitErrorDetails as InitErrorDetails
from typing_extensions import Self

from .constraints import HAS_XML_SUPPORT as HAS_XML_SUPPORT
from .constraints import HAS_YAML_SUPPORT as HAS_YAML_SUPPORT
from .utils import get_base64_encoder as get_base64_encoder
from .utils import is_primitive_type as is_primitive_type
from .xml_utils import xml_dumps as xml_dumps
from .xml_utils import xml_loads as xml_loads
from .yaml_utils import yaml_dumps as yaml_dumps
from .yaml_utils import yaml_loads as yaml_loads

logger: Incomplete
ROOT_KEY: str
FHIR_COMMENTS_FIELD_NAME: str
FHIRErrorCodes: Incomplete

class FHIRAbstractModel(BaseModel):
    __fhir_serialization_exclude_comment__: bool = False
    __resource_type__: str = "Resource"
    fhir_comments: str | list[str] | None = None
    def __init__(self, /, **data: typing.Any) -> None: ...
    @classmethod
    def element_properties(cls) -> typing.Generator[FieldInfo, None, None]: ...
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
    @classmethod
    def has_resource_base(cls) -> bool: ...
    @classmethod
    def get_resource_type(cls) -> str: ...
    @classmethod
    def get_alias_mapping(cls) -> dict[str, str]: ...
    @classmethod
    def get_json_encoder(cls) -> typing.Callable[[typing.Any], typing.Any]: ...
    def model_dump_json(
        self, *, indent: int | None = None, exclude_comments: bool = False, **pydantic_kwargs: typing.Any
    ) -> str: ...
    def model_dump_yaml(
        self, *, indent: int | None = None, exclude_comments: bool = False, **pydantic_kwargs: typing.Any
    ) -> str: ...
    def model_dump_xml(
        self,
        *,
        pretty_print: bool = False,
        xml_declaration: bool = True,
        exclude_comments: bool = False,
        **pydantic_kwargs: typing.Any,
    ) -> str: ...
    def model_dump(self, *, exclude_comments: bool = False, **pydantic_kwargs: typing.Any) -> dict[str, typing.Any]: ...
    def dict(self, *, exclude_comments: bool = False, **pydantic_kwargs: typing.Any) -> dict[str, typing.Any]: ...
    def json(
        self, *, indent: int | None = None, exclude_comments: bool = False, **pydantic_kwargs: typing.Any
    ) -> str: ...
    @classmethod
    def model_validate_yaml(
        cls, yaml_data: str | bytes | bytearray, *, strict: bool | None = None, context: typing.Any | None = None
    ) -> Self: ...
    @classmethod
    def model_validate_xml(
        cls, xml_data: str | bytes | bytearray, *, strict: bool | None = None, context: typing.Any | None = None
    ) -> Self: ...
    def fhir_model_serializer(
        self, serialize: typing.Callable[[typing.Any], typing.Any], info: SerializationInfo
    ) -> OrderedDict: ...
    def validate_after_model_construction(self) -> Self: ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
