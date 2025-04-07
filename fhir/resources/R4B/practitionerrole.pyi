from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PractitionerRole(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availabilityExceptions: fhirtypes.StringType | None
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableTime: list[fhirtypes.PractitionerRoleAvailableTimeType] | None
    code: list[fhirtypes.CodeableConceptType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    healthcareService: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: list[fhirtypes.ReferenceType] | None
    notAvailable: list[fhirtypes.PractitionerRoleNotAvailableType] | None
    organization: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    practitioner: fhirtypes.ReferenceType | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
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

class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    during: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
