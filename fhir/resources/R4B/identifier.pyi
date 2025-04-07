from . import element as element
from . import fhirtypes as fhirtypes

class Identifier(element.Element):
    __resource_type__: str
    assigner: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
