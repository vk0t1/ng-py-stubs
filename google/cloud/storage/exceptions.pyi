from _typeshed import Incomplete
from google.resumable_media import DataCorruption as DataCorruptionDynamicParent, InvalidResponse as InvalidResponseDynamicParent

InvalidResponseDynamicParent = Exception
DataCorruptionDynamicParent = Exception

class InvalidResponse(InvalidResponseDynamicParent):
    response: Incomplete
    def __init__(self, response, *args) -> None: ...

class DataCorruption(DataCorruptionDynamicParent):
    response: Incomplete
    def __init__(self, response, *args) -> None: ...
