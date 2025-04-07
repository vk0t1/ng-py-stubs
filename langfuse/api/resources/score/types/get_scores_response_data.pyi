import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.score_source import ScoreSource as ScoreSource
from .get_scores_response_trace_data import GetScoresResponseTraceData as GetScoresResponseTraceData
from _typeshed import Incomplete

class GetScoresResponseData_Numeric(pydantic_v1.BaseModel):
    trace: GetScoresResponseTraceData
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

class GetScoresResponseData_Categorical(pydantic_v1.BaseModel):
    trace: GetScoresResponseTraceData
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

class GetScoresResponseData_Boolean(pydantic_v1.BaseModel):
    trace: GetScoresResponseTraceData
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
GetScoresResponseData = GetScoresResponseData_Numeric | GetScoresResponseData_Categorical | GetScoresResponseData_Boolean
