from . import element as element
from . import fhirtypes as fhirtypes

class Reference(element.Element):
    __resource_type__: str
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    reference: fhirtypes.StringType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
