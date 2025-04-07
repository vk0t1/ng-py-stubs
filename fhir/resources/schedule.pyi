from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Schedule(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    actor: list[fhirtypes.ReferenceType]
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    planningHorizon: fhirtypes.PeriodType | None
    serviceCategory: list[fhirtypes.CodeableConceptType] | None
    serviceType: list[fhirtypes.CodeableReferenceType] | None
    specialty: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
