import enum
import typing

T_Result = typing.TypeVar('T_Result')

class ScoreDataType(str, enum.Enum):
    NUMERIC = 'NUMERIC'
    BOOLEAN = 'BOOLEAN'
    CATEGORICAL = 'CATEGORICAL'
    def visit(self, numeric: typing.Callable[[], T_Result], boolean: typing.Callable[[], T_Result], categorical: typing.Callable[[], T_Result]) -> T_Result: ...
