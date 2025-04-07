from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RiskAssessment(domainresource.DomainResource):
    __resource_type__: str
    basedOn: fhirtypes.ReferenceType | None
    basis: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    condition: fhirtypes.ReferenceType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    method: fhirtypes.CodeableConceptType | None
    mitigation: fhirtypes.StringType | None
    mitigation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    parent: fhirtypes.ReferenceType | None
    performer: fhirtypes.ReferenceType | None
    prediction: list[fhirtypes.RiskAssessmentPredictionType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    __resource_type__: str
    outcome: fhirtypes.CodeableConceptType | None
    probabilityDecimal: fhirtypes.DecimalType | None
    probabilityDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    probabilityRange: fhirtypes.RangeType | None
    qualitativeRisk: fhirtypes.CodeableConceptType | None
    rationale: fhirtypes.StringType | None
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relativeRisk: fhirtypes.DecimalType | None
    relativeRisk__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenPeriod: fhirtypes.PeriodType | None
    whenRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
