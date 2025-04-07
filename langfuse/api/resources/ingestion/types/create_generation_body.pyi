import datetime as dt
import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.map_value import MapValue as MapValue
from .create_span_body import CreateSpanBody as CreateSpanBody
from .ingestion_usage import IngestionUsage as IngestionUsage
from .usage_details import UsageDetails as UsageDetails
from _typeshed import Incomplete

class CreateGenerationBody(CreateSpanBody):
    completion_start_time: dt.datetime | None
    model: str | None
    model_parameters: dict[str, MapValue] | None
    usage: IngestionUsage | None
    usage_details: UsageDetails | None
    cost_details: dict[str, float] | None
    prompt_name: str | None
    prompt_version: int | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
