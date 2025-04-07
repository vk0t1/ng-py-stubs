from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class HealthcareService(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    appointmentRequired: bool | None
    appointmentRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availability: list[fhirtypes.AvailabilityType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    characteristic: list[fhirtypes.CodeableConceptType] | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.CodeableConceptType] | None
    contact: list[fhirtypes.ExtendedContactDetailType] | None
    coverageArea: list[fhirtypes.ReferenceType] | None
    eligibility: list[fhirtypes.HealthcareServiceEligibilityType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    extraDetails: fhirtypes.MarkdownType | None
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: list[fhirtypes.ReferenceType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offeredIn: list[fhirtypes.ReferenceType] | None
    photo: fhirtypes.AttachmentType | None
    program: list[fhirtypes.CodeableConceptType] | None
    providedBy: fhirtypes.ReferenceType | None
    referralMethod: list[fhirtypes.CodeableConceptType] | None
    serviceProvisionCode: list[fhirtypes.CodeableConceptType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class HealthcareServiceEligibility(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
