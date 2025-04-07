from _typeshed import Incomplete

from . import _api_module
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient

logger: Incomplete

class Operations(_api_module.BaseModule):
    def get(
        self, operation: types.GenerateVideosOperation, *, config: types.GetOperationConfigOrDict | None = None
    ) -> types.GenerateVideosOperation: ...

class AsyncOperations(_api_module.BaseModule):
    async def get(
        self, operation: types.GenerateVideosOperation, *, config: types.GetOperationConfigOrDict | None = None
    ) -> types.GenerateVideosOperation: ...
