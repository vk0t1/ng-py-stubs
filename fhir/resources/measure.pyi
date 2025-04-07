from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Measure(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    basis: fhirtypes.CodeType | None
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    clinicalRecommendationStatement: fhirtypes.MarkdownType | None
    clinicalRecommendationStatement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compositeScoring: fhirtypes.CodeableConceptType | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disclaimer: fhirtypes.MarkdownType | None
    disclaimer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    editor: list[fhirtypes.ContactDetailType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    endorser: list[fhirtypes.ContactDetailType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    group: list[fhirtypes.MeasureGroupType] | None
    guidance: fhirtypes.MarkdownType | None
    guidance__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    improvementNotation: fhirtypes.CodeableConceptType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    library: list[fhirtypes.CanonicalType | None] | None
    library__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rateAggregation: fhirtypes.MarkdownType | None
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rationale: fhirtypes.MarkdownType | None
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    riskAdjustment: fhirtypes.MarkdownType | None
    riskAdjustment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scoring: fhirtypes.CodeableConceptType | None
    scoringUnit: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supplementalData: list[fhirtypes.MeasureSupplementalDataType] | None
    term: list[fhirtypes.MeasureTermType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: fhirtypes.MarkdownType | None
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MeasureGroup(backboneelement.BackboneElement):
    __resource_type__: str
    basis: fhirtypes.CodeType | None
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeableConceptType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    improvementNotation: fhirtypes.CodeableConceptType | None
    library: list[fhirtypes.CanonicalType | None] | None
    library__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    population: list[fhirtypes.MeasureGroupPopulationType] | None
    rateAggregation: fhirtypes.MarkdownType | None
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scoring: fhirtypes.CodeableConceptType | None
    scoringUnit: fhirtypes.CodeableConceptType | None
    stratifier: list[fhirtypes.MeasureGroupStratifierType] | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MeasureGroupPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    aggregateMethod: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    criteria: fhirtypes.ExpressionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    groupDefinition: fhirtypes.ReferenceType | None
    inputPopulationId: fhirtypes.StringType | None
    inputPopulationId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureGroupStratifier(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    component: list[fhirtypes.MeasureGroupStratifierComponentType] | None
    criteria: fhirtypes.ExpressionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    groupDefinition: fhirtypes.ReferenceType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    criteria: fhirtypes.ExpressionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    groupDefinition: fhirtypes.ReferenceType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureSupplementalData(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    criteria: fhirtypes.ExpressionType
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureTerm(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    definition: fhirtypes.MarkdownType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
