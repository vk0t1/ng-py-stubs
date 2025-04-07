# mypy: ignore-errors

from typing import AsyncIterator, Sequence

from _typeshed import Incomplete
from websockets.client import ClientConnection as ClientConnection

from . import _api_module
from . import _transformers as t
from . import client as client
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient
from ._common import experimental_warning as experimental_warning

logger: Incomplete

class AsyncSession:
    def __init__(self, api_client: client.BaseApiClient, websocket: ClientConnection) -> None: ...
    async def send(
        self,
        *,
        input: types.ContentListUnion
        | types.ContentListUnionDict
        | types.LiveClientContentOrDict
        | types.LiveClientRealtimeInputOrDict
        | types.LiveClientToolResponseOrDict
        | types.FunctionResponseOrDict
        | Sequence[types.FunctionResponseOrDict]
        | None = None,
        end_of_turn: bool | None = False,
    ): ...
    async def send_client_content(
        self,
        *,
        turns: types.Content | types.ContentDict | list[types.Content | types.ContentDict] | None = None,
        turn_complete: bool = True,
    ): ...
    async def send_realtime_input(self, *, media: t.BlobUnion): ...
    async def send_tool_response(
        self, *, function_responses: types.FunctionResponseOrDict | Sequence[types.FunctionResponseOrDict]
    ): ...
    async def receive(self) -> AsyncIterator[types.LiveServerMessage]: ...
    async def start_stream(
        self, *, stream: AsyncIterator[bytes], mime_type: str
    ) -> AsyncIterator[types.LiveServerMessage]: ...
    async def close(self) -> None: ...

class AsyncLive(_api_module.BaseModule):
    async def connect(
        self, *, model: str, config: types.LiveConnectConfigOrDict | None = None
    ) -> AsyncIterator[AsyncSession]: ...
