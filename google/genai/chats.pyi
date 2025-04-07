# mypy: ignore-errors

from typing import AsyncIterator, Awaitable

from . import types as types
from .models import AsyncModels as AsyncModels
from .models import Models as Models
from .types import Content as Content
from .types import ContentOrDict as ContentOrDict
from .types import GenerateContentConfigOrDict as GenerateContentConfigOrDict
from .types import GenerateContentResponse as GenerateContentResponse
from .types import Part as Part
from .types import PartUnionDict as PartUnionDict

class _BaseChat:
    def __init__(
        self, *, model: str, config: GenerateContentConfigOrDict | None = None, history: list[ContentOrDict]
    ) -> None: ...
    def record_history(
        self,
        user_input: Content,
        model_output: list[Content],
        automatic_function_calling_history: list[Content],
        is_valid: bool,
    ): ...
    def get_history(self, curated: bool = False) -> list[Content]: ...

class Chat(_BaseChat):
    def __init__(
        self,
        *,
        modules: Models,
        model: str,
        config: GenerateContentConfigOrDict | None = None,
        history: list[ContentOrDict],
    ) -> None: ...
    def send_message(
        self, message: list[PartUnionDict] | PartUnionDict, config: GenerateContentConfigOrDict | None = None
    ) -> GenerateContentResponse: ...
    def send_message_stream(
        self, message: list[PartUnionDict] | PartUnionDict, config: GenerateContentConfigOrDict | None = None
    ): ...

class Chats:
    def __init__(self, modules: Models) -> None: ...
    def create(
        self,
        *,
        model: str,
        config: GenerateContentConfigOrDict | None = None,
        history: list[ContentOrDict] | None = None,
    ) -> Chat: ...

class AsyncChat(_BaseChat):
    def __init__(
        self,
        *,
        modules: AsyncModels,
        model: str,
        config: GenerateContentConfigOrDict | None = None,
        history: list[ContentOrDict],
    ) -> None: ...
    async def send_message(
        self, message: list[PartUnionDict] | PartUnionDict, config: GenerateContentConfigOrDict | None = None
    ) -> GenerateContentResponse: ...
    async def send_message_stream(
        self, message: list[PartUnionDict] | PartUnionDict, config: GenerateContentConfigOrDict | None = None
    ) -> Awaitable[AsyncIterator[GenerateContentResponse]]: ...

class AsyncChats:
    def __init__(self, modules: AsyncModels) -> None: ...
    def create(
        self,
        *,
        model: str,
        config: GenerateContentConfigOrDict | None = None,
        history: list[ContentOrDict] | None = None,
    ) -> AsyncChat: ...
