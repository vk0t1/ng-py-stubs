import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from _typeshed import Incomplete

class Trace(pydantic_v1.BaseModel):
    id: str
    timestamp: dt.datetime
    name: str | None
    input: typing.Any | None
    output: typing.Any | None
    session_id: str | None
    release: str | None
    version: str | None
    user_id: str | None
    metadata: typing.Any | None
    tags: list[str] | None
    public: bool | None
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
