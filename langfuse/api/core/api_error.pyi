import typing

class ApiError(Exception):
    status_code: int | None
    body: typing.Any
    def __init__(self, *, status_code: int | None = None, body: typing.Any = None) -> None: ...
