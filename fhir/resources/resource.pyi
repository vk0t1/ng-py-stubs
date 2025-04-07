from . import base as base
from . import fhirtypes as fhirtypes

class Resource(base.Base):
    __resource_type__: str
    id: fhirtypes.IdType | None
    implicitRules: fhirtypes.UriType | None
    implicitRules__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    meta: fhirtypes.MetaType | None
    @classmethod
    def elements_sequence(cls): ...
