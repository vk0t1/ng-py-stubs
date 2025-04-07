from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Range(datatype.DataType):
    __resource_type__: str
    high: fhirtypes.QuantityType | None
    low: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
