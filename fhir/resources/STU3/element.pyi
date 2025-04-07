from fhir_core import fhirabstractmodel

from . import fhirtypes as fhirtypes

class Element(fhirabstractmodel.FHIRAbstractModel):
    __resource_type__: str
    extension: list[fhirtypes.ExtensionType] | None
    id: fhirtypes.StringType | None
    @classmethod
    def elements_sequence(cls): ...
