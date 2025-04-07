from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceRequest(domainresource.DomainResource):
    __resource_type__: str
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    codeCodeableConcept: fhirtypes.CodeableConceptType | None
    codeReference: fhirtypes.ReferenceType | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    intent: fhirtypes.CodeableConceptType
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    performer: fhirtypes.ReferenceType | None
    performerType: fhirtypes.CodeableConceptType | None
    priorRequest: list[fhirtypes.ReferenceType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.DeviceRequestRequesterType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DeviceRequestRequester(backboneelement.BackboneElement):
    __resource_type__: str
    agent: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
