from fhir_core import fhirabstractmodel

from . import fhirtypes as fhirtypes

class Element(fhirabstractmodel.FHIRAbstractModel):
    __resource_type__: str = "Element"
    extension: list[fhirtypes.ExtensionType] | None = None
    id: fhirtypes.StringType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
