# mypy: ignore-errors
from json import JSONEncoder
from typing import Any

from _typeshed import Incomplete
from langfuse.api.core import pydantic_utilities as pydantic_utilities
from langfuse.api.core import serialize_datetime as serialize_datetime
from langfuse.media import LangfuseMedia as LangfuseMedia

logger: Incomplete

class EventSerializer(JSONEncoder):
    seen: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def default(self, obj: Any): ...
    def encode(self, obj: Any) -> str: ...
    @staticmethod
    def is_js_safe_integer(value: int) -> bool: ...
