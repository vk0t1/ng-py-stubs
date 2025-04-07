# mypy: ignore-errors

import typing

from _typeshed import Incomplete

from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts
from ....core.pydantic_utilities import pydantic_v1 as pydantic_v1
from .observations_view import ObservationsView as ObservationsView
from .score import Score as Score
from .trace import Trace as Trace

class TraceWithFullDetails(Trace):
    html_path: str
    latency: float
    total_cost: float
    observations: list[ObservationsView]
    scores: list[Score]
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
