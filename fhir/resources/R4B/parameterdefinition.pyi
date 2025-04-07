from . import element as element
from . import fhirtypes as fhirtypes

class ParameterDefinition(element.Element):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    max: fhirtypes.StringType | None
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    min: fhirtypes.IntegerType | None
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.CodeType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: fhirtypes.CanonicalType | None
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
