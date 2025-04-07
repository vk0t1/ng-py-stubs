import typing
from ....core.datetime_utils import serialize_datetime as serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts as deep_union_pydantic_dicts, pydantic_v1 as pydantic_v1
from .annotation_queue_object_type import AnnotationQueueObjectType as AnnotationQueueObjectType
from .annotation_queue_status import AnnotationQueueStatus as AnnotationQueueStatus
from _typeshed import Incomplete

class CreateAnnotationQueueItemRequest(pydantic_v1.BaseModel):
    object_id: str
    object_type: AnnotationQueueObjectType
    status: AnnotationQueueStatus | None
    def json(self, **kwargs: typing.Any) -> str: ...
    def dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...
    class Config:
        frozen: bool
        smart_union: bool
        allow_population_by_field_name: bool
        populate_by_name: bool
        extra: Incomplete
        json_encoders: Incomplete
