import typing

import pydantic.v1 as pydantic_v1

__all__ = ["pydantic_v1"]

def deep_union_pydantic_dicts(
    source: typing.Dict[str, typing.Any], destination: typing.Dict[str, typing.Any]
) -> typing.Dict[str, typing.Any]: ...
