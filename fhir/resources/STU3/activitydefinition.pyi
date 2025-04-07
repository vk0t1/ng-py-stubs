from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ActivityDefinition(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType | None
    contact: list[fhirtypes.ContactDetailType] | None
    contributor: list[fhirtypes.ContributorType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dosage: list[fhirtypes.DosageType] | None
    dynamicValue: list[fhirtypes.ActivityDefinitionDynamicValueType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    library: list[fhirtypes.ReferenceType] | None
    location: fhirtypes.ReferenceType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participant: list[fhirtypes.ActivityDefinitionParticipantType] | None
    productCodeableConcept: fhirtypes.CodeableConceptType | None
    productReference: fhirtypes.ReferenceType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDateTime: fhirtypes.DateTimeType | None
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingPeriod: fhirtypes.PeriodType | None
    timingRange: fhirtypes.RangeType | None
    timingTiming: fhirtypes.TimingType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
    transform: fhirtypes.ReferenceType | None
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
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.StringType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    role: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
