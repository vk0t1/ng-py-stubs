from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Slot(domainresource.DomainResource):
    __resource_type__: str
    appointmentType: list[fhirtypes.CodeableConceptType] | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.InstantType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    overbooked: bool | None
    overbooked__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    schedule: fhirtypes.ReferenceType
    serviceCategory: list[fhirtypes.CodeableConceptType] | None
    serviceType: list[fhirtypes.CodeableReferenceType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    start: fhirtypes.InstantType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
