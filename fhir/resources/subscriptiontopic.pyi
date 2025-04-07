from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubscriptionTopic(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    canFilterBy: list[fhirtypes.SubscriptionTopicCanFilterByType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.CanonicalType | None] | None
    derivedFrom__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    eventTrigger: list[fhirtypes.SubscriptionTopicEventTriggerType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notificationShape: list[fhirtypes.SubscriptionTopicNotificationShapeType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resourceTrigger: list[fhirtypes.SubscriptionTopicResourceTriggerType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class SubscriptionTopicCanFilterBy(backboneelement.BackboneElement):
    __resource_type__: str
    comparator: list[fhirtypes.CodeType | None] | None
    comparator__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filterDefinition: fhirtypes.UriType | None
    filterDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filterParameter: fhirtypes.StringType | None
    filterParameter__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeType | None] | None
    modifier__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    resource: fhirtypes.UriType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionTopicEventTrigger(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    event: fhirtypes.CodeableConceptType
    resource: fhirtypes.UriType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionTopicNotificationShape(backboneelement.BackboneElement):
    __resource_type__: str
    include: list[fhirtypes.StringType | None] | None
    include__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    resource: fhirtypes.UriType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    revInclude: list[fhirtypes.StringType | None] | None
    revInclude__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionTopicResourceTrigger(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fhirPathCriteria: fhirtypes.StringType | None
    fhirPathCriteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    queryCriteria: fhirtypes.SubscriptionTopicResourceTriggerQueryCriteriaType | None
    resource: fhirtypes.UriType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportedInteraction: list[fhirtypes.CodeType | None] | None
    supportedInteraction__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionTopicResourceTriggerQueryCriteria(backboneelement.BackboneElement):
    __resource_type__: str
    current: fhirtypes.StringType | None
    current__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    previous: fhirtypes.StringType | None
    previous__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requireBoth: bool | None
    requireBoth__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resultForCreate: fhirtypes.CodeType | None
    resultForCreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resultForDelete: fhirtypes.CodeType | None
    resultForDelete__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
