from . import element as element
from . import fhirtypes as fhirtypes

class HumanName(element.Element):
    __resource_type__: str
    family: fhirtypes.StringType | None
    family__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    given: list[fhirtypes.StringType | None] | None
    given__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    period: fhirtypes.PeriodType | None
    prefix: list[fhirtypes.StringType | None] | None
    prefix__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    suffix: list[fhirtypes.StringType | None] | None
    suffix__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
