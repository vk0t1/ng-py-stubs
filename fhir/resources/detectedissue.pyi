from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DetectedIssue(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType | None
    detail: fhirtypes.MarkdownType | None
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    evidence: list[fhirtypes.DetectedIssueEvidenceType] | None
    identifiedDateTime: fhirtypes.DateTimeType | None
    identifiedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifiedPeriod: fhirtypes.PeriodType | None
    identifier: list[fhirtypes.IdentifierType] | None
    implicated: list[fhirtypes.ReferenceType] | None
    mitigation: list[fhirtypes.DetectedIssueMitigationType] | None
    reference: fhirtypes.UriType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DetectedIssueEvidence(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodeableConceptType] | None
    detail: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class DetectedIssueMitigation(backboneelement.BackboneElement):
    __resource_type__: str
    action: fhirtypes.CodeableConceptType
    author: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    @classmethod
    def elements_sequence(cls): ...
