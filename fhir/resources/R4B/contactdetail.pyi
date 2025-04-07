from . import element as element
from . import fhirtypes as fhirtypes

class ContactDetail(element.Element):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
