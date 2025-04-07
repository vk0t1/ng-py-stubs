from ....core.api_error import ApiError as ApiError

class ServiceUnavailableError(ApiError):
    def __init__(self) -> None: ...
