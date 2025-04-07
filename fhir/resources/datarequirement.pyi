from . import datatype as datatype
from . import element as element
from . import fhirtypes as fhirtypes

class DataRequirement(datatype.DataType):
    __resource_type__: str
    codeFilter: list[fhirtypes.DataRequirementCodeFilterType] | None
    dateFilter: list[fhirtypes.DataRequirementDateFilterType] | None
    limit: fhirtypes.PositiveIntType | None
    limit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mustSupport: list[fhirtypes.StringType | None] | None
    mustSupport__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    profile: list[fhirtypes.CanonicalType | None] | None
    profile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sort: list[fhirtypes.DataRequirementSortType] | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueFilter: list[fhirtypes.DataRequirementValueFilterType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DataRequirementCodeFilter(element.Element):
    __resource_type__: str
    code: list[fhirtypes.CodingType] | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    searchParam: fhirtypes.StringType | None
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class DataRequirementDateFilter(element.Element):
    __resource_type__: str
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    searchParam: fhirtypes.StringType | None
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDuration: fhirtypes.DurationType | None
    valuePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DataRequirementSort(element.Element):
    __resource_type__: str
    direction: fhirtypes.CodeType | None
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DataRequirementValueFilter(element.Element):
    __resource_type__: str
    comparator: fhirtypes.CodeType | None
    comparator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    searchParam: fhirtypes.StringType | None
    searchParam__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDuration: fhirtypes.DurationType | None
    valuePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
