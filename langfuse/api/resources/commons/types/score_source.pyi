import enum
import typing

T_Result = typing.TypeVar('T_Result')

class ScoreSource(str, enum.Enum):
    ANNOTATION = 'ANNOTATION'
    API = 'API'
    EVAL = 'EVAL'
    def visit(self, annotation: typing.Callable[[], T_Result], api: typing.Callable[[], T_Result], eval: typing.Callable[[], T_Result]) -> T_Result: ...
