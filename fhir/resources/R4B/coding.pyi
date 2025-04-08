from . import element as element
from . import fhirtypes as fhirtypes

class Coding(element.Element):
    __resource_type__: str = "Coding"
    code: fhirtypes.CodeType | None = None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    display: fhirtypes.StringType | None = None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    system: fhirtypes.UriType | None = None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    userSelected: bool | None = None
    userSelected__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    version: fhirtypes.StringType | None = None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
