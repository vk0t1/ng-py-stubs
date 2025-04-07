from . import datatype as datatype
from . import fhirtypes as fhirtypes

class MonetaryComponent(datatype.DataType):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    code: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
