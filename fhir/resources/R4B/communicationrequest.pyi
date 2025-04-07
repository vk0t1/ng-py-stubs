from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CommunicationRequest(domainresource.DomainResource):
    __resource_type__: str
    about: list[fhirtypes.ReferenceType] | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    medium: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    payload: list[fhirtypes.CommunicationRequestPayloadType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    recipient: list[fhirtypes.ReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.ReferenceType | None
    sender: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CommunicationRequestPayload(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentReference: fhirtypes.ReferenceType | None
    contentString: fhirtypes.StringType | None
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
