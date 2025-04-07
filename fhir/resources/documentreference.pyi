from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DocumentReference(domainresource.DomainResource):
    __resource_type__: str
    attester: list[fhirtypes.DocumentReferenceAttesterType] | None
    author: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: list[fhirtypes.CodeableReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    content: list[fhirtypes.DocumentReferenceContentType]
    context: list[fhirtypes.ReferenceType] | None
    custodian: fhirtypes.ReferenceType | None
    date: fhirtypes.InstantType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    docStatus: fhirtypes.CodeType | None
    docStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    event: list[fhirtypes.CodeableReferenceType] | None
    facilityType: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    modality: list[fhirtypes.CodeableConceptType] | None
    period: fhirtypes.PeriodType | None
    practiceSetting: fhirtypes.CodeableConceptType | None
    relatesTo: list[fhirtypes.DocumentReferenceRelatesToType] | None
    securityLabel: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DocumentReferenceAttester(backboneelement.BackboneElement):
    __resource_type__: str
    mode: fhirtypes.CodeableConceptType
    party: fhirtypes.ReferenceType | None
    time: fhirtypes.DateTimeType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class DocumentReferenceContent(backboneelement.BackboneElement):
    __resource_type__: str
    attachment: fhirtypes.AttachmentType
    profile: list[fhirtypes.DocumentReferenceContentProfileType] | None
    @classmethod
    def elements_sequence(cls): ...

class DocumentReferenceContentProfile(backboneelement.BackboneElement):
    __resource_type__: str
    valueCanonical: fhirtypes.CanonicalType | None
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    target: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
