from _typeshed import Incomplete
from json import JSONEncoder
from langfuse.api.core import pydantic_utilities as pydantic_utilities, serialize_datetime as serialize_datetime
from langfuse.media import LangfuseMedia as LangfuseMedia
from typing import Any

logger: Incomplete

class EventSerializer(JSONEncoder):
    seen: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def default(self, obj: Any): ...
    def encode(self, obj: Any) -> str: ...
    @staticmethod
    def is_js_safe_integer(value: int) -> bool: ...
