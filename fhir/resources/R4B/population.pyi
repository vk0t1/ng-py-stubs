from . import backboneelement as backboneelement
from . import fhirtypes as fhirtypes

class Population(backboneelement.BackboneElement):
    __resource_type__: str
    ageCodeableConcept: fhirtypes.CodeableConceptType | None
    ageRange: fhirtypes.RangeType | None
    gender: fhirtypes.CodeableConceptType | None
    physiologicalCondition: fhirtypes.CodeableConceptType | None
    race: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
