import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .model_usage_unit import ModelUsageUnit as ModelUsageUnit
from _typeshed import Incomplete

class Model(pydantic_v1.BaseModel):
    id: str
    model_name: str
    match_pattern: str
    start_date: dt.datetime | None
    unit: ModelUsageUnit | None
    input_price: float | None
    output_price: float | None
    total_price: float | None
    tokenizer_id: str | None
    tokenizer_config: typing.Any | None
    is_langfuse_managed: bool
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
