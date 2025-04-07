from . import fhirtypes as fhirtypes
from . import primitivetype as primitivetype

class Integer64(primitivetype.PrimitiveType):
    __resource_type__: str
    value: fhirtypes.Integer64Type | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
