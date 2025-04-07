from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AuditEvent(domainresource.DomainResource):
    __resource_type__: str
    action: fhirtypes.CodeType | None
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    agent: list[fhirtypes.AuditEventAgentType]
    authorization: list[fhirtypes.CodeableConceptType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    encounter: fhirtypes.ReferenceType | None
    entity: list[fhirtypes.AuditEventEntityType] | None
    occurredDateTime: fhirtypes.DateTimeType | None
    occurredDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurredPeriod: fhirtypes.PeriodType | None
    outcome: fhirtypes.AuditEventOutcomeType | None
    patient: fhirtypes.ReferenceType | None
    recorded: fhirtypes.InstantType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.AuditEventSourceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AuditEventAgent(backboneelement.BackboneElement):
    __resource_type__: str
    authorization: list[fhirtypes.CodeableConceptType] | None
    location: fhirtypes.ReferenceType | None
    networkReference: fhirtypes.ReferenceType | None
    networkString: fhirtypes.StringType | None
    networkString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    networkUri: fhirtypes.UriType | None
    networkUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    policy: list[fhirtypes.UriType | None] | None
    policy__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    requestor: bool | None
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    who: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AuditEventEntity(backboneelement.BackboneElement):
    __resource_type__: str
    agent: list[fhirtypes.AuditEventAgentType] | None
    detail: list[fhirtypes.AuditEventEntityDetailType] | None
    query: fhirtypes.Base64BinaryType | None
    query__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodeableConceptType | None
    securityLabel: list[fhirtypes.CodeableConceptType] | None
    what: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class AuditEventEntityDetail(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AuditEventOutcome(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodingType
    detail: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class AuditEventSource(backboneelement.BackboneElement):
    __resource_type__: str
    observer: fhirtypes.ReferenceType
    site: fhirtypes.ReferenceType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
