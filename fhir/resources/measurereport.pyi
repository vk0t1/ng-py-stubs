from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MeasureReport(domainresource.DomainResource):
    __resource_type__: str
    dataUpdateType: fhirtypes.CodeType | None
    dataUpdateType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    evaluatedResource: list[fhirtypes.ReferenceType] | None
    group: list[fhirtypes.MeasureReportGroupType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    improvementNotation: fhirtypes.CodeableConceptType | None
    inputParameters: fhirtypes.ReferenceType | None
    location: fhirtypes.ReferenceType | None
    measure: fhirtypes.CanonicalType | None
    measure__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType
    reporter: fhirtypes.ReferenceType | None
    reportingVendor: fhirtypes.ReferenceType | None
    scoring: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    supplementalData: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MeasureReportGroup(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    measureScoreCodeableConcept: fhirtypes.CodeableConceptType | None
    measureScoreDateTime: fhirtypes.DateTimeType | None
    measureScoreDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    measureScoreDuration: fhirtypes.DurationType | None
    measureScorePeriod: fhirtypes.PeriodType | None
    measureScoreQuantity: fhirtypes.QuantityType | None
    measureScoreRange: fhirtypes.RangeType | None
    population: list[fhirtypes.MeasureReportGroupPopulationType] | None
    stratifier: list[fhirtypes.MeasureReportGroupStratifierType] | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectReport: list[fhirtypes.ReferenceType] | None
    subjectResults: fhirtypes.ReferenceType | None
    subjects: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    stratum: list[fhirtypes.MeasureReportGroupStratifierStratumType] | None
    @classmethod
    def elements_sequence(cls): ...

class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    __resource_type__: str
    component: list[fhirtypes.MeasureReportGroupStratifierStratumComponentType] | None
    measureScoreCodeableConcept: fhirtypes.CodeableConceptType | None
    measureScoreDateTime: fhirtypes.DateTimeType | None
    measureScoreDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    measureScoreDuration: fhirtypes.DurationType | None
    measureScorePeriod: fhirtypes.PeriodType | None
    measureScoreQuantity: fhirtypes.QuantityType | None
    measureScoreRange: fhirtypes.RangeType | None
    population: list[fhirtypes.MeasureReportGroupStratifierStratumPopulationType] | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectReport: list[fhirtypes.ReferenceType] | None
    subjectResults: fhirtypes.ReferenceType | None
    subjects: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
