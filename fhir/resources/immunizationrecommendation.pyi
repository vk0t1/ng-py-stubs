from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImmunizationRecommendation(domainresource.DomainResource):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    patient: fhirtypes.ReferenceType
    recommendation: list[fhirtypes.ImmunizationRecommendationRecommendationType]
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    __resource_type__: str
    contraindicatedVaccineCode: list[fhirtypes.CodeableConceptType] | None
    dateCriterion: list[fhirtypes.ImmunizationRecommendationRecommendationDateCriterionType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseNumber: fhirtypes.StringType | None
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    forecastReason: list[fhirtypes.CodeableConceptType] | None
    forecastStatus: fhirtypes.CodeableConceptType
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDoses: fhirtypes.StringType | None
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportingImmunization: list[fhirtypes.ReferenceType] | None
    supportingPatientInformation: list[fhirtypes.ReferenceType] | None
    targetDisease: list[fhirtypes.CodeableConceptType] | None
    vaccineCode: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    value: fhirtypes.DateTimeType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
