import typing

from _typeshed import Incomplete

from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts
from ....core.pydantic_utilities import pydantic_v1 as pydantic_v1
from ...commons.types.trace_with_details import TraceWithDetails as TraceWithDetails
from ...utils.resources.pagination.types.meta_response import MetaResponse as MetaResponse

class Traces(pydantic_v1.BaseModel):
    data: list[TraceWithDetails]
    meta: MetaResponse
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete
