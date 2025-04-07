from . import datatype as datatype
from . import fhirtypes as fhirtypes

class UsageContext(datatype.DataType):
    __resource_type__: str
    code: fhirtypes.CodingType
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
