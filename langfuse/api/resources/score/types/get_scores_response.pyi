import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from ...utils.resources.pagination.types.meta_response import MetaResponse as MetaResponse
from .get_scores_response_data import GetScoresResponseData as GetScoresResponseData
from _typeshed import Incomplete

class GetScoresResponse(pydantic_v1.BaseModel):
    data: list[GetScoresResponseData]
    meta: MetaResponse
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        extra: Incomplete
        json_encoders: Incomplete
