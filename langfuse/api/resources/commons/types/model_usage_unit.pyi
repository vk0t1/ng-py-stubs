import enum
import typing

T_Result = typing.TypeVar('T_Result')

class ModelUsageUnit(str, enum.Enum):
    CHARACTERS = 'CHARACTERS'
    TOKENS = 'TOKENS'
    MILLISECONDS = 'MILLISECONDS'
    SECONDS = 'SECONDS'
    IMAGES = 'IMAGES'
    REQUESTS = 'REQUESTS'
    def visit(self, characters: typing.Callable[[], T_Result], tokens: typing.Callable[[], T_Result], milliseconds: typing.Callable[[], T_Result], seconds: typing.Callable[[], T_Result], images: typing.Callable[[], T_Result], requests: typing.Callable[[], T_Result]) -> T_Result: ...
