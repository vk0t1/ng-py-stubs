from . import element as element
from . import fhirtypes as fhirtypes

class Timing(element.Element):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    event: list[fhirtypes.DateTimeType | None] | None
    event__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    repeat: fhirtypes.TimingRepeatType | None
    @classmethod
    def elements_sequence(cls): ...

class TimingRepeat(element.Element):
    __resource_type__: str
    boundsDuration: fhirtypes.DurationType | None
    boundsPeriod: fhirtypes.PeriodType | None
    boundsRange: fhirtypes.RangeType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    countMax: fhirtypes.IntegerType | None
    countMax__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dayOfWeek: list[fhirtypes.CodeType | None] | None
    dayOfWeek__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    duration: fhirtypes.DecimalType | None
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    durationMax: fhirtypes.DecimalType | None
    durationMax__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    durationUnit: fhirtypes.CodeType | None
    durationUnit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    frequency: fhirtypes.IntegerType | None
    frequency__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    frequencyMax: fhirtypes.IntegerType | None
    frequencyMax__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offset: fhirtypes.UnsignedIntType | None
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.DecimalType | None
    period__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    periodMax: fhirtypes.DecimalType | None
    periodMax__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    periodUnit: fhirtypes.CodeType | None
    periodUnit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timeOfDay: list[fhirtypes.TimeType | None] | None
    timeOfDay__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    when: list[fhirtypes.CodeType | None] | None
    when__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
