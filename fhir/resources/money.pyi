from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Money(datatype.DataType):
    __resource_type__: str
    currency: fhirtypes.CodeType | None
    currency__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.DecimalType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
