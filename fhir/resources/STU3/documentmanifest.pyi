from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DocumentManifest(domainresource.DomainResource):
    __resource_type__: str
    author: list[fhirtypes.ReferenceType] | None
    content: list[fhirtypes.DocumentManifestContentType]
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    masterIdentifier: fhirtypes.IdentifierType | None
    recipient: list[fhirtypes.ReferenceType] | None
    related: list[fhirtypes.DocumentManifestRelatedType] | None
    source: fhirtypes.UriType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DocumentManifestContent(backboneelement.BackboneElement):
    __resource_type__: str
    pAttachment: fhirtypes.AttachmentType | None
    pReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DocumentManifestRelated(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType | None
    ref: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
