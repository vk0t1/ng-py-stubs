from . import element as element
from . import fhirtypes as fhirtypes

class Address(element.Element):
    __resource_type__: str
    city: fhirtypes.StringType | None
    city__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    country: fhirtypes.StringType | None
    country__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    district: fhirtypes.StringType | None
    district__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    line: list[fhirtypes.StringType | None] | None
    line__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    period: fhirtypes.PeriodType | None
    postalCode: fhirtypes.StringType | None
    postalCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    state: fhirtypes.StringType | None
    state__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
