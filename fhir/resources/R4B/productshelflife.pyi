from . import backboneelement as backboneelement
from . import fhirtypes as fhirtypes

class ProductShelfLife(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType | None
    period: fhirtypes.QuantityType
    specialPrecautionsForStorage: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
