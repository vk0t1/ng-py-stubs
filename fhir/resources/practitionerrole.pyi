from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PractitionerRole(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availability: list[fhirtypes.AvailabilityType] | None
    characteristic: list[fhirtypes.CodeableConceptType] | None
    code: list[fhirtypes.CodeableConceptType] | None
    communication: list[fhirtypes.CodeableConceptType] | None
    contact: list[fhirtypes.ExtendedContactDetailType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    healthcareService: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: list[fhirtypes.ReferenceType] | None
    organization: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    practitioner: fhirtypes.ReferenceType | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
