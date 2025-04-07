import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.config_category import ConfigCategory as ConfigCategory
from ...commons.types.score_data_type import ScoreDataType as ScoreDataType
from _typeshed import Incomplete

class CreateScoreConfigRequest(pydantic_v1.BaseModel):
    name: str
    data_type: ScoreDataType
    categories: list[ConfigCategory] | None
    min_value: float | None
    max_value: float | None
    description: str | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
