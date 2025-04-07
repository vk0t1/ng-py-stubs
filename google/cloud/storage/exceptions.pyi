# mypy: ignore-errors

from _typeshed import Incomplete
from google.resumable_media import DataCorruption as DataCorruptionDynamicParent
from google.resumable_media import InvalidResponse as InvalidResponseDynamicParent

InvalidResponseDynamicParent = Exception
DataCorruptionDynamicParent = Exception

class InvalidResponse(InvalidResponseDynamicParent):
    response: Incomplete
    def __init__(self, response, *args) -> None: ...

class DataCorruption(DataCorruptionDynamicParent):
    response: Incomplete
    def __init__(self, response, *args) -> None: ...
