import httpx
from _typeshed import Incomplete
from langfuse.client import Langfuse as Langfuse, StateType as StateType, StatefulSpanClient as StatefulSpanClient, StatefulTraceClient as StatefulTraceClient
from typing import Any, Callable

class LangfuseBaseCallbackHandler:
    log: Incomplete
    version: Incomplete
    session_id: Incomplete
    user_id: Incomplete
    trace_name: Incomplete
    release: Incomplete
    metadata: Incomplete
    tags: Incomplete
    root_span: Incomplete
    update_stateful_client: Incomplete
    langfuse: Incomplete
    trace: Incomplete
    def __init__(self, *, public_key: str | None = None, secret_key: str | None = None, host: str | None = None, debug: bool = False, stateful_client: StatefulTraceClient | StatefulSpanClient | None = None, update_stateful_client: bool = False, version: str | None = None, session_id: str | None = None, user_id: str | None = None, trace_name: str | None = None, release: str | None = None, metadata: Any | None = None, tags: list[str] | None = None, threads: int | None = None, flush_at: int | None = None, flush_interval: int | None = None, max_retries: int | None = None, timeout: int | None = None, enabled: bool | None = None, httpx_client: httpx.Client | None = None, sdk_integration: str, sample_rate: float | None = None, mask: Callable | None = None, environment: str | None = None) -> None: ...
    def get_trace_id(self): ...
    def get_trace_url(self): ...
    def flush(self) -> None: ...
    def auth_check(self): ...
