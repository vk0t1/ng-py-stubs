# mypy: ignore-errors

from _typeshed import Incomplete
from google.auth import environment_vars as environment_vars
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY
from google.cloud.storage.retry import (
    DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED as DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
)

STORAGE_EMULATOR_ENV_VAR: str

class _PropertyMixin:
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...
    @property
    def path(self) -> None: ...
    @property
    def client(self) -> None: ...
    @property
    def user_project(self) -> None: ...
    def reload(
        self,
        client: Incomplete | None = None,
        projection: str = "noAcl",
        if_etag_match: Incomplete | None = None,
        if_etag_not_match: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
        soft_deleted: Incomplete | None = None,
    ) -> None: ...
    def patch(
        self,
        client: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
        override_unlocked_retention: bool = False,
    ) -> None: ...
    def update(
        self,
        client: Incomplete | None = None,
        if_generation_match: Incomplete | None = None,
        if_generation_not_match: Incomplete | None = None,
        if_metageneration_match: Incomplete | None = None,
        if_metageneration_not_match: Incomplete | None = None,
        timeout=...,
        retry=...,
        override_unlocked_retention: bool = False,
    ) -> None: ...
