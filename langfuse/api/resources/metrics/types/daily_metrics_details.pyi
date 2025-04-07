import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .usage_by_model import UsageByModel as UsageByModel
from _typeshed import Incomplete

class DailyMetricsDetails(pydantic_v1.BaseModel):
    date: dt.date
    count_traces: int
    count_observations: int
    total_cost: float
    usage: list[UsageByModel]
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
