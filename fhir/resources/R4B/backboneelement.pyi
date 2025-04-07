from . import element as element
from . import fhirtypes as fhirtypes

class BackboneElement(element.Element):
    __resource_type__: str
    modifierExtension: list[fhirtypes.ExtensionType] | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
