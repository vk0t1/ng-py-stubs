from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AppointmentResponse(domainresource.DomainResource):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    appointment: fhirtypes.ReferenceType
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    participantStatus: fhirtypes.CodeType | None
    participantStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participantType: list[fhirtypes.CodeableConceptType] | None
    start: fhirtypes.InstantType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
