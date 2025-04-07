from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ResearchSubject(domainresource.DomainResource):
    __resource_type__: str
    actualComparisonGroup: fhirtypes.IdType | None
    actualComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    assignedComparisonGroup: fhirtypes.IdType | None
    assignedComparisonGroup__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    consent: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    period: fhirtypes.PeriodType | None
    progress: list[fhirtypes.ResearchSubjectProgressType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    study: fhirtypes.ReferenceType
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ResearchSubjectProgress(backboneelement.BackboneElement):
    __resource_type__: str
    endDate: fhirtypes.DateTimeType | None
    endDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    milestone: fhirtypes.CodeableConceptType | None
    reason: fhirtypes.CodeableConceptType | None
    startDate: fhirtypes.DateTimeType | None
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectState: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
