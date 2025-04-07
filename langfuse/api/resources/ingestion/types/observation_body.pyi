import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.map_value import MapValue as MapValue
from ...commons.types.observation_level import ObservationLevel as ObservationLevel
from ...commons.types.usage import Usage as Usage
from .observation_type import ObservationType as ObservationType
from _typeshed import Incomplete

class ObservationBody(pydantic_v1.BaseModel):
    id: str | None
    trace_id: str | None
    type: ObservationType
    name: str | None
    start_time: dt.datetime | None
    end_time: dt.datetime | None
    completion_start_time: dt.datetime | None
    model: str | None
    model_parameters: dict[str, MapValue] | None
    input: typing.Any | None
    version: str | None
    metadata: typing.Any | None
    output: typing.Any | None
    usage: Usage | None
    level: ObservationLevel | None
    status_message: str | None
    parent_observation_id: str | None
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
