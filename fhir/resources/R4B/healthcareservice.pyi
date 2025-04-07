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
    category: list[fhirtypes.CodeableConceptType] | None
    characteristic: list[fhirtypes.CodeableConceptType] | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.CodeableConceptType] | None
    coverageArea: list[fhirtypes.ReferenceType] | None
    eligibility: list[fhirtypes.HealthcareServiceEligibilityType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    extraDetails: fhirtypes.MarkdownType | None
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: list[fhirtypes.ReferenceType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notAvailable: list[fhirtypes.HealthcareServiceNotAvailableType] | None
    photo: fhirtypes.AttachmentType | None
    program: list[fhirtypes.CodeableConceptType] | None
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

class HealthcareServiceEligibility(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
