from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Appointment(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    appointmentType: fhirtypes.CodeableConceptType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    cancellationDate: fhirtypes.DateTimeType | None
    cancellationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    cancellationReason: fhirtypes.CodeableConceptType | None
    class_fhir: list[fhirtypes.CodeableConceptType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    minutesDuration: fhirtypes.PositiveIntType | None
    minutesDuration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceChanged: bool | None
    occurrenceChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    originatingAppointment: fhirtypes.ReferenceType | None
    participant: list[fhirtypes.AppointmentParticipantType]
    patientInstruction: list[fhirtypes.CodeableReferenceType] | None
    previousAppointment: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeableConceptType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    recurrenceId: fhirtypes.PositiveIntType | None
    recurrenceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recurrenceTemplate: list[fhirtypes.AppointmentRecurrenceTemplateType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    requestedPeriod: list[fhirtypes.PeriodType] | None
    serviceCategory: list[fhirtypes.CodeableConceptType] | None
    serviceType: list[fhirtypes.CodeableReferenceType] | None
    slot: list[fhirtypes.ReferenceType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    start: fhirtypes.InstantType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    virtualService: list[fhirtypes.VirtualServiceDetailType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AppointmentParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    required: bool | None
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AppointmentRecurrenceTemplate(backboneelement.BackboneElement):
    __resource_type__: str
    excludingDate: list[fhirtypes.DateType | None] | None
    excludingDate__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    excludingRecurrenceId: list[fhirtypes.PositiveIntType | None] | None
    excludingRecurrenceId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    lastOccurrenceDate: fhirtypes.DateType | None
    lastOccurrenceDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    monthlyTemplate: fhirtypes.AppointmentRecurrenceTemplateMonthlyTemplateType | None
    occurrenceCount: fhirtypes.PositiveIntType | None
    occurrenceCount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrenceDate: list[fhirtypes.DateType | None] | None
    occurrenceDate__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    recurrenceType: fhirtypes.CodeableConceptType
    timezone: fhirtypes.CodeableConceptType | None
    weeklyTemplate: fhirtypes.AppointmentRecurrenceTemplateWeeklyTemplateType | None
    yearlyTemplate: fhirtypes.AppointmentRecurrenceTemplateYearlyTemplateType | None
    @classmethod
    def elements_sequence(cls): ...

class AppointmentRecurrenceTemplateMonthlyTemplate(backboneelement.BackboneElement):
    __resource_type__: str
    dayOfMonth: fhirtypes.PositiveIntType | None
    dayOfMonth__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dayOfWeek: fhirtypes.CodingType | None
    monthInterval: fhirtypes.PositiveIntType | None
    monthInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nthWeekOfMonth: fhirtypes.CodingType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AppointmentRecurrenceTemplateWeeklyTemplate(backboneelement.BackboneElement):
    __resource_type__: str
    friday: bool | None
    friday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    monday: bool | None
    monday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    saturday: bool | None
    saturday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sunday: bool | None
    sunday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    thursday: bool | None
    thursday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tuesday: bool | None
    tuesday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    wednesday: bool | None
    wednesday__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    weekInterval: fhirtypes.PositiveIntType | None
    weekInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class AppointmentRecurrenceTemplateYearlyTemplate(backboneelement.BackboneElement):
    __resource_type__: str
    yearInterval: fhirtypes.PositiveIntType | None
    yearInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
