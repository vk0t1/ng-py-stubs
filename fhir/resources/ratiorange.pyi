from . import datatype as datatype
from . import fhirtypes as fhirtypes

class RatioRange(datatype.DataType):
    __resource_type__: str
    denominator: fhirtypes.QuantityType | None
    highNumerator: fhirtypes.QuantityType | None
    lowNumerator: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
