import enum
import typing

T_Result = typing.TypeVar('T_Result')

class ObservationLevel(str, enum.Enum):
    DEBUG = 'DEBUG'
    DEFAULT = 'DEFAULT'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    def visit(self, debug: typing.Callable[[], T_Result], default: typing.Callable[[], T_Result], warning: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result: ...
