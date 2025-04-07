from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Linkage(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: fhirtypes.ReferenceType | None
    item: list[fhirtypes.LinkageItemType]
    @classmethod
    def elements_sequence(cls): ...

class LinkageItem(backboneelement.BackboneElement):
    __resource_type__: str
    resource: fhirtypes.ReferenceType
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
