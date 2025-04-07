import enum
import typing

T_Result = typing.TypeVar('T_Result')

class ObservationType(str, enum.Enum):
    SPAN = 'SPAN'
    GENERATION = 'GENERATION'
    EVENT = 'EVENT'
    def visit(self, span: typing.Callable[[], T_Result], generation: typing.Callable[[], T_Result], event: typing.Callable[[], T_Result]) -> T_Result: ...
