from . import datatype as datatype
from . import fhirtypes as fhirtypes

class TriggerDefinition(datatype.DataType):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    condition: fhirtypes.ExpressionType | None
    data: list[fhirtypes.DataRequirementType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subscriptionTopic: fhirtypes.CanonicalType | None
    subscriptionTopic__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDate: fhirtypes.DateType | None
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDateTime: fhirtypes.DateTimeType | None
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingReference: fhirtypes.ReferenceType | None
    timingTiming: fhirtypes.TimingType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
