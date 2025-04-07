from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Expression(datatype.DataType):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.CodeType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.UriType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
