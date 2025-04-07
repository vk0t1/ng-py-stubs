from fhir_core.fhirabstractmodel import FHIRAbstractModel

from .fhirtypes import IdType as IdType
from .fhirtypes import StringType as StringType

class FHIRResourceModel(FHIRAbstractModel):
    __resource_type__: str
    id: IdType | StringType | None
    def relative_base(self): ...
    def relative_path(self): ...
