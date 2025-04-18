from _typeshed import Incomplete

from . import _api_module
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient
from .pagers import AsyncPager as AsyncPager
from .pagers import Pager as Pager

logger: Incomplete

class Caches(_api_module.BaseModule):
    def create(
        self, *, model: str, config: types.CreateCachedContentConfigOrDict | None = None
    ) -> types.CachedContent: ...
    def get(self, *, name: str, config: types.GetCachedContentConfigOrDict | None = None) -> types.CachedContent: ...
    def delete(
        self, *, name: str, config: types.DeleteCachedContentConfigOrDict | None = None
    ) -> types.DeleteCachedContentResponse: ...
    def update(
        self, *, name: str, config: types.UpdateCachedContentConfigOrDict | None = None
    ) -> types.CachedContent: ...
    def list(self, *, config: types.ListCachedContentsConfigOrDict | None = None) -> Pager[types.CachedContent]: ...

class AsyncCaches(_api_module.BaseModule):
    async def create(
        self, *, model: str, config: types.CreateCachedContentConfigOrDict | None = None
    ) -> types.CachedContent: ...
    async def get(
        self, *, name: str, config: types.GetCachedContentConfigOrDict | None = None
    ) -> types.CachedContent: ...
    async def delete(
        self, *, name: str, config: types.DeleteCachedContentConfigOrDict | None = None
    ) -> types.DeleteCachedContentResponse: ...
    async def update(
        self, *, name: str, config: types.UpdateCachedContentConfigOrDict | None = None
    ) -> types.CachedContent: ...
    async def list(
        self, *, config: types.ListCachedContentsConfigOrDict | None = None
    ) -> AsyncPager[types.CachedContent]: ...
