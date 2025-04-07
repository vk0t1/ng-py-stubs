from . import datatype as datatype
from . import fhirtypes as fhirtypes

class CodeableConcept(datatype.DataType):
    __resource_type__: str
    coding: list[fhirtypes.CodingType] | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
