# mypy: ignore-errors

import abc
from abc import ABC, abstractmethod
from typing import Any, TypedDict

from _typeshed import Incomplete
from langfuse.api.resources.commons.types.dataset import Dataset as Dataset
from langfuse.api.resources.commons.types.dataset_item import DatasetItem as DatasetItem
from langfuse.api.resources.commons.types.dataset_run import DatasetRun as DatasetRun
from langfuse.api.resources.commons.types.dataset_status import DatasetStatus as DatasetStatus
from langfuse.api.resources.commons.types.map_value import MapValue as MapValue
from langfuse.api.resources.commons.types.observation import Observation as Observation
from langfuse.api.resources.commons.types.trace_with_full_details import TraceWithFullDetails as TraceWithFullDetails
from langfuse.api.resources.dataset_items.types.create_dataset_item_request import (
    CreateDatasetItemRequest as CreateDatasetItemRequest,
)
from langfuse.api.resources.dataset_run_items.types.create_dataset_run_item_request import (
    CreateDatasetRunItemRequest as CreateDatasetRunItemRequest,
)
from langfuse.api.resources.datasets.types.create_dataset_request import CreateDatasetRequest as CreateDatasetRequest
from langfuse.api.resources.prompts import ChatMessage as ChatMessage
from langfuse.api.resources.prompts import Prompt as Prompt
from langfuse.api.resources.prompts import Prompt_Chat as Prompt_Chat
from langfuse.api.resources.prompts import Prompt_Text as Prompt_Text

class ModelUsage(TypedDict):
    unit: str | None
    input: int | None
    output: int | None
    total: int | None
    input_cost: float | None
    output_cost: float | None
    total_cost: float | None

class ChatMessageDict(TypedDict):
    role: str
    content: str

class TemplateParser:
    OPENING: str
    CLOSING: str
    @staticmethod
    def find_variable_names(content: str) -> list[str]: ...
    @staticmethod
    def compile_template(content: str, data: dict[str, Any] | None = None) -> str: ...

class BasePromptClient(ABC, metaclass=abc.ABCMeta):
    name: str
    version: int
    config: dict[str, Any]
    labels: list[str]
    tags: list[str]
    commit_message: str | None
    is_fallback: Incomplete
    def __init__(self, prompt: Prompt, is_fallback: bool = False) -> None: ...
    @abstractmethod
    def compile(self, **kwargs) -> str | list[ChatMessage]: ...
    @property
    @abstractmethod
    def variables(self) -> list[str]: ...
    @abstractmethod
    def __eq__(self, other): ...
    @abstractmethod
    def get_langchain_prompt(self): ...

class TextPromptClient(BasePromptClient):
    prompt: Incomplete
    def __init__(self, prompt: Prompt_Text, is_fallback: bool = False) -> None: ...
    def compile(self, **kwargs) -> str: ...
    @property
    def variables(self) -> list[str]: ...
    def __eq__(self, other): ...
    def get_langchain_prompt(self, **kwargs) -> str: ...

class ChatPromptClient(BasePromptClient):
    prompt: Incomplete
    def __init__(self, prompt: Prompt_Chat, is_fallback: bool = False) -> None: ...
    def compile(self, **kwargs) -> list[ChatMessageDict]: ...
    @property
    def variables(self) -> list[str]: ...
    def __eq__(self, other): ...
    def get_langchain_prompt(self, **kwargs): ...

PromptClient = TextPromptClient | ChatPromptClient
