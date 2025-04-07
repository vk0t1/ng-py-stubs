import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .score_source import ScoreSource as ScoreSource
from _typeshed import Incomplete

class Score_Numeric(pydantic_v1.BaseModel):
    value: float
    id: str
    trace_id: str
    name: str
    source: ScoreSource
    observation_id: str | None
    timestamp: dt.datetime
    created_at: dt.datetime
    updated_at: dt.datetime
    author_user_id: str | None
    comment: str | None
    config_id: str | None
    queue_id: str | None
    environment: str | None
    data_type: typing.Literal['NUMERIC']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete

class Score_Categorical(pydantic_v1.BaseModel):
    value: float | None
    string_value: str
    id: str
    trace_id: str
    name: str
    source: ScoreSource
    observation_id: str | None
    timestamp: dt.datetime
    created_at: dt.datetime
    updated_at: dt.datetime
    author_user_id: str | None
    comment: str | None
    config_id: str | None
    queue_id: str | None
    environment: str | None
    data_type: typing.Literal['CATEGORICAL']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete

class Score_Boolean(pydantic_v1.BaseModel):
    value: float
    string_value: str
    id: str
    trace_id: str
    name: str
    source: ScoreSource
    observation_id: str | None
    timestamp: dt.datetime
    created_at: dt.datetime
    updated_at: dt.datetime
    author_user_id: str | None
    comment: str | None
    config_id: str | None
    queue_id: str | None
    environment: str | None
    data_type: typing.Literal['BOOLEAN']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
Score = Score_Numeric | Score_Categorical | Score_Boolean
