# mypy: ignore-errors

from typing import AsyncIterator, Awaitable, Iterator

from _typeshed import Incomplete

from . import _api_module
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient
from .pagers import AsyncPager as AsyncPager
from .pagers import Pager as Pager

logger: Incomplete

class Models(_api_module.BaseModule):
    def embed_content(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.EmbedContentConfigOrDict | None = None,
    ) -> types.EmbedContentResponse: ...
    def get(self, *, model: str, config: types.GetModelConfigOrDict | None = None) -> types.Model: ...
    def update(self, *, model: str, config: types.UpdateModelConfigOrDict | None = None) -> types.Model: ...
    def delete(
        self, *, model: str, config: types.DeleteModelConfigOrDict | None = None
    ) -> types.DeleteModelResponse: ...
    def count_tokens(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.CountTokensConfigOrDict | None = None,
    ) -> types.CountTokensResponse: ...
    def compute_tokens(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.ComputeTokensConfigOrDict | None = None,
    ) -> types.ComputeTokensResponse: ...
    def generate_videos(
        self,
        *,
        model: str,
        prompt: str | None = None,
        image: types.ImageOrDict | None = None,
        config: types.GenerateVideosConfigOrDict | None = None,
    ) -> types.GenerateVideosOperation: ...
    def generate_content(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.GenerateContentConfigOrDict | None = None,
    ) -> types.GenerateContentResponse: ...
    def generate_content_stream(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.GenerateContentConfigOrDict | None = None,
    ) -> Iterator[types.GenerateContentResponse]: ...
    def generate_images(
        self, *, model: str, prompt: str, config: types.GenerateImagesConfigOrDict | None = None
    ) -> types.GenerateImagesResponse: ...
    def edit_image(
        self,
        *,
        model: str,
        prompt: str,
        reference_images: list[types._ReferenceImageAPIOrDict],
        config: types.EditImageConfigOrDict | None = None,
    ) -> types.EditImageResponse: ...
    def upscale_image(
        self,
        *,
        model: str,
        image: types.ImageOrDict,
        upscale_factor: str,
        config: types.UpscaleImageConfigOrDict | None = None,
    ) -> types.UpscaleImageResponse: ...
    def list(self, *, config: types.ListModelsConfigOrDict | None = None) -> Pager[types.Model]: ...

class AsyncModels(_api_module.BaseModule):
    async def embed_content(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.EmbedContentConfigOrDict | None = None,
    ) -> types.EmbedContentResponse: ...
    async def get(self, *, model: str, config: types.GetModelConfigOrDict | None = None) -> types.Model: ...
    async def update(self, *, model: str, config: types.UpdateModelConfigOrDict | None = None) -> types.Model: ...
    async def delete(
        self, *, model: str, config: types.DeleteModelConfigOrDict | None = None
    ) -> types.DeleteModelResponse: ...
    async def count_tokens(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.CountTokensConfigOrDict | None = None,
    ) -> types.CountTokensResponse: ...
    async def compute_tokens(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.ComputeTokensConfigOrDict | None = None,
    ) -> types.ComputeTokensResponse: ...
    async def generate_videos(
        self,
        *,
        model: str,
        prompt: str | None = None,
        image: types.ImageOrDict | None = None,
        config: types.GenerateVideosConfigOrDict | None = None,
    ) -> types.GenerateVideosOperation: ...
    async def generate_content(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.GenerateContentConfigOrDict | None = None,
    ) -> types.GenerateContentResponse: ...
    async def generate_content_stream(
        self,
        *,
        model: str,
        contents: types.ContentListUnion | types.ContentListUnionDict,
        config: types.GenerateContentConfigOrDict | None = None,
    ) -> Awaitable[AsyncIterator[types.GenerateContentResponse]]: ...
    async def edit_image(
        self,
        *,
        model: str,
        prompt: str,
        reference_images: list[types._ReferenceImageAPIOrDict],
        config: types.EditImageConfigOrDict | None = None,
    ) -> types.EditImageResponse: ...
    async def list(self, *, config: types.ListModelsConfigOrDict | None = None) -> AsyncPager[types.Model]: ...
    async def generate_images(
        self, *, model: str, prompt: str, config: types.GenerateImagesConfigOrDict | None = None
    ) -> types.GenerateImagesResponse: ...
    async def upscale_image(
        self,
        *,
        model: str,
        image: types.ImageOrDict,
        upscale_factor: str,
        config: types.UpscaleImageConfigOrDict | None = None,
    ) -> types.UpscaleImageResponse: ...
