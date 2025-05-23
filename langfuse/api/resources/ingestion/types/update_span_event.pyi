# mypy: ignore-errors

import typing

from _typeshed import Incomplete

from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import (
    deep_union_pydantic_dicts as deep_union_pydantic_dicts,
)
from ....core.pydantic_utilities import (
    pydantic_v1 as pydantic_v1,
)
from .base_event import BaseEvent as BaseEvent
from .update_span_body import UpdateSpanBody as UpdateSpanBody

class UpdateSpanEvent(BaseEvent):
    body: UpdateSpanBody
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
