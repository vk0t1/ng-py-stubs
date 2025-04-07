from . import element as element
from . import fhirtypes as fhirtypes

class Range(element.Element):
    __resource_type__: str
    high: fhirtypes.QuantityType | None
    low: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
