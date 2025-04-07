from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ProcedureRequest(domainresource.DomainResource):
    __resource_type__: str
    asNeededBoolean: bool | None
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    performer: fhirtypes.ReferenceType | None
    performerType: fhirtypes.CodeableConceptType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.ProcedureRequestRequesterType | None
    requisition: fhirtypes.IdentifierType | None
    specimen: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ProcedureRequestRequester(backboneelement.BackboneElement):
    __resource_type__: str
    agent: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
