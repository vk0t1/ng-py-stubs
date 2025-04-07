from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DiagnosticReport(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType
    codedDiagnosis: list[fhirtypes.CodeableConceptType] | None
    conclusion: fhirtypes.StringType | None
    conclusion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    context: fhirtypes.ReferenceType | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    identifier: list[fhirtypes.IdentifierType] | None
    image: list[fhirtypes.DiagnosticReportImageType] | None
    imagingStudy: list[fhirtypes.ReferenceType] | None
    issued: fhirtypes.InstantType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: list[fhirtypes.DiagnosticReportPerformerType] | None
    presentedForm: list[fhirtypes.AttachmentType] | None
    result: list[fhirtypes.ReferenceType] | None
    specimen: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DiagnosticReportImage(backboneelement.BackboneElement):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    link: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class DiagnosticReportPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
