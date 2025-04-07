from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Subscription(domainresource.DomainResource):
    __resource_type__: str
    channel: fhirtypes.SubscriptionChannelType
    contact: list[fhirtypes.ContactPointType] | None
    criteria: fhirtypes.StringType | None
    criteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    error: fhirtypes.StringType | None
    error__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: fhirtypes.StringType | None
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tag: list[fhirtypes.CodingType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionChannel(backboneelement.BackboneElement):
    __resource_type__: str
    endpoint: fhirtypes.UriType | None
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    header: list[fhirtypes.StringType | None] | None
    header__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    payload: fhirtypes.StringType | None
    payload__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
