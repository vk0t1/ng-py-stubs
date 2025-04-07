from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Measure(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    clinicalRecommendationStatement: fhirtypes.MarkdownType | None
    clinicalRecommendationStatement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compositeScoring: fhirtypes.CodeableConceptType | None
    contact: list[fhirtypes.ContactDetailType] | None
    contributor: list[fhirtypes.ContributorType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definition: list[fhirtypes.MarkdownType | None] | None
    definition__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disclaimer: fhirtypes.MarkdownType | None
    disclaimer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    group: list[fhirtypes.MeasureGroupType] | None
    guidance: fhirtypes.MarkdownType | None
    guidance__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    improvementNotation: fhirtypes.StringType | None
    improvementNotation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    library: list[fhirtypes.ReferenceType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rateAggregation: fhirtypes.StringType | None
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rationale: fhirtypes.MarkdownType | None
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    riskAdjustment: fhirtypes.StringType | None
    riskAdjustment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scoring: fhirtypes.CodeableConceptType | None
    set: fhirtypes.StringType | None
    set__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supplementalData: list[fhirtypes.MeasureSupplementalDataType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: fhirtypes.StringType | None
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureGroup(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    population: list[fhirtypes.MeasureGroupPopulationType] | None
    stratifier: list[fhirtypes.MeasureGroupStratifierType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureGroupPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    criteria: fhirtypes.StringType | None
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureGroupStratifier(backboneelement.BackboneElement):
    __resource_type__: str
    criteria: fhirtypes.StringType | None
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureSupplementalData(backboneelement.BackboneElement):
    __resource_type__: str
    criteria: fhirtypes.StringType | None
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
