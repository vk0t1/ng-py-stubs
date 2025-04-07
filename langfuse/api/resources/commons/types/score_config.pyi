import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .config_category import ConfigCategory as ConfigCategory
from .score_data_type import ScoreDataType as ScoreDataType
from _typeshed import Incomplete

class ScoreConfig(pydantic_v1.BaseModel):
    id: str
    name: str
    created_at: dt.datetime
    updated_at: dt.datetime
    project_id: str
    data_type: ScoreDataType
    is_archived: bool
    min_value: float | None
    max_value: float | None
    categories: list[ConfigCategory] | None
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
