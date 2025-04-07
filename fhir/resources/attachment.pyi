from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Attachment(datatype.DataType):
    __resource_type__: str
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    creation: fhirtypes.DateTimeType | None
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    data: fhirtypes.Base64BinaryType | None
    data__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    duration: fhirtypes.DecimalType | None
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    frames: fhirtypes.PositiveIntType | None
    frames__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hash: fhirtypes.Base64BinaryType | None
    hash__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    height: fhirtypes.PositiveIntType | None
    height__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    pages: fhirtypes.PositiveIntType | None
    pages__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    size: fhirtypes.Integer64Type | None
    size__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UrlType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    width: fhirtypes.PositiveIntType | None
    width__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
