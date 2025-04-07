from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BodyStructure(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    image: list[fhirtypes.AttachmentType] | None
    location: fhirtypes.CodeableConceptType | None
    locationQualifier: list[fhirtypes.CodeableConceptType] | None
    morphology: fhirtypes.CodeableConceptType | None
    patient: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
