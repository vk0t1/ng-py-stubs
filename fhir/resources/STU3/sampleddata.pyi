from . import element as element
from . import fhirtypes as fhirtypes

class SampledData(element.Element):
    __resource_type__: str
    data: fhirtypes.StringType | None
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dimensions: fhirtypes.PositiveIntType | None
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lowerLimit: fhirtypes.DecimalType | None
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    origin: fhirtypes.QuantityType
    period: fhirtypes.DecimalType | None
    period__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    upperLimit: fhirtypes.DecimalType | None
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
