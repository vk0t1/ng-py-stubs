from . import element as element
from . import fhirtypes as fhirtypes

class Signature(element.Element):
    __resource_type__: str
    blob: fhirtypes.Base64BinaryType | None
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onBehalfOfReference: fhirtypes.ReferenceType | None
    onBehalfOfUri: fhirtypes.UriType | None
    onBehalfOfUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodingType]
    when: fhirtypes.InstantType | None
    when__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whoReference: fhirtypes.ReferenceType | None
    whoUri: fhirtypes.UriType | None
    whoUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
