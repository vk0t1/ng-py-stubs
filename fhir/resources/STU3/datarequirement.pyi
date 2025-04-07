from . import element as element
from . import fhirtypes as fhirtypes

class DataRequirement(element.Element):
    __resource_type__: str
    codeFilter: list[fhirtypes.DataRequirementCodeFilterType] | None
    dateFilter: list[fhirtypes.DataRequirementDateFilterType] | None
    mustSupport: list[fhirtypes.StringType | None] | None
    mustSupport__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    profile: list[fhirtypes.UriType | None] | None
    profile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DataRequirementCodeFilter(element.Element):
    __resource_type__: str
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: list[fhirtypes.CodeType | None] | None
    valueCode__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    valueCodeableConcept: list[fhirtypes.CodeableConceptType] | None
    valueCoding: list[fhirtypes.CodingType] | None
    valueSetReference: fhirtypes.ReferenceType | None
    valueSetString: fhirtypes.StringType | None
    valueSetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DataRequirementDateFilter(element.Element):
    __resource_type__: str
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDuration: fhirtypes.DurationType | None
    valuePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
