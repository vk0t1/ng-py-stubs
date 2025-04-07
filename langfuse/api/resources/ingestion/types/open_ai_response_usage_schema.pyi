import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from _typeshed import Incomplete

class OpenAiResponseUsageSchema(pydantic_v1.BaseModel):
    input_tokens: int
    output_tokens: int
    total_tokens: int
    input_tokens_details: dict[str, int | None] | None
    output_tokens_details: dict[str, int | None] | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete
