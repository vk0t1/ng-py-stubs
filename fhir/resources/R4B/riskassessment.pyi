from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RiskAssessment(domainresource.DomainResource):
    __resource_type__: str = "RiskAssessment"
    basedOn: fhirtypes.ReferenceType | None = None
    basis: list[fhirtypes.ReferenceType] | None = None
    code: fhirtypes.CodeableConceptType | None = None
    condition: fhirtypes.ReferenceType | None = None
    encounter: fhirtypes.ReferenceType | None = None
    identifier: list[fhirtypes.IdentifierType] | None = None
    method: fhirtypes.CodeableConceptType | None = None
    mitigation: fhirtypes.StringType | None = None
    mitigation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    note: list[fhirtypes.AnnotationType] | None = None
    occurrenceDateTime: fhirtypes.DateTimeType | None = None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    occurrencePeriod: fhirtypes.PeriodType | None = None
    parent: fhirtypes.ReferenceType | None = None
    performer: fhirtypes.ReferenceType | None = None
    prediction: list[fhirtypes.RiskAssessmentPredictionType] | None = None
    reasonCode: list[fhirtypes.CodeableConceptType] | None = None
    reasonReference: list[fhirtypes.ReferenceType] | None = None
    status: fhirtypes.CodeType | None = None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
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
    def elements_sequence(cls) -> list[str]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
