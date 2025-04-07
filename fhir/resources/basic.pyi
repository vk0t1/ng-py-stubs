from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Basic(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    code: fhirtypes.CodeableConceptType
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
