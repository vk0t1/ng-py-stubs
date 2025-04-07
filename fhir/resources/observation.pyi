from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Observation(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    bodyStructure: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    component: list[fhirtypes.ObservationComponentType] | None
    dataAbsentReason: fhirtypes.CodeableConceptType | None
    derivedFrom: list[fhirtypes.ReferenceType] | None
    device: fhirtypes.ReferenceType | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectiveInstant: fhirtypes.InstantType | None
    effectiveInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    effectiveTiming: fhirtypes.TimingType | None
    encounter: fhirtypes.ReferenceType | None
    focus: list[fhirtypes.ReferenceType] | None
    hasMember: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: fhirtypes.CanonicalType | None
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instantiatesReference: fhirtypes.ReferenceType | None
    interpretation: list[fhirtypes.CodeableConceptType] | None
    issued: fhirtypes.InstantType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.ReferenceType] | None
    referenceRange: list[fhirtypes.ObservationReferenceRangeType] | None
    specimen: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    triggeredBy: list[fhirtypes.ObservationTriggeredByType] | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueReference: fhirtypes.ReferenceType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ObservationComponent(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    dataAbsentReason: fhirtypes.CodeableConceptType | None
    interpretation: list[fhirtypes.CodeableConceptType] | None
    referenceRange: list[fhirtypes.ObservationReferenceRangeType] | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueReference: fhirtypes.ReferenceType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ObservationReferenceRange(backboneelement.BackboneElement):
    __resource_type__: str
    age: fhirtypes.RangeType | None
    appliesTo: list[fhirtypes.CodeableConceptType] | None
    high: fhirtypes.QuantityType | None
    low: fhirtypes.QuantityType | None
    normalValue: fhirtypes.CodeableConceptType | None
    text: fhirtypes.MarkdownType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ObservationTriggeredBy(backboneelement.BackboneElement):
    __resource_type__: str
    observation: fhirtypes.ReferenceType
    reason: fhirtypes.StringType | None
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
