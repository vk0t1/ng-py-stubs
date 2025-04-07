from . import element as element
from . import fhirtypes as fhirtypes

class Period(element.Element):
    __resource_type__: str
    end: fhirtypes.DateTimeType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    start: fhirtypes.DateTimeType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
