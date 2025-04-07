from . import datatype as datatype
from . import fhirtypes as fhirtypes

class CodeableReference(datatype.DataType):
    __resource_type__: str
    concept: fhirtypes.CodeableConceptType | None
    reference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
