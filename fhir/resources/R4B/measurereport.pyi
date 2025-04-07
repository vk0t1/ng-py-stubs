from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MeasureReport(domainresource.DomainResource):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    evaluatedResource: list[fhirtypes.ReferenceType] | None
    group: list[fhirtypes.MeasureReportGroupType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    improvementNotation: fhirtypes.CodeableConceptType | None
    measure: fhirtypes.CanonicalType | None
    measure__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType
    reporter: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureReportGroup(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    measureScore: fhirtypes.QuantityType | None
    population: list[fhirtypes.MeasureReportGroupPopulationType] | None
    stratifier: list[fhirtypes.MeasureReportGroupStratifierType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectResults: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodeableConceptType] | None
    stratum: list[fhirtypes.MeasureReportGroupStratifierStratumType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    __resource_type__: str
    component: list[fhirtypes.MeasureReportGroupStratifierStratumComponentType] | None
    measureScore: fhirtypes.QuantityType | None
    population: list[fhirtypes.MeasureReportGroupStratifierStratumPopulationType] | None
    value: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    value: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectResults: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
