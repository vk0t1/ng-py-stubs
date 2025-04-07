import typing
from ....core.api_error import ApiError as ApiError

class UnauthorizedError(ApiError):
    def __init__(self, body: typing.Any) -> None: ...
