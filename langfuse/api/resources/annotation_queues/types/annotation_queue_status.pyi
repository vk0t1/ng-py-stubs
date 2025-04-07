import enum
import typing

T_Result = typing.TypeVar('T_Result')

class AnnotationQueueStatus(str, enum.Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    def visit(self, pending: typing.Callable[[], T_Result], completed: typing.Callable[[], T_Result]) -> T_Result: ...
