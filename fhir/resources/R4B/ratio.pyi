from . import element as element
from . import fhirtypes as fhirtypes

class Ratio(element.Element):
    __resource_type__: str
    denominator: fhirtypes.QuantityType | None
    numerator: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
