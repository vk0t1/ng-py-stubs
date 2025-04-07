from . import datatype as datatype
from . import element as element
from . import fhirtypes as fhirtypes

class Availability(datatype.DataType):
    __resource_type__: str
    availableTime: list[fhirtypes.AvailabilityAvailableTimeType] | None
    notAvailableTime: list[fhirtypes.AvailabilityNotAvailableTimeType] | None
    @classmethod
    def elements_sequence(cls): ...

class AvailabilityAvailableTime(element.Element):
    __resource_type__: str
    allDay: bool | None
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableEndTime: fhirtypes.TimeType | None
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    availableStartTime: fhirtypes.TimeType | None
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    daysOfWeek: list[fhirtypes.CodeType | None] | None
    daysOfWeek__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class AvailabilityNotAvailableTime(element.Element):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    during: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
