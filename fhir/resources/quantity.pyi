from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Quantity(datatype.DataType):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comparator: fhirtypes.CodeType | None
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unit: fhirtypes.StringType | None
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.DecimalType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
