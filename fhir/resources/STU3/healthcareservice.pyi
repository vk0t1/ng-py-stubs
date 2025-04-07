from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class HealthcareService(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    appointmentRequired: bool | None
    appointmentRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availabilityExceptions: fhirtypes.StringType | None
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableTime: list[fhirtypes.HealthcareServiceAvailableTimeType] | None
    category: fhirtypes.CodeableConceptType | None
    characteristic: list[fhirtypes.CodeableConceptType] | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    coverageArea: list[fhirtypes.ReferenceType] | None
    eligibility: fhirtypes.CodeableConceptType | None
    eligibilityNote: fhirtypes.StringType | None
    eligibilityNote__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    extraDetails: fhirtypes.StringType | None
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: list[fhirtypes.ReferenceType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notAvailable: list[fhirtypes.HealthcareServiceNotAvailableType] | None
    photo: fhirtypes.AttachmentType | None
    programName: list[fhirtypes.StringType | None] | None
    programName__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    providedBy: fhirtypes.ReferenceType | None
    referralMethod: list[fhirtypes.CodeableConceptType] | None
    serviceProvisionCode: list[fhirtypes.CodeableConceptType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    __resource_type__: str
    allDay: bool | None
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableEndTime: fhirtypes.TimeType | None
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableStartTime: fhirtypes.TimeType | None
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    daysOfWeek: list[fhirtypes.CodeType | None] | None
    daysOfWeek__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    during: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
