from . import element as element
from . import fhirtypes as fhirtypes

class RatioRange(element.Element):
    __resource_type__: str
    denominator: fhirtypes.QuantityType | None
    highNumerator: fhirtypes.QuantityType | None
    lowNumerator: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
