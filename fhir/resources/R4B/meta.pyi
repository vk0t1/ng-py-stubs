from . import element as element
from . import fhirtypes as fhirtypes

class Meta(element.Element):
    __resource_type__: str
    lastUpdated: fhirtypes.InstantType | None
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: list[fhirtypes.CanonicalType | None] | None
    profile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    security: list[fhirtypes.CodingType] | None
    source: fhirtypes.UriType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tag: list[fhirtypes.CodingType] | None
    versionId: fhirtypes.IdType | None
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
