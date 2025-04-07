import datetime
from _typeshed import Incomplete

Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime
DateFromTicks: Incomplete
TimestampFromTicks: Incomplete

def Binary(data): ...
def TimeFromTicks(ticks, tz: Incomplete | None = None): ...

class _DBAPITypeObject:
    values: Incomplete
    def __init__(self, *values) -> None: ...
    def __eq__(self, other): ...

STRING: str
BINARY: Incomplete
NUMBER: Incomplete
DATETIME: Incomplete
ROWID: str
