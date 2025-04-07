from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DocumentReference(domainresource.DomainResource):
    __resource_type__: str
    authenticator: fhirtypes.ReferenceType | None
    author: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    content: list[fhirtypes.DocumentReferenceContentType]
    context: fhirtypes.DocumentReferenceContextType | None
    custodian: fhirtypes.ReferenceType | None
    date: fhirtypes.InstantType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    docStatus: fhirtypes.CodeType | None
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    masterIdentifier: fhirtypes.IdentifierType | None
    relatesTo: list[fhirtypes.DocumentReferenceRelatesToType] | None
    securityLabel: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DocumentReferenceContent(backboneelement.BackboneElement):
    __resource_type__: str
    attachment: fhirtypes.AttachmentType
    format: fhirtypes.CodingType | None
    @classmethod
    def elements_sequence(cls): ...

class DocumentReferenceContext(backboneelement.BackboneElement):
    __resource_type__: str
    encounter: list[fhirtypes.ReferenceType] | None
    event: list[fhirtypes.CodeableConceptType] | None
    facilityType: fhirtypes.CodeableConceptType | None
    period: fhirtypes.PeriodType | None
    practiceSetting: fhirtypes.CodeableConceptType | None
    related: list[fhirtypes.ReferenceType] | None
    sourcePatientInfo: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
