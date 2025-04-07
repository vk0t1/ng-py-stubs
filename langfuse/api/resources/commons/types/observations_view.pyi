import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .observation import Observation as Observation
from _typeshed import Incomplete

class ObservationsView(Observation):
    prompt_name: str | None
    prompt_version: int | None
    model_id: str | None
    input_price: float | None
    output_price: float | None
    total_price: float | None
    calculated_input_cost: float | None
    calculated_output_cost: float | None
    calculated_total_cost: float | None
    latency: float | None
    time_to_first_token: float | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
