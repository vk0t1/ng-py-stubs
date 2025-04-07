from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Communication(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    medium: list[fhirtypes.CodeableConceptType] | None
    notDone: bool | None
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notDoneReason: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    payload: list[fhirtypes.CommunicationPayloadType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    received: fhirtypes.DateTimeType | None
    received__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recipient: list[fhirtypes.ReferenceType] | None
    sender: fhirtypes.ReferenceType | None
    sent: fhirtypes.DateTimeType | None
    sent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    topic: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CommunicationPayload(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentReference: fhirtypes.ReferenceType | None
    contentString: fhirtypes.StringType | None
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
