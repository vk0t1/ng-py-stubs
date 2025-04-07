from . import datatype as datatype
from . import fhirtypes as fhirtypes

class SampledData(datatype.DataType):
    __resource_type__: str
    codeMap: fhirtypes.CanonicalType | None
    codeMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    data: fhirtypes.StringType | None
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dimensions: fhirtypes.PositiveIntType | None
    dimensions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    interval: fhirtypes.DecimalType | None
    interval__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    intervalUnit: fhirtypes.CodeType | None
    intervalUnit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lowerLimit: fhirtypes.DecimalType | None
    lowerLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offsets: fhirtypes.StringType | None
    offsets__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    origin: fhirtypes.QuantityType
    upperLimit: fhirtypes.DecimalType | None
    upperLimit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
