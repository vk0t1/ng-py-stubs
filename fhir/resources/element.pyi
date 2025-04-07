from . import base as base
from . import fhirtypes as fhirtypes

class Element(base.Base):
    __resource_type__: str
    extension: list[fhirtypes.ExtensionType] | None
    id: fhirtypes.StringType | None
    @classmethod
    def elements_sequence(cls): ...
