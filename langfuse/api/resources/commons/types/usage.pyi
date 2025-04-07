import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .model_usage_unit import ModelUsageUnit as ModelUsageUnit
from _typeshed import Incomplete

class Usage(pydantic_v1.BaseModel):
    input: int | None
    output: int | None
    total: int | None
    unit: ModelUsageUnit | None
    input_cost: float | None
    output_cost: float | None
    total_cost: float | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
