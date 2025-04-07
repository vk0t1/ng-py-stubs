from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ResearchElementDefinition(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    characteristic: list[fhirtypes.ResearchElementDefinitionCharacteristicType]
    comment: list[fhirtypes.StringType | None] | None
    comment__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    editor: list[fhirtypes.ContactDetailType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    endorser: list[fhirtypes.ContactDetailType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
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
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    shortTitle: fhirtypes.StringType | None
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: fhirtypes.StringType | None
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    variableType: fhirtypes.CodeType | None
    variableType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    definitionCanonical: fhirtypes.CanonicalType | None
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionCodeableConcept: fhirtypes.CodeableConceptType | None
    definitionDataRequirement: fhirtypes.DataRequirementType | None
    definitionExpression: fhirtypes.ExpressionType | None
    exclude: bool | None
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participantEffectiveDateTime: fhirtypes.DateTimeType | None
    participantEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participantEffectiveDescription: fhirtypes.StringType | None
    participantEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participantEffectiveDuration: fhirtypes.DurationType | None
    participantEffectiveGroupMeasure: fhirtypes.CodeType | None
    participantEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participantEffectivePeriod: fhirtypes.PeriodType | None
    participantEffectiveTimeFromStart: fhirtypes.DurationType | None
    participantEffectiveTiming: fhirtypes.TimingType | None
    studyEffectiveDateTime: fhirtypes.DateTimeType | None
    studyEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyEffectiveDescription: fhirtypes.StringType | None
    studyEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyEffectiveDuration: fhirtypes.DurationType | None
    studyEffectiveGroupMeasure: fhirtypes.CodeType | None
    studyEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyEffectivePeriod: fhirtypes.PeriodType | None
    studyEffectiveTimeFromStart: fhirtypes.DurationType | None
    studyEffectiveTiming: fhirtypes.TimingType | None
    unitOfMeasure: fhirtypes.CodeableConceptType | None
    usageContext: list[fhirtypes.UsageContextType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
