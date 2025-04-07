import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .chat_message import ChatMessage as ChatMessage
from _typeshed import Incomplete

class Prompt_Chat(pydantic_v1.BaseModel):
    prompt: list[ChatMessage]
    name: str
    version: int
    config: typing.Any
    labels: list[str]
    tags: list[str]
    commit_message: str | None
    resolution_graph: dict[str, typing.Any] | None
    type: typing.Literal['chat']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete

class Prompt_Text(pydantic_v1.BaseModel):
    prompt: str
    name: str
    version: int
    config: typing.Any
    labels: list[str]
    tags: list[str]
    commit_message: str | None
    resolution_graph: dict[str, typing.Any] | None
    type: typing.Literal['text']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
Prompt = Prompt_Chat | Prompt_Text
