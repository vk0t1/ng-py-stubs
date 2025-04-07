import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .dataset_status import DatasetStatus as DatasetStatus
from _typeshed import Incomplete

class DatasetItem(pydantic_v1.BaseModel):
    id: str
    status: DatasetStatus
    input: typing.Any | None
    expected_output: typing.Any | None
    metadata: typing.Any | None
    source_trace_id: str | None
    source_observation_id: str | None
    dataset_id: str
    dataset_name: str
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
