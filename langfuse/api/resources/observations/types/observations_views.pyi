import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...commons.types.observations_view import ObservationsView as ObservationsView
from ...utils.resources.pagination.types.meta_response import MetaResponse as MetaResponse
from _typeshed import Incomplete

class ObservationsViews(pydantic_v1.BaseModel):
    data: list[ObservationsView]
    meta: MetaResponse
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete
