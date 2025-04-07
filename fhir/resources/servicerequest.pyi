from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ServiceRequest(domainresource.DomainResource):
    __resource_type__: str
    asNeededBoolean: bool | None
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    bodyStructure: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableReferenceType | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    focus: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    insurance: list[fhirtypes.ReferenceType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: list[fhirtypes.CodeableReferenceType] | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    orderDetail: list[fhirtypes.ServiceRequestOrderDetailType] | None
    patientInstruction: list[fhirtypes.ServiceRequestPatientInstructionType] | None
    performer: list[fhirtypes.ReferenceType] | None
    performerType: fhirtypes.CodeableConceptType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantityQuantity: fhirtypes.QuantityType | None
    quantityRange: fhirtypes.RangeType | None
    quantityRatio: fhirtypes.RatioType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.ReferenceType | None
    requisition: fhirtypes.IdentifierType | None
    specimen: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.CodeableReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ServiceRequestOrderDetail(backboneelement.BackboneElement):
    __resource_type__: str
    parameter: list[fhirtypes.ServiceRequestOrderDetailParameterType]
    parameterFocus: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class ServiceRequestOrderDetailParameter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valuePeriod: fhirtypes.PeriodType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ServiceRequestPatientInstruction(backboneelement.BackboneElement):
    __resource_type__: str
    instructionMarkdown: fhirtypes.MarkdownType | None
    instructionMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instructionReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
