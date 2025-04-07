from . import element as element
from . import fhirtypes as fhirtypes

class Attachment(element.Element):
    __resource_type__: str
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    creation: fhirtypes.DateTimeType | None
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    data: fhirtypes.Base64BinaryType | None
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hash: fhirtypes.Base64BinaryType | None
    hash__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    size: fhirtypes.UnsignedIntType | None
    size__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UrlType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
