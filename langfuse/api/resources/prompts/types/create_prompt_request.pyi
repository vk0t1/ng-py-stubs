import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .chat_message import ChatMessage as ChatMessage
from _typeshed import Incomplete

class CreatePromptRequest_Chat(pydantic_v1.BaseModel):
    name: str
    prompt: list[ChatMessage]
    config: typing.Any | None
    labels: list[str] | None
    tags: list[str] | None
    commit_message: str | None
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

class CreatePromptRequest_Text(pydantic_v1.BaseModel):
    name: str
    prompt: str
    config: typing.Any | None
    labels: list[str] | None
    tags: list[str] | None
    commit_message: str | None
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
CreatePromptRequest = CreatePromptRequest_Chat | CreatePromptRequest_Text
