from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubscriptionStatus(domainresource.DomainResource):
    __resource_type__: str
    error: list[fhirtypes.CodeableConceptType] | None
    eventsSinceSubscriptionStart: fhirtypes.Integer64Type | None
    eventsSinceSubscriptionStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notificationEvent: list[fhirtypes.SubscriptionStatusNotificationEventType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subscription: fhirtypes.ReferenceType
    topic: fhirtypes.CanonicalType | None
    topic__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubscriptionStatusNotificationEvent(backboneelement.BackboneElement):
    __resource_type__: str
    additionalContext: list[fhirtypes.ReferenceType] | None
    eventNumber: fhirtypes.Integer64Type | None
    eventNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    focus: fhirtypes.ReferenceType | None
    timestamp: fhirtypes.InstantType | None
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
