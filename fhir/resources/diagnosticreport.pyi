from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DiagnosticReport(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    composition: fhirtypes.ReferenceType | None
    conclusion: fhirtypes.MarkdownType | None
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    conclusionCode: list[fhirtypes.CodeableConceptType] | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    issued: fhirtypes.InstantType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    media: list[fhirtypes.DiagnosticReportMediaType] | None
    note: list[fhirtypes.AnnotationType] | None
    performer: list[fhirtypes.ReferenceType] | None
    presentedForm: list[fhirtypes.AttachmentType] | None
    result: list[fhirtypes.ReferenceType] | None
    resultsInterpreter: list[fhirtypes.ReferenceType] | None
    specimen: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    study: list[fhirtypes.ReferenceType] | None
    subject: fhirtypes.ReferenceType | None
    supportingInfo: list[fhirtypes.DiagnosticReportSupportingInfoType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DiagnosticReportMedia(backboneelement.BackboneElement):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    link: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class DiagnosticReportSupportingInfo(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
