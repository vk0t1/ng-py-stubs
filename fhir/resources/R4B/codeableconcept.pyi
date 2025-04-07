from . import element as element
from . import fhirtypes as fhirtypes

class CodeableConcept(element.Element):
    __resource_type__: str
    coding: list[fhirtypes.CodingType] | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
