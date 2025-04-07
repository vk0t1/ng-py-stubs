import typing
from typing_extensions import NotRequired

class RequestOptions(typing.TypedDict, total=False):
    timeout_in_seconds: NotRequired[int]
    max_retries: NotRequired[int]
    additional_headers: NotRequired[dict[str, typing.Any]]
    additional_query_parameters: NotRequired[dict[str, typing.Any]]
    additional_body_parameters: NotRequired[dict[str, typing.Any]]
