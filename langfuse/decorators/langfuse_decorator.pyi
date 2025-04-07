# mypy: ignore-errors
import httpx
from _typeshed import Incomplete
from datetime import datetime
from langfuse.api import UsageDetails as UsageDetails
from langfuse.client import (
    Langfuse as Langfuse,
    MapValue as MapValue,
    ModelUsage as ModelUsage,
    PromptClient as PromptClient,
    ScoreDataType as ScoreDataType,
    StateType as StateType,
    StatefulGenerationClient as StatefulGenerationClient,
    StatefulSpanClient as StatefulSpanClient,
    StatefulTraceClient as StatefulTraceClient,
)
from langfuse.serializer import EventSerializer as EventSerializer
from langfuse.types import ObservationParams as ObservationParams, SpanLevel as SpanLevel
from langfuse.utils.error_logging import catch_and_log_errors as catch_and_log_errors
from langfuse.utils.langfuse_singleton import LangfuseSingleton as LangfuseSingleton
from pydantic import BaseModel as BaseModel
from typing import Any, Callable, Iterable, Literal, TypeVar, overload
from typing_extensions import ParamSpec

F = TypeVar("F", bound=Callable[..., Any])
P = ParamSpec("P")
R = TypeVar("R")

class LangfuseDecorator:
    @overload
    def observe(self, func: F) -> F: ...
    @overload
    def observe(
        self,
        func: None = None,
        *,
        name: str | None = None,
        as_type: Literal["generation"] | None = None,
        capture_input: bool = True,
        capture_output: bool = True,
        transform_to_string: Callable[[Iterable[Any]], str] | None = None,
    ) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
    def get_current_llama_index_handler(self): ...
    def get_current_langchain_handler(self): ...
    def get_current_trace_id(self) -> str | None: ...
    def get_current_trace_url(self) -> str | None: ...
    def get_current_observation_id(self) -> str | None: ...
    def update_current_trace(
        self,
        name: str | None = None,
        input: Any | None = None,
        output: Any | None = None,
        user_id: str | None = None,
        session_id: str | None = None,
        version: str | None = None,
        release: str | None = None,
        metadata: Any | None = None,
        tags: list[str] | None = None,
        public: bool | None = None,
    ) -> None: ...
    def update_current_observation(
        self,
        *,
        input: Any | None = None,
        output: Any | None = None,
        name: str | None = None,
        version: str | None = None,
        metadata: Any | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        release: str | None = None,
        tags: list[str] | None = None,
        user_id: str | None = None,
        session_id: str | None = None,
        level: SpanLevel | None = None,
        status_message: str | None = None,
        completion_start_time: datetime | None = None,
        model: str | None = None,
        model_parameters: dict[str, MapValue] | None = None,
        usage: BaseModel | ModelUsage | None = None,
        usage_details: UsageDetails | None = None,
        cost_details: dict[str, float] | None = None,
        prompt: PromptClient | None = None,
        public: bool | None = None,
    ) -> None: ...
    def score_current_observation(
        self,
        *,
        name: str,
        value: float | str,
        data_type: ScoreDataType | None = None,
        comment: str | None = None,
        id: str | None = None,
        config_id: str | None = None,
    ) -> None: ...
    def score_current_trace(
        self,
        *,
        name: str,
        value: float | str,
        data_type: ScoreDataType | None = None,
        comment: str | None = None,
        id: str | None = None,
        config_id: str | None = None,
    ) -> None: ...
    def flush(self) -> None: ...
    def configure(
        self,
        *,
        public_key: str | None = None,
        secret_key: str | None = None,
        host: str | None = None,
        release: str | None = None,
        debug: bool | None = None,
        threads: int | None = None,
        flush_at: int | None = None,
        flush_interval: int | None = None,
        max_retries: int | None = None,
        timeout: int | None = None,
        httpx_client: httpx.Client | None = None,
        enabled: bool | None = None,
        mask: Callable | None = None,
        environment: str | None = None,
    ) -> None: ...
    @property
    def client_instance(self) -> Langfuse: ...
    def auth_check(self) -> bool: ...

langfuse_context: LangfuseDecorator

@overload
def observe(func: F) -> F: ...
@overload
def observe(
    func: None = None,
    *,
    name: str | None = None,
    as_type: Literal["generation"] | None = None,
    capture_input: bool = True,
    capture_output: bool = True,
    transform_to_string: Callable[[Iterable[Any]], str] | None = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
