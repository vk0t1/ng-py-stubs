from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Signature(datatype.DataType):
    __resource_type__: str
    data: fhirtypes.Base64BinaryType | None
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onBehalfOf: fhirtypes.ReferenceType | None
    sigFormat: fhirtypes.CodeType | None
    sigFormat__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetFormat: fhirtypes.CodeType | None
    targetFormat__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodingType] | None
    when: fhirtypes.InstantType | None
    when__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    who: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
