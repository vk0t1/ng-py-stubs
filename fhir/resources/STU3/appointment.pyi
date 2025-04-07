from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Appointment(domainresource.DomainResource):
    __resource_type__: str
    appointmentType: fhirtypes.CodeableConceptType | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    incomingReferral: list[fhirtypes.ReferenceType] | None
    indication: list[fhirtypes.ReferenceType] | None
    minutesDuration: fhirtypes.PositiveIntType | None
    minutesDuration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participant: list[fhirtypes.AppointmentParticipantType]
    priority: fhirtypes.UnsignedIntType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableConceptType] | None
    requestedPeriod: list[fhirtypes.PeriodType] | None
    serviceCategory: fhirtypes.CodeableConceptType | None
    serviceType: list[fhirtypes.CodeableConceptType] | None
    slot: list[fhirtypes.ReferenceType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    start: fhirtypes.InstantType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AppointmentParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    required: fhirtypes.CodeType | None
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
