from fhir_core.fhirabstractmodel import FHIRAbstractModel

from .fhirtypes import IdType as IdType
from .fhirtypes import StringType as StringType

class FHIRResourceModel(FHIRAbstractModel):
    __resource_type__: str = "FHIRResourceModel"
    id: IdType | StringType | None = None
    def relative_base(self) -> str: ...
    def relative_path(self) -> str: ...
