# mypy: ignore-errors

import typing

from pydantic.fields import FieldInfo

__all__ = ["is_primitive_type", "get_fhir_type_name", "is_list_type", "get_base64_encoder"]

def is_primitive_type(field: FieldInfo) -> bool: ...
def is_list_type(field: FieldInfo) -> bool: ...
def get_fhir_type_name(field: FieldInfo): ...
def get_base64_encoder(field_info: FieldInfo) -> typing.Any: ...
