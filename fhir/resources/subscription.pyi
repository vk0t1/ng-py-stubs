from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Subscription(domainresource.DomainResource):
    __resource_type__: str
    channelType: fhirtypes.CodingType
    contact: list[fhirtypes.ContactPointType] | None
    content: fhirtypes.CodeType | None
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: fhirtypes.UrlType | None
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filterBy: list[fhirtypes.SubscriptionFilterByType] | None
    heartbeatPeriod: fhirtypes.UnsignedIntType | None
    heartbeatPeriod__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingEntity: fhirtypes.ReferenceType | None
    maxCount: fhirtypes.PositiveIntType | None
    maxCount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameter: list[fhirtypes.SubscriptionParameterType] | None
    reason: fhirtypes.StringType | None
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timeout: fhirtypes.UnsignedIntType | None
    timeout__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: fhirtypes.CanonicalType | None
    topic__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionFilterBy(backboneelement.BackboneElement):
    __resource_type__: str
    comparator: fhirtypes.CodeType | None
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filterParameter: fhirtypes.StringType | None
    filterParameter__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: fhirtypes.CodeType | None
    modifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resourceType: fhirtypes.UriType | None
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionParameter(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
