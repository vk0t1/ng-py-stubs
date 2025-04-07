from . import backbonetype as backbonetype
from . import fhirtypes as fhirtypes

class ProductShelfLife(backbonetype.BackboneType):
    __resource_type__: str
    periodDuration: fhirtypes.DurationType | None
    periodString: fhirtypes.StringType | None
    periodString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    specialPrecautionsForStorage: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
