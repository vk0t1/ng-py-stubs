from .datetime_utils import serialize_datetime as serialize_datetime
from .pydantic_utilities import pydantic_v1 as pydantic_v1
from _typeshed import Incomplete
from typing import Any, Callable

SetIntStr = set[int | str]
DictIntStrAny = dict[int | str, Any]

def generate_encoders_by_class_tuples(type_encoder_map: dict[Any, Callable[[Any], Any]]) -> dict[Callable[[Any], Any], tuple[Any, ...]]: ...

encoders_by_class_tuples: Incomplete

def jsonable_encoder(obj: Any, custom_encoder: dict[Any, Callable[[Any], Any]] | None = None) -> Any: ...
