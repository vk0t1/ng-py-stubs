from . import element as element
from . import fhirtypes as fhirtypes

class CodeableReference(element.Element):
    __resource_type__: str
    concept: fhirtypes.CodeableConceptType | None
    reference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
