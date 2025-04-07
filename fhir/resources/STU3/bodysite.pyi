from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BodySite(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeableConceptType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    image: list[fhirtypes.AttachmentType] | None
    patient: fhirtypes.ReferenceType
    qualifier: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
