from . import element as element
from . import fhirtypes as fhirtypes

class RelatedArtifact(element.Element):
    __resource_type__: str
    citation: fhirtypes.MarkdownType | None
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    document: fhirtypes.AttachmentType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.CanonicalType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UrlType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
