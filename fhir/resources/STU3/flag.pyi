from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Flag(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
