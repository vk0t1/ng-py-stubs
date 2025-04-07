from _typeshed import Incomplete
from langfuse.model import PromptClient as PromptClient
from queue import Queue
from threading import Thread

DEFAULT_PROMPT_CACHE_TTL_SECONDS: int
DEFAULT_PROMPT_CACHE_REFRESH_WORKERS: int

class PromptCacheItem:
    value: Incomplete
    def __init__(self, prompt: PromptClient, ttl_seconds: int) -> None: ...
    def is_expired(self) -> bool: ...
    @staticmethod
    def get_epoch_seconds() -> int: ...

class PromptCacheRefreshConsumer(Thread):
    running: bool
    daemon: bool
    def __init__(self, queue: Queue, identifier: int) -> None: ...
    def run(self) -> None: ...
    def pause(self) -> None: ...

class PromptCacheTaskManager:
    def __init__(self, threads: int = 1) -> None: ...
    def add_task(self, key: str, task): ...
    def active_tasks(self) -> int: ...
    def shutdown(self) -> None: ...

class PromptCache:
    def __init__(self, max_prompt_refresh_workers: int = ...) -> None: ...
    def get(self, key: str) -> PromptCacheItem | None: ...
    def set(self, key: str, value: PromptClient, ttl_seconds: int | None): ...
    def invalidate(self, prompt_name: str): ...
    def add_refresh_prompt_task(self, key: str, fetch_func): ...
    @staticmethod
    def generate_cache_key(name: str, *, version: int | None, label: str | None) -> str: ...
