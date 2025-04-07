from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Identifier(datatype.DataType):
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
