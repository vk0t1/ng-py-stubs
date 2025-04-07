from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Ratio(datatype.DataType):
    __resource_type__: str
    denominator: fhirtypes.QuantityType | None
    numerator: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
