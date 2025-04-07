import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.observation_level import ObservationLevel as ObservationLevel
from _typeshed import Incomplete

class OptionalObservationBody(pydantic_v1.BaseModel):
    trace_id: str | None
    name: str | None
    start_time: dt.datetime | None
    metadata: typing.Any | None
    input: typing.Any | None
    output: typing.Any | None
    level: ObservationLevel | None
    status_message: str | None
    parent_observation_id: str | None
    version: str | None
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
