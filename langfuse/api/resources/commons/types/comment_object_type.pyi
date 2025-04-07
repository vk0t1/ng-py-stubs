import enum
import typing

T_Result = typing.TypeVar('T_Result')

class CommentObjectType(str, enum.Enum):
    TRACE = 'TRACE'
    OBSERVATION = 'OBSERVATION'
    SESSION = 'SESSION'
    PROMPT = 'PROMPT'
    def visit(self, trace: typing.Callable[[], T_Result], observation: typing.Callable[[], T_Result], session: typing.Callable[[], T_Result], prompt: typing.Callable[[], T_Result]) -> T_Result: ...
