from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Procedure(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType | None
    complication: list[fhirtypes.CodeableReferenceType] | None
    encounter: fhirtypes.ReferenceType | None
    focalDevice: list[fhirtypes.ProcedureFocalDeviceType] | None
    focus: fhirtypes.ReferenceType | None
    followUp: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    location: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceAge: fhirtypes.AgeType | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceRange: fhirtypes.RangeType | None
    occurrenceString: fhirtypes.StringType | None
    occurrenceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrenceTiming: fhirtypes.TimingType | None
    outcome: fhirtypes.CodeableConceptType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.ProcedurePerformerType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    recorded: fhirtypes.DateTimeType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recorder: fhirtypes.ReferenceType | None
    report: list[fhirtypes.ReferenceType] | None
    reportedBoolean: bool | None
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reportedReference: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.ReferenceType] | None
    used: list[fhirtypes.CodeableReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ProcedureFocalDevice(backboneelement.BackboneElement):
    __resource_type__: str
    action: fhirtypes.CodeableConceptType | None
    manipulated: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class ProcedurePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    onBehalfOf: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
