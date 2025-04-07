from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceDispense(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    destination: fhirtypes.ReferenceType | None
    device: fhirtypes.CodeableReferenceType
    encounter: fhirtypes.ReferenceType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.DeviceDispensePerformerType] | None
    preparedDate: fhirtypes.DateTimeType | None
    preparedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    receiver: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableReferenceType | None
    subject: fhirtypes.ReferenceType
    supportingInformation: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    usageInstruction: fhirtypes.MarkdownType | None
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenHandedOver: fhirtypes.DateTimeType | None
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDispensePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
