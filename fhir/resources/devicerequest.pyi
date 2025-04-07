from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceRequest(domainresource.DomainResource):
    __resource_type__: str
    asNeeded: bool | None
    asNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededFor: fhirtypes.CodeableConceptType | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableReferenceType
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    insurance: list[fhirtypes.ReferenceType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    parameter: list[fhirtypes.DeviceRequestParameterType] | None
    performer: fhirtypes.CodeableReferenceType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.IntegerType | None
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DeviceRequestParameter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
