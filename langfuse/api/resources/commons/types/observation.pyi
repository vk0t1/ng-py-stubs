import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .map_value import MapValue as MapValue
from .observation_level import ObservationLevel as ObservationLevel
from .usage import Usage as Usage
from _typeshed import Incomplete

class Observation(pydantic_v1.BaseModel):
    id: str
    trace_id: str | None
    type: str
    name: str | None
    start_time: dt.datetime
    end_time: dt.datetime | None
    completion_start_time: dt.datetime | None
    model: str | None
    model_parameters: dict[str, MapValue] | None
    input: typing.Any | None
    version: str | None
    metadata: typing.Any | None
    output: typing.Any | None
    usage: Usage | None
    level: ObservationLevel
    status_message: str | None
    parent_observation_id: str | None
    prompt_id: str | None
    usage_details: dict[str, int] | None
    cost_details: dict[str, float] | None
    environment: str | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
