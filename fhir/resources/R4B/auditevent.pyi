from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AuditEvent(domainresource.DomainResource):
    __resource_type__: str
    action: fhirtypes.CodeType | None
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    agent: list[fhirtypes.AuditEventAgentType]
    entity: list[fhirtypes.AuditEventEntityType] | None
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outcomeDesc: fhirtypes.StringType | None
    outcomeDesc__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType | None
    purposeOfEvent: list[fhirtypes.CodeableConceptType] | None
    recorded: fhirtypes.InstantType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.AuditEventSourceType
    subtype: list[fhirtypes.CodingType] | None
    type: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AuditEventAgent(backboneelement.BackboneElement):
    __resource_type__: str
    altId: fhirtypes.StringType | None
    altId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.ReferenceType | None
    media: fhirtypes.CodingType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: fhirtypes.AuditEventAgentNetworkType | None
    policy: list[fhirtypes.UriType | None] | None
    policy__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    purposeOfUse: list[fhirtypes.CodeableConceptType] | None
    requestor: bool | None
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    who: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AuditEventAgentNetwork(backboneelement.BackboneElement):
    __resource_type__: str
    address: fhirtypes.StringType | None
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class AuditEventEntity(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detail: list[fhirtypes.AuditEventEntityDetailType] | None
    lifecycle: fhirtypes.CodingType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    query: fhirtypes.Base64BinaryType | None
    query__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodingType | None
    securityLabel: list[fhirtypes.CodingType] | None
    type: fhirtypes.CodingType | None
    what: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class AuditEventEntityDetail(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.StringType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AuditEventSource(backboneelement.BackboneElement):
    __resource_type__: str
    observer: fhirtypes.ReferenceType
    site: fhirtypes.StringType | None
    site__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodingType] | None
    @classmethod
    def elements_sequence(cls): ...
