from . import element as element
from . import fhirtypes as fhirtypes

class Narrative(element.Element):
    __resource_type__: str
    div: fhirtypes.XhtmlType | None
    div__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
