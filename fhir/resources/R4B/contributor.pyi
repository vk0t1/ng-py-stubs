from . import element as element
from . import fhirtypes as fhirtypes

class Contributor(element.Element):
    __resource_type__: str
    contact: list[fhirtypes.ContactDetailType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
