import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from _typeshed import Incomplete

class DatasetRunItem(pydantic_v1.BaseModel):
    id: str
    dataset_run_id: str
    dataset_run_name: str
    dataset_item_id: str
    trace_id: str
    observation_id: str | None
    created_at: dt.datetime
    updated_at: dt.datetime
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
