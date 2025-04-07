from . import datatype as datatype
from . import fhirtypes as fhirtypes

class RelatedArtifact(datatype.DataType):
    __resource_type__: str
    citation: fhirtypes.MarkdownType | None
    citation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    classifier: list[fhirtypes.CodeableConceptType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    document: fhirtypes.AttachmentType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publicationDate: fhirtypes.DateType | None
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publicationStatus: fhirtypes.CodeType | None
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.CanonicalType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resourceReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
