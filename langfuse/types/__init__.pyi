from _typeshed import Incomplete
from datetime import datetime
from langfuse.api import MediaContentType as MediaContentType, UsageDetails as UsageDetails
from langfuse.model import MapValue as MapValue, ModelUsage as ModelUsage, PromptClient as PromptClient
from pydantic import BaseModel as BaseModel
from typing import Any, Protocol, TypedDict

SpanLevel: Incomplete
ScoreDataType: Incomplete

class TraceMetadata(TypedDict):
    name: str | None
    user_id: str | None
    session_id: str | None
    version: str | None
    release: str | None
    metadata: Any | None
    tags: list[str] | None
    public: bool | None

class ObservationParams(TraceMetadata, TypedDict):
    input: Any | None
    output: Any | None
    level: SpanLevel | None
    status_message: str | None
    start_time: datetime | None
    end_time: datetime | None
    completion_start_time: datetime | None
    model: str | None
    model_parameters: dict[str, MapValue] | None
    usage: BaseModel | ModelUsage | None
    usage_details: UsageDetails | None
    cost_details: dict[str, float] | None
    prompt: PromptClient | None

class MaskFunction(Protocol):
    def __call__(self, *, data: Any) -> Any: ...

class ParsedMediaReference(TypedDict):
    media_id: str
    source: str
    content_type: MediaContentType
