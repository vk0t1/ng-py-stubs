from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DocumentReference(domainresource.DomainResource):
    __resource_type__: str = "DocumentReference"
    authenticator: fhirtypes.ReferenceType | None = None
    author: list[fhirtypes.ReferenceType] | None = None
    category: list[fhirtypes.CodeableConceptType] | None = None
    content: list[fhirtypes.DocumentReferenceContentType] = []
    context: fhirtypes.DocumentReferenceContextType | None = None
    custodian: fhirtypes.ReferenceType | None = None
    date: fhirtypes.InstantType | None = None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    description: fhirtypes.StringType | None = None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    docStatus: fhirtypes.CodeType | None = None
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    identifier: list[fhirtypes.IdentifierType] | None = None
    masterIdentifier: fhirtypes.IdentifierType | None = None
    relatesTo: list[fhirtypes.DocumentReferenceRelatesToType] | None = None
    securityLabel: list[fhirtypes.CodeableConceptType] | None = None
    status: fhirtypes.CodeType | None = None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    subject: fhirtypes.ReferenceType | None = None
    type: fhirtypes.CodeableConceptType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DocumentReferenceContent(backboneelement.BackboneElement):
    __resource_type__: str = "DocumentReferenceContent"
    attachment: fhirtypes.AttachmentType
    format: fhirtypes.CodingType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...

class DocumentReferenceContext(backboneelement.BackboneElement):
    __resource_type__: str = "DocumentReferenceContext"
    encounter: list[fhirtypes.ReferenceType] | None = None
    event: list[fhirtypes.CodeableConceptType] | None = None
    facilityType: fhirtypes.CodeableConceptType | None = None
    period: fhirtypes.PeriodType | None = None
    practiceSetting: fhirtypes.CodeableConceptType | None = None
    related: list[fhirtypes.ReferenceType] | None = None
    sourcePatientInfo: fhirtypes.ReferenceType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...

class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str = "DocumentReferenceRelatesTo"
    code: fhirtypes.CodeType | None = None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    target: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
