from . import datatype as datatype
from . import fhirtypes as fhirtypes

class ContactPoint(datatype.DataType):
    __resource_type__: str
    period: fhirtypes.PeriodType | None
    rank: fhirtypes.PositiveIntType | None
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.CodeType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
