import enum
import typing

T_Result = typing.TypeVar('T_Result')

class DatasetStatus(str, enum.Enum):
    ACTIVE = 'ACTIVE'
    ARCHIVED = 'ARCHIVED'
    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result: ...
