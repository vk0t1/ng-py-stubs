from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Coding(datatype.DataType):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    userSelected: bool | None
    userSelected__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
