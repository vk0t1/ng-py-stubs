import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.create_score_value import CreateScoreValue as CreateScoreValue
from ...commons.types.score_data_type import ScoreDataType as ScoreDataType
from _typeshed import Incomplete

class CreateScoreRequest(pydantic_v1.BaseModel):
    id: str | None
    trace_id: str
    name: str
    value: CreateScoreValue
    observation_id: str | None
    comment: str | None
    environment: str | None
    data_type: ScoreDataType | None
    config_id: str | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
