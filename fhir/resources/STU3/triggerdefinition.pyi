from . import element as element
from . import fhirtypes as fhirtypes

class TriggerDefinition(element.Element):
    __resource_type__: str
    eventData: fhirtypes.DataRequirementType | None
    eventName: fhirtypes.StringType | None
    eventName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventTimingDate: fhirtypes.DateType | None
    eventTimingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventTimingDateTime: fhirtypes.DateTimeType | None
    eventTimingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventTimingReference: fhirtypes.ReferenceType | None
    eventTimingTiming: fhirtypes.TimingType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
