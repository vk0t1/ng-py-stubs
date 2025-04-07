import typing
from _typeshed import Incomplete
from langfuse.model import ModelUsage as ModelUsage, PromptClient as PromptClient

log: Incomplete
T = typing.TypeVar('T')

def extract_by_priority(usage: dict, keys: list[str], target_type: type[T]) -> T | None: ...
