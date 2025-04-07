from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Communication(domainresource.DomainResource):
    __resource_type__: str
    about: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    inResponseTo: list[fhirtypes.ReferenceType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    medium: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    payload: list[fhirtypes.CommunicationPayloadType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    received: fhirtypes.DateTimeType | None
    received__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recipient: list[fhirtypes.ReferenceType] | None
    sender: fhirtypes.ReferenceType | None
    sent: fhirtypes.DateTimeType | None
    sent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType | None
    topic: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CommunicationPayload(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentCodeableConcept: fhirtypes.CodeableConceptType | None
    contentReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
