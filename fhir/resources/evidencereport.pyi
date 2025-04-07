from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EvidenceReport(domainresource.DomainResource):
    __resource_type__: str
    author: list[fhirtypes.ContactDetailType] | None
    citeAsMarkdown: fhirtypes.MarkdownType | None
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    citeAsReference: fhirtypes.ReferenceType | None
    contact: list[fhirtypes.ContactDetailType] | None
    editor: list[fhirtypes.ContactDetailType] | None
    endorser: list[fhirtypes.ContactDetailType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    relatedIdentifier: list[fhirtypes.IdentifierType] | None
    relatesTo: list[fhirtypes.EvidenceReportRelatesToType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    section: list[fhirtypes.EvidenceReportSectionType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.EvidenceReportSubjectType
    type: fhirtypes.CodeableConceptType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceReportRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.EvidenceReportRelatesToTargetType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EvidenceReportRelatesToTarget(backboneelement.BackboneElement):
    __resource_type__: str
    display: fhirtypes.MarkdownType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    resource: fhirtypes.ReferenceType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceReportSection(backboneelement.BackboneElement):
    __resource_type__: str
    author: list[fhirtypes.ReferenceType] | None
    emptyReason: fhirtypes.CodeableConceptType | None
    entryClassifier: list[fhirtypes.CodeableConceptType] | None
    entryQuantity: list[fhirtypes.QuantityType] | None
    entryReference: list[fhirtypes.ReferenceType] | None
    focus: fhirtypes.CodeableConceptType | None
    focusReference: fhirtypes.ReferenceType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    orderedBy: fhirtypes.CodeableConceptType | None
    section: list[fhirtypes.EvidenceReportSectionType] | None
    text: fhirtypes.NarrativeType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceReportSubject(backboneelement.BackboneElement):
    __resource_type__: str
    characteristic: list[fhirtypes.EvidenceReportSubjectCharacteristicType] | None
    note: list[fhirtypes.AnnotationType] | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceReportSubjectCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    exclude: bool | None
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
