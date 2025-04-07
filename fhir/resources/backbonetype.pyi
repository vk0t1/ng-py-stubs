from . import datatype as datatype
from . import fhirtypes as fhirtypes

class BackboneType(datatype.DataType):
    __resource_type__: str
    modifierExtension: list[fhirtypes.ExtensionType] | None
    @classmethod
    def elements_sequence(cls): ...
