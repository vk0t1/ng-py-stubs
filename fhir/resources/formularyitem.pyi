from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class FormularyItem(domainresource.DomainResource):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
