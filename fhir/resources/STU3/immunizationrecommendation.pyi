from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImmunizationRecommendation(domainresource.DomainResource):
    __resource_type__: str
    identifier: list[fhirtypes.IdentifierType] | None
    patient: fhirtypes.ReferenceType
    recommendation: list[fhirtypes.ImmunizationRecommendationRecommendationType]
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dateCriterion: list[fhirtypes.ImmunizationRecommendationRecommendationDateCriterionType] | None
    doseNumber: fhirtypes.PositiveIntType | None
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    forecastStatus: fhirtypes.CodeableConceptType
    protocol: fhirtypes.ImmunizationRecommendationRecommendationProtocolType | None
    supportingImmunization: list[fhirtypes.ReferenceType] | None
    supportingPatientInformation: list[fhirtypes.ReferenceType] | None
    targetDisease: fhirtypes.CodeableConceptType | None
    vaccineCode: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    value: fhirtypes.DateTimeType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseSequence: fhirtypes.PositiveIntType | None
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
