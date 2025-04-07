from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Schedule(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    actor: list[fhirtypes.ReferenceType]
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    planningHorizon: fhirtypes.PeriodType | None
    serviceCategory: fhirtypes.CodeableConceptType | None
    serviceType: list[fhirtypes.CodeableConceptType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
