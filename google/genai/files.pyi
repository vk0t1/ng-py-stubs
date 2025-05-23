# mypy: ignore-errors

import io
import os
import pathlib

from _typeshed import Incomplete

from . import _api_module
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient
from .pagers import AsyncPager as AsyncPager
from .pagers import Pager as Pager

logger: Incomplete

class Files(_api_module.BaseModule):
    def get(self, *, name: str, config: types.GetFileConfigOrDict | None = None) -> types.File: ...
    def delete(self, *, name: str, config: types.DeleteFileConfigOrDict | None = None) -> types.DeleteFileResponse: ...
    def upload(
        self, *, file: str | pathlib.Path | os.PathLike | io.IOBase, config: types.UploadFileConfigOrDict | None = None
    ) -> types.File: ...
    def list(self, *, config: types.ListFilesConfigOrDict | None = None) -> Pager[types.File]: ...
    def download(
        self,
        *,
        file: str | types.File | types.Video | types.GeneratedVideo,
        config: types.DownloadFileConfigOrDict | None = None,
    ) -> bytes: ...

class AsyncFiles(_api_module.BaseModule):
    async def get(self, *, name: str, config: types.GetFileConfigOrDict | None = None) -> types.File: ...
    async def delete(
        self, *, name: str, config: types.DeleteFileConfigOrDict | None = None
    ) -> types.DeleteFileResponse: ...
    async def upload(
        self, *, file: str | pathlib.Path | os.PathLike | io.IOBase, config: types.UploadFileConfigOrDict | None = None
    ) -> types.File: ...
    async def list(self, *, config: types.ListFilesConfigOrDict | None = None) -> AsyncPager[types.File]: ...
    async def download(
        self, *, file: str | types.File, config: types.DownloadFileConfigOrDict | None = None
    ) -> bytes: ...
