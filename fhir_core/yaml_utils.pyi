from datetime import datetime
from decimal import Decimal

from _typeshed import Incomplete
from pydantic_core._pydantic_core import Url
from yaml import Node, ScalarNode
from yaml.representer import SafeRepresenter

__all__ = ["yaml_loads", "yaml_dumps"]

class Representer(SafeRepresenter):
    def represent_decimal(self, data: Decimal) -> Node: ...
    def represent_datetime(self, data: datetime) -> ScalarNode: ...
    def represent_url(self, data: Url) -> Node: ...

def yaml_loads(stream, loader: Incomplete | None = None): ...
def yaml_dumps(
    data,
    *,
    stream: Incomplete | None = None,
    indent: Incomplete | None = None,
    width: Incomplete | None = None,
    line_break: Incomplete | None = None,
    sort_keys: bool = False,
    encoding: str = "utf-8",
    return_bytes: bool = True,
): ...
