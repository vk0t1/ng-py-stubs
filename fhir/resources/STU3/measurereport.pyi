from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MeasureReport(domainresource.DomainResource):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    evaluatedResources: fhirtypes.ReferenceType | None
    group: list[fhirtypes.MeasureReportGroupType] | None
    identifier: fhirtypes.IdentifierType | None
    measure: fhirtypes.ReferenceType
    patient: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType
    reportingOrganization: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureReportGroup(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType
    measureScore: fhirtypes.DecimalType | None
    measureScore__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    population: list[fhirtypes.MeasureReportGroupPopulationType] | None
    stratifier: list[fhirtypes.MeasureReportGroupStratifierType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    patients: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType | None
    stratum: list[fhirtypes.MeasureReportGroupStratifierStratumType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    __resource_type__: str
    measureScore: fhirtypes.DecimalType | None
    measureScore__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    population: list[fhirtypes.MeasureReportGroupStratifierStratumPopulationType] | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    patients: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
