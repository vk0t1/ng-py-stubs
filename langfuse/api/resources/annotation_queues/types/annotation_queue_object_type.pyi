import enum
import typing

T_Result = typing.TypeVar('T_Result')

class AnnotationQueueObjectType(str, enum.Enum):
    TRACE = 'TRACE'
    OBSERVATION = 'OBSERVATION'
    def visit(self, trace: typing.Callable[[], T_Result], observation: typing.Callable[[], T_Result]) -> T_Result: ...
