import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .create_event_body import CreateEventBody as CreateEventBody
from .create_generation_body import CreateGenerationBody as CreateGenerationBody
from .create_span_body import CreateSpanBody as CreateSpanBody
from .observation_body import ObservationBody as ObservationBody
from .score_body import ScoreBody as ScoreBody
from .sdk_log_body import SdkLogBody as SdkLogBody
from .trace_body import TraceBody as TraceBody
from .update_generation_body import UpdateGenerationBody as UpdateGenerationBody
from .update_span_body import UpdateSpanBody as UpdateSpanBody
from _typeshed import Incomplete

class IngestionEvent_TraceCreate(pydantic_v1.BaseModel):
    body: TraceBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['trace-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_ScoreCreate(pydantic_v1.BaseModel):
    body: ScoreBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['score-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_SpanCreate(pydantic_v1.BaseModel):
    body: CreateSpanBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['span-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_SpanUpdate(pydantic_v1.BaseModel):
    body: UpdateSpanBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['span-update']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_GenerationCreate(pydantic_v1.BaseModel):
    body: CreateGenerationBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['generation-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_GenerationUpdate(pydantic_v1.BaseModel):
    body: UpdateGenerationBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['generation-update']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_EventCreate(pydantic_v1.BaseModel):
    body: CreateEventBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['event-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_SdkLog(pydantic_v1.BaseModel):
    body: SdkLogBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['sdk-log']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_ObservationCreate(pydantic_v1.BaseModel):
    body: ObservationBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['observation-create']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete

class IngestionEvent_ObservationUpdate(pydantic_v1.BaseModel):
    body: ObservationBody
    id: str
    timestamp: str
    metadata: typing.Any | None
    type: typing.Literal['observation-update']
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete
IngestionEvent = IngestionEvent_TraceCreate | IngestionEvent_ScoreCreate | IngestionEvent_SpanCreate | IngestionEvent_SpanUpdate | IngestionEvent_GenerationCreate | IngestionEvent_GenerationUpdate | IngestionEvent_EventCreate | IngestionEvent_SdkLog | IngestionEvent_ObservationCreate | IngestionEvent_ObservationUpdate
