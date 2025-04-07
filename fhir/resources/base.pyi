from fhir_core import fhirabstractmodel

class Base(fhirabstractmodel.FHIRAbstractModel):
    __resource_type__: str
    @classmethod
    def elements_sequence(cls): ...
